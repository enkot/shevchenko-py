from typing import TypedDict, Optional
from shevchenko.language import GrammaticalGender

class DeclensionInput(TypedDict, total=False):
    gender: GrammaticalGender
    givenName: Optional[str]
    patronymicName: Optional[str]
    familyName: Optional[str]

class DeclensionOutput(TypedDict, total=False):
    givenName: Optional[str]
    patronymicName: Optional[str]
    familyName: Optional[str]

class GenderDetectionInput(TypedDict, total=False):
    givenName: Optional[str]
    patronymicName: Optional[str]
    familyName: Optional[str]

class GenderDetectionOutput(TypedDict):
    gender: Optional[GrammaticalGender]
