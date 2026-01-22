import unittest
from shevchenko import in_vocative, GrammaticalGender, in_genitive

class TestShevchenko(unittest.TestCase):
    def test_taras_schevchenko_vocative(self):
        input_data = {
            'gender': GrammaticalGender.MASCULINE,
            'givenName': 'Тарас',
            'patronymicName': 'Григорович',
            'familyName': 'Шевченко'
        }
        expected = {
            'givenName': 'Тарасе',
            'patronymicName': 'Григоровичу',
            'familyName': 'Шевченку'
        }
        result = in_vocative(input_data)
        self.assertEqual(result, expected)

    def test_taras_schevchenko_genitive(self):
        input_data = {
            'gender': GrammaticalGender.MASCULINE,
            'givenName': 'Тарас',
            'patronymicName': 'Григорович',
            'familyName': 'Шевченко'
        }
        expected = {
            'givenName': 'Тараса',
            'patronymicName': 'Григоровича',
            'familyName': 'Шевченка'
        }
        result = in_genitive(input_data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
