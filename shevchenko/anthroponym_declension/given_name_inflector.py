from typing import Any
from shevchenko.language import GrammaticalCase, GrammaticalGender
from shevchenko.word_declension.word_inflector import WordInflector, DeclensionParams
from shevchenko.word_declension.declension_types import ApplicationType
from .name_inflector import NameInflector

class GivenNameInflector(NameInflector):
    def __init__(self, word_inflector: WordInflector):
        self.word_inflector = word_inflector

    def inflect_name_part(self, given_name: str, gender: GrammaticalGender, 
                         grammatical_case: GrammaticalCase, is_last_word: bool) -> str:
        params = DeclensionParams(
            grammatical_case=grammatical_case,
            gender=gender,
            application_type=ApplicationType.GIVEN_NAME
        )
        return self.word_inflector.inflect(given_name, params)
