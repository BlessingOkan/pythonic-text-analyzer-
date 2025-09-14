# text_analyzer.py
"""
Refactored, Pythonic text analyzer.
Reads a text file, tokenizes words, counts frequencies, finds long words,
and prints a small report. Designed to meet the Module 2 requirements.
"""

from collections import Counter
from typing import List, Tuple


def read_text(file_path: str) -> str:
    """
    Read and return the full contents of a UTF-8 text file.

    Uses a context manager so the file is always closed safely
    (even if an error occurs while reading).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def tokenize(text: str) -> List[str]:
    """
    Lowercase the text and split on whitespace to produce a list of tokens.

    Note: This keeps punctuation attached (simple split). For class scope,
    that's acceptable and matches the starter’s behavior.
    """
    return text.lower().split()


def count_words(tokens: List[str]) -> Counter:
    """
    Count word frequencies using collections.Counter (idiomatic & efficient).
    """
    return Counter(tokens)


def find_long_words(tokens: List[str], min_length: int = 4) -> List[str]:
    """
    Return words whose length is at least min_length.
    Uses a list comprehension (idiomatic Python).
    """
    return [word for word in tokens if len(word) >= min_length]


def top_n(freqs: Counter, n: int = 5) -> List[Tuple[str, int]]:
    """
    Return the top-n most common (word, count) pairs.
    """
    return freqs.most_common(n)


def print_report(tokens: List[str], freqs: Counter, long_words: List[str]) -> None:
    """
    Print the required statistics using f-strings:
    - total word count
    - unique word count
    - top 5 most frequent words
    - count of long words (≥ 4 chars)
    """
    print(f"The total number of words is: {len(tokens)}")
    print(f"The unique words count is: {len(freqs)}")
    print("The most frequent words are:")
    for word, count in top_n(freqs, 5):
        print(f"'{word}': {count}")
    print(f"Long words (≥ 4 characters): {len(long_words)}")


def analyze_text(file_path: str) -> None:
    """
    Orchestrate the analysis pipeline for a given text file.
    """
    text = read_text(file_path)
    tokens = tokenize(text)
    freqs = count_words(tokens)
    long_words = find_long_words(tokens, min_length=4)
    print_report(tokens, freqs, long_words)


if __name__ == "__main__":
    # Ensure 'sample.txt' exists in the same folder as this script.
    analyze_text("sample.txt")