from setuptools import setup, find_packages
import pathlib

# Текущая директория
HERE = pathlib.Path(__file__).parent.resolve()

# Длинное описание из README.md
long_description = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="string-comparator-tools",
    version="0.1.0",
    author="Timur_Hellmut",
    author_email="timurgilmutpr@gmail.com",
    description="Advanced string comparison and spelling correction toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TimurGilmutpr/StringComparator.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.7',
    install_requires=[
        'nltk>=3.5',
    ],
    keywords='spellcheck, ngrams, string comparison, levenshtein, damerau',
    project_urls={
        'Source': 'https://github.com/timur-hellmut/string-comparator-tools',
        'Bug Reports': 'https://github.com/timur-hellmut/string-comparator-tools/issues',
    },
)