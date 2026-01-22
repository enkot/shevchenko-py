import regex as re

VOWEL_PATTERN = re.compile(r'[аоуеиіяюєї]', re.IGNORECASE)

def count_syllables(word: str) -> int:
    return len(VOWEL_PATTERN.findall(word))

def is_monosyllable(word: str) -> bool:
    return count_syllables(word) == 1
