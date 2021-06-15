from setuptools import setup, find_packages

with open("ReadMe.md", 'r') as f:
    long_description = f.read()

setup (
    name = 'Csv_Json_Converter',
    version = '1.1.0',
    author = 'Rerice', 
    author_email = 'maxim.covalev@gmail.com',
    description = 'Аccepts files as input and converts them to csv or json format',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Rerice',
    packages = find_packages(),
    test_suite='tests',
    python_requires='>=3.7'
)