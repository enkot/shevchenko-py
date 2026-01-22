from setuptools import setup, find_packages

setup(
    name='shevchenko',
    version='3.1.6',
    description='Python library for declension of Ukrainian anthroponyms',
    author='Oleksandr Tolochko',
    author_email='shevchenko-js@tooleks.com',
    packages=find_packages(),
    package_data={
        'shevchenko.gender_detection': ['artifacts/*.json'],
        'shevchenko.word_declension': ['rules/artifacts/*.json'],
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
