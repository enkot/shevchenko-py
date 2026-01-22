import regex as re
from typing import Optional
from shevchenko.language import GrammaticalGender

class GrammaticalGenderDetector:
    def __init__(self, masculine_pattern: str, feminine_pattern: str):
        self.masculine_pattern = re.compile(masculine_pattern, re.IGNORECASE)
        self.feminine_pattern = re.compile(feminine_pattern, re.IGNORECASE)

    def detect(self, word: str) -> Optional[GrammaticalGender]:
        masculine_match = self.masculine_pattern.search(word)
        feminine_match = self.feminine_pattern.search(word)

        if masculine_match and not feminine_match:
            return GrammaticalGender.MASCULINE
        elif not masculine_match and feminine_match:
            return GrammaticalGender.FEMININE
        elif masculine_match and feminine_match:
            # logic: longest match wins
            m_len = len(masculine_match.group(0))
            f_len = len(feminine_match.group(0))
            return GrammaticalGender.MASCULINE if m_len > f_len else GrammaticalGender.FEMININE
        
        return None
