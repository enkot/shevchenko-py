# shevchenko-py

Python library for declension of Ukrainian anthroponyms. Port of [shevchenko.js](https://github.com/tooleks/shevchenko-js).

## Installation

```bash
pip install shevchenko-py
```

## Usage

```python
from shevchenko import in_nominative, in_genitive, in_dative, in_accusative, in_ablative, in_locative, in_vocative, GrammaticalGender

input_data = {
    'gender': GrammaticalGender.MASCULINE,
    'givenName': 'Тарас',
    'patronymicName': 'Григорович',
    'familyName': 'Шевченко'
}

# Nominative: Тарас Григорович Шевченко
print(in_nominative(input_data))

# Genitive: Тараса Григоровича Шевченка
print(in_genitive(input_data))

# Dative: Тарасу Григоровичу Шевченку
print(in_dative(input_data))

# Accusative: Тараса Григоровича Шевченка
print(in_accusative(input_data))

# Ablative: Тарасом Григоровичем Шевченком
print(in_ablative(input_data))

# Locative: Тарасові Григоровичу Шевченку
print(in_locative(input_data))

# Vocative: Тарасе Григоровичу Шевченку
print(in_vocative(input_data))
```

## Using Extensions

You can extend the library to support declension of additional fields. For example, to declin military ranks and appointments using the `shevchenko-ext-military` extension:

```python
from shevchenko import inflect, GrammaticalCase
from shevchenko.extension import register_extension
from shevchenko_ext_military import military_extension

# Register the military extension
register_extension(military_extension)

input_data = {
    'gender': 'masculine',
    'givenName': 'Тарас',
    'familyName': 'Шевченко',
    'militaryRank': 'Генерал-майор',
    'militaryAppointment': 'Командир'
}

# Inflect including the custom fields
result = inflect(input_data, GrammaticalCase.DATIVE)

print(f"{result['militaryRank']} {result['militaryAppointment']} {result['givenName']} {result['familyName']}")
# Output: Генерал-майору Командиру Тарасу Шевченку
```

## Features

- Declension of given names, patronymic names, and family names.
- Auto-detection of grammatical gender (if not provided, though recommended to provide).
- Support for all grammatical cases.
- Uses `regex` library for advanced pattern matching compatibility with JS version.

## License

MIT
