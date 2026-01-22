from typing import Any, Optional
import regex as re
from shevchenko.language import GrammaticalCase, GrammaticalGender
from shevchenko.language.linguistics import is_monosyllable
from shevchenko.word_declension.word_inflector import WordInflector, DeclensionParams
from shevchenko.word_declension.declension_types import ApplicationType
from .name_inflector import NameInflector
from .family_name_classifier.family_name_classifier import FamilyNameClassifier

UNCERTAIN_FEMININE_FAMILY_NAME_PATTERN = re.compile(r'[ая]$', re.IGNORECASE)
UNCERTAIN_MASCULINE_FAMILY_NAME_PATTERN = re.compile(r'(ой|ий|ій|их)$', re.IGNORECASE)

class FamilyNameInflector(NameInflector):
    def __init__(self, word_inflector: WordInflector, family_name_classifier: FamilyNameClassifier):
        self.word_inflector = word_inflector
        self.family_name_classifier = family_name_classifier

    def inflect_name_part(self, family_name: str, gender: GrammaticalGender, 
                         grammatical_case: GrammaticalCase, is_last_word: bool) -> str:
        
        if not is_last_word and is_monosyllable(family_name):
            return family_name

        family_name_class = None
        if self._is_uncertain_family_name_class(family_name, gender):
            family_name_class = self.family_name_classifier.classify(family_name)
            
        word_class = family_name_class['wordClass'] if family_name_class else None

        params = DeclensionParams(
            grammatical_case=grammatical_case,
            gender=gender,
            word_class=word_class,
            application_type=ApplicationType.FAMILY_NAME
        )
        return self.word_inflector.inflect(family_name, params)

    def _is_uncertain_family_name_class(self, family_name: str, gender: GrammaticalGender) -> bool:
        return (
            (gender == GrammaticalGender.FEMININE and
             bool(UNCERTAIN_FEMININE_FAMILY_NAME_PATTERN.search(family_name))) or
            (gender == GrammaticalGender.MASCULINE and
             bool(UNCERTAIN_MASCULINE_FAMILY_NAME_PATTERN.search(family_name)))
        )
