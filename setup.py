from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='shevchenko-py',
    version='1.0.5',
    description='Python library for declension of Ukrainian anthroponyms',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Taras Batenkov',
    author_email='taras.batenkov@gmail.com',
    packages=find_packages(),
    package_data={
        'shevchenko.gender_detection': ['artifacts/*.json'],
        'shevchenko.word_declension': ['rules/artifacts/*.json'],
        'shevchenko_ext_military': ['*.json'],
    },
    include_package_data=True,
    install_requires=['regex'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
