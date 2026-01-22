from shevchenko.word_declension.bootstrap import word_inflector
from .given_name_inflector import GivenNameInflector
from .patronymic_name_inflector import PatronymicNameInflector
from .family_name_inflector import FamilyNameInflector
from .anthroponym_inflector import AnthroponymInflector
from .family_name_classifier.family_name_classifier import FamilyNameClassifier

given_name_inflector = GivenNameInflector(word_inflector)
patronymic_name_inflector = PatronymicNameInflector(word_inflector)
family_name_classifier = FamilyNameClassifier() # Dummy for now
family_name_inflector = FamilyNameInflector(word_inflector, family_name_classifier)

anthroponym_inflector = AnthroponymInflector(
    given_name_inflector,
    patronymic_name_inflector,
    family_name_inflector
)
