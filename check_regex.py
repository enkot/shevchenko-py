import json
import re
import os

def check_patterns():
    path = "c:/Users/taras/projects/shevchenko-js/python/shevchenko/word_declension/rules/artifacts/declension-rules.json"
    with open(path, 'r', encoding='utf-8') as f:
        rules = json.load(f)

    for rule in rules:
        pattern = rule['pattern']['find']
        try:
            re.compile(pattern, re.IGNORECASE)
        except re.error as e:
            if "look-behind requires fixed-width pattern" in str(e):
                print(f"Variable look-behind found: {pattern}")
            else:
                print(f"Other regex error in {pattern}: {e}")
        
        pattern_modify = rule['pattern']['modify']
        try:
            re.compile(pattern_modify, re.IGNORECASE)
        except re.error as e:
            if "look-behind requires fixed-width pattern" in str(e):
                print(f"Variable look-behind found in modify: {pattern_modify}")
            else:
                 print(f"Other regex error in modify {pattern_modify}: {e}")

check_patterns()
