from shevchenko import in_dative, GrammaticalGender
from shevchenko_ext_military import military_extension
from shevchenko.extension import register_extension

register_extension(military_extension)

input_data = {
    'gender': GrammaticalGender.MASCULINE,
    'givenName': 'Тарас',
    'familyName': 'Шевченко',
    'militaryRank': 'Генерал-майор', 
    'militaryAppointment': 'Командир'
}

print(in_dative(input_data))