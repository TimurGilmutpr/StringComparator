String Comparator Tools
https://img.shields.io/badge/python-3.7%252B-blue
https://img.shields.io/badge/license-MIT-green
https://img.shields.io/pypi/v/string-comparator-tools

Advanced string comparison and spelling correction toolkit for Python. Provides efficient methods for string similarity calculation, n-gram analysis, and context-aware spelling suggestions.

Features
N-gram Similarity: Calculate string similarity using n-gram overlap

Damerau-Levenshtein Distance: Compute optimal string alignment distance with transposition support

Spelling Correction: Suggest corrections for misspelled words based on a dictionary

Customizable Thresholds: Fine-tune sensitivity and performance

Language-Agnostic: Works with any language and character set

Installation
bash
pip install string-comparator-tools
Quick Start
Basic Usage
python
from string_comparator_tools import StringComparator

# Calculate n-gram similarity
similarity = StringComparator.ngram_similarity("apple", "appel", n=2)
print(f"N-gram similarity: {similarity:.2f}")  # Output: 0.88

# Compute Damerau-Levenshtein distance
distance = StringComparator.damerau_levenshtein("kitten", "sitting")
print(f"Edit distance: {distance}")  # Output: 3
Spelling Correction
python
dictionary = ["apple", "banana", "orange", "grape", "kiwi", "lemon"]

# Get spelling suggestions
suggestions = StringComparator.suggest_correction(
    "aple",
    dictionary,
    max_distance=2
)

print("Top suggestions:")
for word, dist in suggestions:
    print(f"- {word} (distance: {dist})")
Output:

text
Top suggestions:
- apple (distance: 1)
- grape (distance: 2)
Advanced Usage
Customizing Search Parameters
python
# Customize n-gram and distance thresholds
suggestions = StringComparator.suggest_correction(
    "orng",
    dictionary,
    max_distance=2,
    ngram_threshold=0.3,  # Lower = more candidates
    n=3                   # Use trigrams instead of bigrams
)
Handling Case Sensitivity
python
# Case-sensitive comparison
StringComparator.ngram_similarity("Apple", "apple", n=2)  # 1.0 (always case-insensitive)

# To preserve case in results:
dictionary = ["NewYork", "Paris", "London"]
suggestions = StringComparator.suggest_correction("newyork", dictionary)
print(suggestions)  # [('NewYork', 0)]
Large Dictionary Optimization
python
# Pre-filter dictionary for better performance
large_dict = [...]  # 10,000+ words

# Step 1: Pre-filter by length
word = "accomodation"
candidates = [w for w in large_dict if abs(len(w) - len(word)) <= 3]

# Step 2: Get suggestions
suggestions = StringComparator.suggest_correction(
    word,
    candidates,
    max_distance=2
)
API Reference
StringComparator.ngram_similarity(s1, s2, n=2)
Calculate n-gram similarity between two strings

Parameters:

s1, s2 (str): Input strings

n (int): Gram size (default=2)

Returns:

float: Similarity score (0.0 to 1.0)

StringComparator.damerau_levenshtein(s1, s2)
Compute Damerau-Levenshtein distance

Parameters:

s1, s2 (str): Input strings

Returns:

int: Edit distance

StringComparator.suggest_correction(word, dictionary, max_distance=2, ngram_threshold=0.4, n=2)
Suggest spelling corrections

Parameters:

word (str): Word to correct

dictionary (list): List of valid words

max_distance (int): Maximum edit distance (default=2)

ngram_threshold (float): Minimum n-gram similarity (default=0.4)

n (int): Gram size (default=2)

Returns:

list: Sorted suggestions as (word, distance) tuples

Performance Tips
Pre-filter Dictionaries: For large dictionaries (>10k words), pre-filter by length before calling suggest_correction

Adjust n-gram Size: For longer words, increase n (3-4) for better accuracy

Tune Thresholds: Lower ngram_threshold increases recall but decreases performance

Cache Results: Memoize frequent lookups in your application

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a new feature branch (git checkout -b feature/your-feature)

Commit your changes (git commit -am 'Add some feature')

Push to the branch (git push origin feature/your-feature)

Create a new Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Support
For issues and feature requests, please open an issue on GitHub.
