from abc import ABC, abstractmethod
from shevchenko.language import GrammaticalCase, GrammaticalGender

class NameInflector(ABC):
    def inflect(self, name: str, gender: GrammaticalGender, grammatical_case: GrammaticalCase) -> str:
        inflected_name_parts = []
        name_parts = name.split('-')
        
        for index, part in enumerate(name_parts):
            is_last_word = (index == len(name_parts) - 1)
            inflected_name_part = self.inflect_name_part(part, gender, grammatical_case, is_last_word)
            inflected_name_parts.append(inflected_name_part)

        return '-'.join(inflected_name_parts)

    @abstractmethod
    def inflect_name_part(self, name_part: str, gender: GrammaticalGender, 
                         grammatical_case: GrammaticalCase, is_last_word: bool) -> str:
        pass
