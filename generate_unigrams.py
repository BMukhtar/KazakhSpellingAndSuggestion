import collections
import re


def read_stopwords():
    with open('./stopwords.txt', "r") as file:
        stopwords = file.read().split(',')
    # Remove newline characters and make the words lowercase
    stopwords = set([word.strip().lower() for word in stopwords])
    return stopwords


def remove_stopwords(words):
    # Open the stopword file
    stopwords = read_stopwords()

    # Filter out the stopwords from the words list
    filtered_words = [word for word in words if word.lower() not in stopwords]

    return filtered_words


def get_unigram_frequencies(in_file, out_file):
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

    print('Removing stopwords...')
    words = remove_stopwords(words)

    # Count the frequency of each word
    print('Counting word frequency...')
    word_counts = collections.Counter(words)

    # Sort the words by frequency
    print('Sorting words by frequency...')
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Open the output file and write the word frequencies to it
    print('Writing to output file...')
    with open(out_file, 'w') as outfile:
        for word, count in sorted_words:
            # ignore 1,2
            if count < 500:
                continue
            outfile.write(f'{word},{count}\n')


if __name__ == '__main__':
    # Test the function
    get_unigram_frequencies('kk.txt', 'kk_unigrams.txt')
