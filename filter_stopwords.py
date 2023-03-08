import string


def remove_stopwords(words, stopword_file):
    # Open the stopword file
    stopwords = read_stopwords(stopword_file)

    # Filter out the stopwords from the words list
    filtered_words = [word for word in words if word[0].lower() not in stopwords]

    return filtered_words


def read_stopwords(stopword_file):
    with open(stopword_file, "r") as file:
        stopwords = file.read().split(',')
    # Remove newline characters and make the words lowercase
    stopwords = set([word.strip().lower() for word in stopwords])
    return stopwords


def read_unigrams_file(file_name):
    with open(file_name, "r") as file:
        unigrams = [(line.split(',')[0], int(line.split(',')[1])) for line in file]
    return unigrams


def filter_and_save_unigrams(unigram_file, stopword_file, output_file):
    unigrams = read_unigrams_file(unigram_file)
    filtered_unigrams = remove_stopwords(unigrams, stopword_file)
    save_filtered_unigrams_to_file(filtered_unigrams, output_file)


def save_filtered_unigrams_to_file(filtered_unigrams, file_name):
    with open(file_name, "w") as file:
        for unigram, count in filtered_unigrams:
            file.write(f"{unigram},{count}\n")


def remove_stopwords_bigrams(bigrams, stopword_file):
    stopwords = read_stopwords(stopword_file)
    filtered_bigrams = []
    for bigram, count in bigrams:
        bigram_words = bigram.split()
        if bigram_words[0].lower() not in stopwords and bigram_words[1].lower() not in stopwords:
            filtered_bigrams.append((bigram, count))
    return filtered_bigrams


def read_bigrams_file(file_name):
    with open(file_name, "r") as file:
        bigrams = [(line.split()[0] + ' ' + line.split()[1], int(line.split()[2])) for line in file]
    return bigrams


def filter_and_save_bigrams(bigram_file, stopword_file, output_file):
    bigrams = read_bigrams_file(bigram_file)
    filtered_bigrams = remove_stopwords_bigrams(bigrams, stopword_file)
    save_filtered_bigrams_to_file(filtered_bigrams, output_file)


def save_filtered_bigrams_to_file(filtered_bigrams, file_name):
    with open(file_name, "w") as file:
        for bigram, count in filtered_bigrams:
            file.write(f"{bigram} {count}\n")


if __name__ == '__main__':
    # Test the function
    filter_and_save_unigrams('kk_unigrams.txt', 'stopwords.txt', 'kk_unigrams_filtered.txt')
    filter_and_save_bigrams('kk_bigrams.txt', 'stopwords.txt', 'kk_bigrams_filtered.txt')
