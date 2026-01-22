import regex as re
from shevchenko.language import GrammaticalCase
from shevchenko.language.letter_case import copy_letter_case
from shevchenko.word_declension.declension_types import DeclensionRule
from shevchenko.word_declension.command_runner import CommandRunnerFactory

def count_groups(src: str) -> int:
    """
    Counts a number of groups in a given regular expression pattern.
    """
    try:
        pattern = re.compile(f"{src}|")
        # Python's match returns a match object if it matches at the beginning of the string
        # 'exec' in JS is similar to search but here we emulate countGroups from JS.
        # JS: new RegExp(`${src.toString()}|`).exec('')
        # '(|)' groups is 1. '' matches empty string.
        # Python re: re.compile("pattern|")
        # if pattern is (a)(b), (a)(b)| matches empty string?
        # Let's test this logic.
        # JS regex with empty string match creates groups with undefined values if they don't capture.
        # Actually in JS: new RegExp('(a)|').exec('') -> ['', undefined] length 2.
        # The JS logic `matches.length - 1` essentially counts capturing groups in the `src` part.
        
        # In Python `re` module, `pattern.groups` gives the number of capturing groups.
        return re.compile(src).groups
    except re.error:
        return 0


class DeclensionRuleInflector:
    def __init__(self, rule: DeclensionRule):
        self.rule = rule
        self.command_runner_factory = CommandRunnerFactory()

    def inflect(self, word: str, grammatical_case: GrammaticalCase) -> str:
        # accessing rule['grammaticalCases'][grammatical_case] which might be a list of commands
        # JS: const [commands] = this.rule.grammaticalCases[grammaticalCase];
        # It takes the first element of the array.
        cases = self.rule['grammaticalCases'].get(grammatical_case)
        if cases and len(cases) > 0:
            commands = cases[0]
            
            # JS: const searchValue = new RegExp(this.rule.pattern.modify, 'gi');
            # JS replace can take a function.
            
            pattern_str = self.rule['pattern']['modify']
            
            # Note: JS flags 'gi' means global and case-insensitive.
            # Python re.sub handles global by default (count=0).
            
            # We need a replacer function that behaves like the JS one.
            def replacer(match):
                groups = match.groups()
                # JS: (match, ...groups)
                # match is full match. groups correspond to capturing groups.
                
                # countGroups(this.rule.pattern.modify);
                # In JS code they recalculate group count every time, but it's constant for the pattern.
                # However, in JS replace callback, `groups` contains all captured groups.
                
                result_str = ""
                # group_count = count_groups(pattern_str) # Already have groups from match
                
                # Iterate over groups.
                # In JS code: for (let groupIndex = 0; groupIndex < groupCount; groupIndex += 1)
                # JS groups are 0-indexed in the ...groups array, which corresponds to group 1, 2, 3... in regex.
                
                for i, value in enumerate(groups):
                    # value can be None in Python if group didn't match
                    if value is None:
                        value = "" # Or handle as empty string? JS undefined -> likely empty string behavior in concatenation or logic?
                        # In JS `value` would be undefined.
                        # `replacer += value` with undefined results in "undefined" string?
                        # Wait, `groups[groupIndex]` is the captured string.
                        
                    current_value = value if value is not None else ""
                    
                    # command lookup using string key
                    command = commands.get(str(i))
                    if command:
                        current_value = self.command_runner_factory.make(command).exec(current_value)
                    
                    result_str += current_value
                
                return result_str

            inflected_word = re.sub(
                pattern_str, 
                replacer, 
                word, 
                flags=re.IGNORECASE
            )
            
            return copy_letter_case(word, inflected_word)
            
        return word
