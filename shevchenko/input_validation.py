from typing import Any, List, Dict
from shevchenko.language import GrammaticalGender
from shevchenko.contracts import DeclensionInput, GenderDetectionInput
from shevchenko.extension import get_custom_field_names

class InputValidationError(TypeError):
    pass

FIELD_NAMES = ['givenName', 'patronymicName', 'familyName']

def validate_declension_input(input_data: Any) -> None:
    if not isinstance(input_data, dict):
        raise InputValidationError('The input type must be an object (dict).')

    gender = input_data.get('gender')
    
    # Check if gender is valid
    is_gender_valid = False
    for valid_gender in GrammaticalGender:
        if gender == valid_gender.value:
            is_gender_valid = True
            break
            
    if not is_gender_valid:
        valid_values = '", "'.join([g.value for g in GrammaticalGender])
        raise InputValidationError(
            f'The "gender" parameter must be one of the following: "{valid_values}".'
        )

    merged_field_names = FIELD_NAMES + get_custom_field_names()

    has_fields = any(
        field_name in input_data and input_data[field_name] is not None
        for field_name in merged_field_names
    )

    if not has_fields:
        valid_fields = '", "'.join(merged_field_names)
        raise InputValidationError(
            f'At least one of the following parameters must present: "{valid_fields}".'
        )

    for field_name in merged_field_names:
        val = input_data.get(field_name)
        if val is not None and not isinstance(val, str):
             raise InputValidationError(f'The "{field_name}" parameter must be a string.')

def validate_gender_detection_input(input_data: Any) -> None:
    if not isinstance(input_data, dict):
        raise InputValidationError('The input type must be an object (dict).')

    has_fields = any(
        field_name in input_data and input_data[field_name] is not None
        for field_name in FIELD_NAMES
    )

    if not has_fields:
        valid_fields = '", "'.join(FIELD_NAMES)
        raise InputValidationError(
            f'At least one of the following parameters must present: "{valid_fields}".'
        )

    for field_name in FIELD_NAMES:
        val = input_data.get(field_name)
        if val is not None and not isinstance(val, str):
            raise InputValidationError(f'The "{field_name}" parameter must be a string.')
