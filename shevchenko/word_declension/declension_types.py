from typing import TypedDict, List, Dict, Union, Optional
from enum import Enum
from shevchenko.language import GrammaticalCase, GrammaticalGender, WordClass

class ApplicationType(str, Enum):
    GIVEN_NAME = 'givenName'
    PATRONYMIC_NAME = 'patronymicName'
    FAMILY_NAME = 'familyName'

class InflectionCommandAction(str, Enum):
    REPLACE = 'replace'
    APPEND = 'append'

class InflectionCommand(TypedDict):
    action: InflectionCommandAction
    value: str

# InflectionCommands is a dict where keys are group indexes (as strings because JSON keys are strings)
# and values are InflectionCommand.
InflectionCommands = Dict[str, InflectionCommand]

GrammaticalCases = Dict[GrammaticalCase, List[InflectionCommands]]

class DeclensionPattern(TypedDict):
    find: str
    modify: str

class DeclensionRule(TypedDict):
    description: str
    examples: List[str]
    wordClass: WordClass
    gender: List[GrammaticalGender]
    priority: int
    applicationType: List[ApplicationType]
    pattern: DeclensionPattern
    grammaticalCases: GrammaticalCases
