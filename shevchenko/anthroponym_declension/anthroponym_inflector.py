from typing import TypedDict, Optional
from shevchenko.language import GrammaticalCase, GrammaticalGender
from .given_name_inflector import GivenNameInflector
from .patronymic_name_inflector import PatronymicNameInflector
from .family_name_inflector import FamilyNameInflector
from shevchenko.contracts import DeclensionInput

# This corresponds to Anthroponym type in JS, which is essentially same as DeclensionInput without gender
class Anthroponym(TypedDict, total=False):
    givenName: Optional[str]
    patronymicName: Optional[str]
    familyName: Optional[str]

class AnthroponymInflector:
    def __init__(self, 
                 given_name_inflector: GivenNameInflector,
                 patronymic_name_inflector: PatronymicNameInflector,
                 family_name_inflector: FamilyNameInflector):
        self.given_name_inflector = given_name_inflector
        self.patronymic_name_inflector = patronymic_name_inflector
        self.family_name_inflector = family_name_inflector

    def inflect(self, anthroponym: DeclensionInput, gender: GrammaticalGender, grammatical_case: GrammaticalCase) -> Anthroponym:
        inflected_anthroponym: Anthroponym = {}

        if anthroponym.get('givenName'):
            inflected_anthroponym['givenName'] = self.given_name_inflector.inflect(
                anthroponym['givenName'],
                gender,
                grammatical_case
            )

        if anthroponym.get('patronymicName'):
            inflected_anthroponym['patronymicName'] = self.patronymic_name_inflector.inflect(
                anthroponym['patronymicName'],
                gender,
                grammatical_case
            )

        if anthroponym.get('familyName'):
            inflected_anthroponym['familyName'] = self.family_name_inflector.inflect(
                anthroponym['familyName'],
                gender,
                grammatical_case
            )
            
        return inflected_anthroponym
