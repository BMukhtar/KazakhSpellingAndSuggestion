import collections
import re


def read_stopwords():
    with open('./stopwords.txt', "r") as file:
        stopwords = file.read().split(',')
    # Remove newline characters and make the words lowercase
    stopwords = set([word.strip().lower() for word in stopwords])
    return stopwords


def remove_stopwords_bigrams(bigrams):
    stopwords = read_stopwords()
    filtered_bigrams = []
    for b1, b2 in bigrams:
        if b1.lower() not in stopwords and b2.lower() not in stopwords:
            filtered_bigrams.append((b1, b2))
    return filtered_bigrams


def get_bigram_frequencies(in_file, out_file):
    # Open the input file and read in the contents
    print('Reading in file...')
    with open(in_file, 'r') as infile:
        text = infile.read()

    # Tokenize the words in the text
    print('Tokenizing words...')
    words = re.findall(r'\b[^\W\d_]{2,}\b', text)

    # Normalize the case of the words
    print('Normalizing case...')
    words = [word.lower() for word in words]

    # Generate the bigrams
    print('Generating bigrams...')
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]

    print('Removing stopwords...')
    bigrams = remove_stopwords_bigrams(bigrams)

    # Count the frequency of each bigram
    print('Counting bigram frequency...')
    bigram_counts = collections.Counter(bigrams)

    # Sort the bigrams by frequency
    print('Sorting bigrams by frequency...')
    sorted_bigrams = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)

    # Open the output file and write the bigram frequencies to it
    print('Writing to output file...')
    with open(out_file, 'w') as outfile:
        for bigram, count in sorted_bigrams:
            # ignore less than
            if count < 1000:
                continue
            outfile.write(f'{bigram[0]} {bigram[1]},{count}\n')


if __name__ == '__main__':
    # Test the function
    # Download oscar corpus from here https://www.kaggle.com/code/bmukhtar/starter-kazakh-oscar-corpus-05b5dbd5-d
    get_bigram_frequencies('kk.txt', 'kk_bigrams.txt')
