from typing import TypeVar, cast
from shevchenko.anthroponym_declension.bootstrap import anthroponym_inflector
from shevchenko.contracts import DeclensionInput, DeclensionOutput, GenderDetectionInput, GenderDetectionOutput
from shevchenko.extension import after_inflect, register_extension, ShevchenkoExtension, ExtensionFactory, AfterInflectHook
from shevchenko.gender_detection import detect_gender as auto_detect_gender
from shevchenko.input_validation import validate_declension_input, validate_gender_detection_input, InputValidationError
from shevchenko.language import GrammaticalCase, GrammaticalGender, WordClass
from shevchenko.word_declension import WordInflector

# Export types and classes
__all__ = [
    'DeclensionInput',
    'DeclensionOutput',
    'GenderDetectionInput',
    'GenderDetectionOutput',
    'InputValidationError',
    'GrammaticalCase',
    'GrammaticalGender',
    'WordClass',
    'WordInflector',
    'register_extension',
    'ShevchenkoExtension',
    'ExtensionFactory',
    'AfterInflectHook',
    'in_grammatical_case',
    'in_nominative',
    'in_genitive',
    'in_dative',
    'in_accusative',
    'in_ablative',
    'in_locative',
    'in_vocative',
    'detect_gender',
    'inflect'
]

T = TypeVar('T', bound=DeclensionInput)

def inflect(input_data: T, grammatical_case: GrammaticalCase) -> DeclensionOutput:
    """
    Inflects an anthroponym in the given grammatical case.
    
    :param input_data: The input anthroponym data.
    :param grammatical_case: The grammatical case to inflect to.
    :return: The inflected anthroponym.
    """
    return in_grammatical_case(grammatical_case, input_data)

def in_grammatical_case(grammatical_case: GrammaticalCase, input_data: T) -> DeclensionOutput:
    """
    Inflects an anthroponym in the given grammatical case.
    
    :param grammatical_case: The grammatical case to inflect to.
    :param input_data: The input anthroponym data.
    :return: The inflected anthroponym.
    :raises InputValidationError: If input validation fails.
    """
    validate_declension_input(input_data)
    
    # We validated input_data has gender in validate_declension_input
    gender = GrammaticalGender(input_data['gender'])
    
    output = anthroponym_inflector.inflect(input_data, gender, grammatical_case)
    after_output = after_inflect(grammatical_case, input_data)
    
    # Merge dictionaries
    result = {**output, **after_output}
    return cast(DeclensionOutput, result)

def in_nominative(input_data: T) -> DeclensionOutput:
    """Inflects an anthroponym in nominative grammatical case."""
    return in_grammatical_case(GrammaticalCase.NOMINATIVE, input_data)

def in_genitive(input_data: T) -> DeclensionOutput:
    """Inflects an anthroponym in genitive grammatical case."""
    return in_grammatical_case(GrammaticalCase.GENITIVE, input_data)

def in_dative(input_data: T) -> DeclensionOutput:
    """Inflects an anthroponym in dative grammatical case."""
    return in_grammatical_case(GrammaticalCase.DATIVE, input_data)

def in_accusative(input_data: T) -> DeclensionOutput:
    """Inflects an anthroponym in accusative grammatical case."""
    return in_grammatical_case(GrammaticalCase.ACCUSATIVE, input_data)

def in_ablative(input_data: T) -> DeclensionOutput:
    """Inflects an anthroponym in ablative grammatical case."""
    return in_grammatical_case(GrammaticalCase.ABLATIVE, input_data)

def in_locative(input_data: T) -> DeclensionOutput:
    """Inflects an anthroponym in locative grammatical case."""
    return in_grammatical_case(GrammaticalCase.LOCATIVE, input_data)

def in_vocative(input_data: T) -> DeclensionOutput:
    """Inflects an anthroponym in vocative grammatical case."""
    return in_grammatical_case(GrammaticalCase.VOCATIVE, input_data)

def detect_gender(input_data: GenderDetectionInput) -> GenderDetectionOutput:
    """
    Detects the grammatical gender of the anthroponym.
    """
    validate_gender_detection_input(input_data)
    return {'gender': auto_detect_gender(input_data)}
