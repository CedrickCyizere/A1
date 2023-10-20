#!/usr/bin/env python3
import sys
from collections import defaultdict

def term_frequency_counter():
    # Create a dictionary to store term frequencies
    term_freq = defaultdict(int)

    # Read line by line from standard input
    for line in sys.stdin:
        # Split the line into terms
        terms = line.split()

        # Update term frequencies
        for term in terms:
            term_freq[term] += 1

    # Sort the dictionary lexicographically
    sorted_terms = sorted(term_freq.items())

    # Print out the terms and their frequencies
    for term, freq in sorted_terms:
        print(f'{term} {freq}')

if __name__ == "__main__":
    term_frequency_counter()
