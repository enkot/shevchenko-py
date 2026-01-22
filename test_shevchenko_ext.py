from shevchenko_ext_military import military_extension
from shevchenko.extension import register_extension
from shevchenko import inflect
from shevchenko.language import GrammaticalCase

# Register the extension
register_extension(military_extension)

# Inflect with new fields
# Note: You can pass any dictionary as input, DeclensionInput type hints are for static analysis
result = inflect({
    'gender': 'masculine',
    'givenName': 'Тарас',
    'familyName': 'Шевченко',
    'militaryRank': 'Генерал-майор', 
    'militaryAppointment': 'Командир'
}, GrammaticalCase.DATIVE)

print(result)
# Should output contains keys 'militaryRank': 'Генерал-майору', 'militaryAppointment': 'Командиру' (subject to rules)