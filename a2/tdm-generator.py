import os
import collections
import sys

def process_files(input_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize lists to store filenames and terms
    filenames = []
    terms = []

    # Initialize a dictionary to store term-document matrix
    td_matrix = collections.defaultdict(dict)

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        with open(os.path.join(input_dir, filename), 'r') as f:
            words = f.read().split()
            # Add words to terms list
            terms.extend(words)
            # Calculate frequency distribution and update term-document matrix
            freq_dist = collections.Counter(words)
            for word, freq in freq_dist.items():
                td_matrix[word][filename] = freq
        # Add filename to filenames list
        filenames.append(filename)

    # Remove duplicates from terms list
    terms = list(set(terms))

    # Write sorted filenames to file
    with open(os.path.join(output_dir, 'sorted_documents.txt'), 'w') as f:
        for filename in sorted(filenames):
            f.write(filename + '\n')

    # Write sorted terms to file
    with open(os.path.join(output_dir, 'sorted_terms.txt'), 'w') as f:
        for term in sorted(terms):
            f.write(term + '\n')

    # Write term-document matrix to file
    with open(os.path.join(output_dir, 'td_matrix.txt'), 'w') as f:
        # Write the dimensions of the matrix on the first line
        f.write(f'{len(td_matrix)} {len(os.listdir(input_dir))}\n')
        # Write the term-document matrix
        for word, doc_freqs in td_matrix.items():
            for filename in os.listdir(input_dir):
                f.write(f'{doc_freqs.get(filename, 0)} ')
            f.write('\n')

if __name__ == "__main__":
    # Check that the user has provided input and output directories
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_dir> <output_dir>")
        sys.exit(1)

    # Call the function with user-provided directories
    process_files(sys.argv[1], sys.argv[2])

