from typing import List, Optional, Callable, Dict
from shevchenko.language import GrammaticalCase, GrammaticalGender, WordClass
from shevchenko.word_declension.declension_types import DeclensionRule, ApplicationType
from shevchenko.word_declension.declension_rule_inflector import DeclensionRuleInflector
import regex as re

CustomRuleFilter = Callable[[DeclensionRule, int, List[DeclensionRule]], bool]

class DeclensionParams:
    grammatical_case: GrammaticalCase
    gender: GrammaticalGender
    word_class: Optional[WordClass] = None
    application_type: Optional[ApplicationType] = None
    custom_rule_filter: Optional[CustomRuleFilter] = None

    def __init__(self, grammatical_case: GrammaticalCase, gender: GrammaticalGender, 
                 word_class: Optional[WordClass] = None, 
                 application_type: Optional[ApplicationType] = None,
                 custom_rule_filter: Optional[CustomRuleFilter] = None):
        self.grammatical_case = grammatical_case
        self.gender = gender
        self.word_class = word_class
        self.application_type = application_type
        self.custom_rule_filter = custom_rule_filter

class WordInflector:
    def __init__(self, declension_rules: List[DeclensionRule]):
        # Sort by priority descending
        self.declension_rules = sorted(declension_rules, key=lambda r: r['priority'], reverse=True)

    def inflect(self, word: str, params: DeclensionParams) -> str:
        matching_rule = self._find_first_matching_rule(word, params)

        if matching_rule is None:
            return word

        return DeclensionRuleInflector(matching_rule).inflect(word, params.grammatical_case)

    def _find_first_matching_rule(self, word: str, params: DeclensionParams) -> Optional[DeclensionRule]:
        # Filter rules
        for i, rule in enumerate(self.declension_rules):
            if params.gender not in rule['gender']:
                continue
            
            if params.word_class and rule['wordClass'] != params.word_class:
                continue

            if params.application_type and rule['applicationType'] and params.application_type not in rule['applicationType']:
                continue
            
            if params.custom_rule_filter and not params.custom_rule_filter(rule, i, self.declension_rules):
                continue
            
            # Check pattern match
            # rule.pattern.find
            if re.search(rule['pattern']['find'], word, re.IGNORECASE):
                return rule
                
        return None
