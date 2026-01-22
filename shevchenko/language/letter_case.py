def copy_letter_case(template_word: str, target_word: str) -> str:
    """
    Copies a letter case pattern from a template word to a target word.
    Returns a modified target word in the letter case of the template word.
    """
    result_word = []
    
    template_len = len(template_word)
    
    for index, target_letter in enumerate(target_word):
        if index < template_len:
            template_letter = template_word[index]
        elif template_len > 0:
            template_letter = template_word[-1]
        else:
            # Should not happen for normal words, but if template is empty, just keep target as is?
            # JS code: templateWord[templateWord.length - 1] would be undefined if empty.
            # Assuming template is not empty based on logic.
            result_word.append(target_letter)
            continue

        if template_letter.islower():
            result_word.append(target_letter.lower())
        elif template_letter.isupper():
            result_word.append(target_letter.upper())
        else:
            result_word.append(target_letter)
            
    return "".join(result_word)
