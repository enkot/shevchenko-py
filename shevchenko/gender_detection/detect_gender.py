import json
import os
from typing import Optional, Dict
from shevchenko.language import GrammaticalGender
from shevchenko.contracts import GenderDetectionInput
from .grammatical_gender_detector import GrammaticalGenderDetector

def _load_rules(filename: str) -> Dict[str, str]:
    path = os.path.join(os.path.dirname(__file__), 'artifacts', filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

_given_name_rules = _load_rules('given-name-rules.json')
_patronymic_name_rules = _load_rules('patronymic-name-rules.json')

_given_name_detector = GrammaticalGenderDetector(
    _given_name_rules['masculine'],
    _given_name_rules['feminine']
)

_patronymic_name_detector = GrammaticalGenderDetector(
    _patronymic_name_rules['masculine'],
    _patronymic_name_rules['feminine']
)

def detect_gender(anthroponym: GenderDetectionInput) -> Optional[GrammaticalGender]:
    patronymic = anthroponym.get('patronymicName')
    if patronymic:
        return _patronymic_name_detector.detect(patronymic.lower())
    
    given_name = anthroponym.get('givenName')
    if given_name:
        return _given_name_detector.detect(given_name.lower())
        
    return None
