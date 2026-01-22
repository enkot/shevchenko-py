import re
import json
import os
from typing import List, Optional, TypedDict, Dict, Any
from shevchenko.language import GrammaticalCase, GrammaticalGender, WordClass
from shevchenko.word_declension.word_inflector import WordInflector, DeclensionParams

class WordHyphenationRule(TypedDict, total=False):
    include: List[str]
    useCase: Optional[str]

class WordClassifierRule(TypedDict):
    gender: str
    wordClass: str
    include: List[str]

class ExtractedWordResult:
    def __init__(self, extracted_word: str, start_delimiter: str, end_delimiter: str):
        self.extracted_word = extracted_word
        self.start_delimiter = start_delimiter
        self.end_delimiter = end_delimiter

class MilitaryInflector:
    def __init__(self, word_inflector: WordInflector, 
                 word_hyphenation_rules: List[WordHyphenationRule] = None, 
                 word_classifier_rules: List[WordClassifierRule] = None):
        self.word_inflector = word_inflector
        self.word_hyphenation_rules = word_hyphenation_rules or self._load_hyphenation_rules()
        self.word_classifier_rules = word_classifier_rules or self._load_classifier_rules()

    def _load_hyphenation_rules(self) -> List[WordHyphenationRule]:
        path = os.path.join(os.path.dirname(__file__), 'word-hyphenation-rules.json')
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _load_classifier_rules(self) -> List[WordClassifierRule]:
        path = os.path.join(os.path.dirname(__file__), 'word-classifier-rules.json')
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def inflect(self, words: str, grammatical_case: GrammaticalCase, use_case: str) -> str:
        word_parts = []
        for word in words.split(' '):
            hyphenated_rule = self._find_hyphenation_rule(word, use_case)
            
            if hyphenated_rule:
                word_parts.append(self._inflect_hyphenated_word(word, grammatical_case))
            else:
                word_parts.append(self._inflect_word(word, grammatical_case))
        
        return ' '.join(word_parts)

    def _find_hyphenation_rule(self, word: str, use_case: str) -> Optional[WordHyphenationRule]:
        for rule in self.word_hyphenation_rules:
            rule_use_case = rule.get('useCase')
            if rule_use_case is not None and rule_use_case != use_case:
                continue
            
            if all(self._check_pattern(pattern, word) for pattern in rule['include']):
                return rule
        return None
    
    def _check_pattern(self, pattern: str, word: str) -> bool:
        # Regex check corresponding to new RegExp(pattern, 'i').test(word)
        try:
             return bool(re.search(pattern, word, re.IGNORECASE))
        except re.error:
            # Fallback or error logging if pattern is invalid python regex
            return False

    def _inflect_hyphenated_word(self, words: str, grammatical_case: GrammaticalCase) -> str:
        word_parts = []
        for word in words.split('-'):
            word_parts.append(self._inflect_word(word, grammatical_case))
        return '-'.join(word_parts)

    def _inflect_word(self, word: str, grammatical_case: GrammaticalCase) -> str:
        extracted = self.extract_word_delimiters(word)
        
        rule = self._find_classifier_rule(extracted.extracted_word)
        
        if rule is None:
            return word
            
        gender = GrammaticalGender(rule['gender'])
        word_class = WordClass(rule['wordClass'])
        
        params = DeclensionParams(
            grammatical_case=grammatical_case,
            gender=gender,
            word_class=word_class
        )
        
        inflected_word = self.word_inflector.inflect(extracted.extracted_word, params)
        
        return extracted.start_delimiter + inflected_word + extracted.end_delimiter

    def _find_classifier_rule(self, word: str) -> Optional[WordClassifierRule]:
        for rule in self.word_classifier_rules:
            if all(self._check_pattern(pattern, word) for pattern in rule['include']):
                return rule
        return None

    def extract_word_delimiters(self, word: str) -> ExtractedWordResult:
        extracted_word = word
        start_delimiter = ''
        end_delimiter = ''
        
        # Matches punctuation at start
        start_match = re.match(r'^(["\'()]+)', extracted_word)
        if start_match:
            start_delimiter = start_match.group(0)
            extracted_word = extracted_word[len(start_delimiter):]
            
        # Matches punctuation at end
        end_match = re.search(r'(["\'()]+)$', extracted_word)
        if end_match:
            end_delimiter = end_match.group(0)
            extracted_word = extracted_word[:end_match.start()]
            
        return ExtractedWordResult(extracted_word, start_delimiter, end_delimiter)
