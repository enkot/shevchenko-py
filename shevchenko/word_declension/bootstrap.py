import json
import os
from typing import List
from .word_inflector import WordInflector
from .declension_types import DeclensionRule

def _load_rules() -> List[DeclensionRule]:
    path = os.path.join(os.path.dirname(__file__), 'rules', 'artifacts', 'declension-rules.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

word_inflector = WordInflector(_load_rules())
