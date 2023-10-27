import os
import collections

def process_files(input_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        with open(os.path.join(input_dir, filename), 'r') as f:
            words = f.read().split()

        # Calculate frequency distribution
        freq_dist = collections.Counter(words)

        # Write frequency distribution to file
        with open(os.path.join(output_dir, filename + '_freq.txt'), 'w') as f:
            for word, freq in freq_dist.items():
                f.write(f'{word}: {freq}\n')

        # Write sorted words to file
        with open(os.path.join(output_dir, filename + '_sorted.txt'), 'w') as f:
            for word in sorted(words, reverse=True):
                f.write(word + '\n')

# Call the function with your directories
process_files('path_to_your_input_directory', 'path_to_your_output_directory')
