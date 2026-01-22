from typing import Any
from shevchenko.language import GrammaticalCase, GrammaticalGender
from shevchenko.word_declension.word_inflector import WordInflector, DeclensionParams
from shevchenko.word_declension.declension_types import ApplicationType
from .name_inflector import NameInflector

class PatronymicNameInflector(NameInflector):
    def __init__(self, word_inflector: WordInflector):
        self.word_inflector = word_inflector

    def inflect_name_part(self, patronymic_name: str, gender: GrammaticalGender, 
                         grammatical_case: GrammaticalCase, is_last_word: bool) -> str:
        
        def custom_rule_filter(rule, index, rules):
            return ApplicationType.PATRONYMIC_NAME in rule['applicationType']

        params = DeclensionParams(
            grammatical_case=grammatical_case,
            gender=gender,
            application_type=ApplicationType.PATRONYMIC_NAME,
            custom_rule_filter=custom_rule_filter
        )
        return self.word_inflector.inflect(patronymic_name, params)
