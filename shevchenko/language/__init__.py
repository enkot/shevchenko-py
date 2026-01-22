from enum import Enum, IntEnum

class GrammaticalCase(str, Enum):
    NOMINATIVE = 'nominative'
    GENITIVE = 'genitive'
    DATIVE = 'dative'
    ACCUSATIVE = 'accusative'
    ABLATIVE = 'ablative'
    LOCATIVE = 'locative'
    VOCATIVE = 'vocative'

class GrammaticalGender(str, Enum):
    MASCULINE = 'masculine'
    FEMININE = 'feminine'

class WordClass(str, Enum):
    NOUN = 'noun'
    ADJECTIVE = 'adjective'

class AlphabetEncoding(IntEnum):
    а = 1
    б = 2
    в = 3
    г = 4
    ґ = 5
    д = 6
    е = 7
    є = 8
    ж = 9
    з = 10
    и = 11
    і = 12
    ї = 13
    й = 14
    к = 15
    л = 16
    м = 17
    н = 18
    о = 19
    п = 20
    р = 21
    с = 22
    т = 23
    у = 24
    ф = 25
    х = 26
    ц = 27
    ч = 28
    ш = 29
    щ = 30
    ь = 31
    ю = 32
    я = 33

ALPHABET_SIZE = len(AlphabetEncoding)
