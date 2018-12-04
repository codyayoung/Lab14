# Cody Young
# CST 205
# Lab 14
# 2018-12-2

import re

# Problem 1
# Parses the literary classic "Green Eggs and Ham", and outputs certain statistics.
# Prints words in text and their frequency, along with number of unique words.

# Writes output to text file.
# Note: Uses current working directory.
foutput = open('lab14_results_cyoung.txt', 'w')

def word_list():

    # Dictionary used to store word and word counts.
    word_counts = {}
    # Number of unique words
    unique_wordcount = 0

    # Open text file and parse words.
    # If word is not in dictionary, add to dictionary, increment unique word count by 1.
    # Else, increment count by 1.

    with open('eggs.txt', 'r') as file:
        for line in file:
            line = line.lower().split()
            for word in line:
                if word not in word_counts:
                    word_counts.update({word: 1})
                    unique_wordcount += 1
                else:
                    word_counts[word] += 1

    for word in word_counts:
        print('{:<10s}{:<10s}{:>10s}{:>4s}'.format("word:",word.lower(),"count:",str(word_counts[word])))
        foutput.write('{:<10s}{:<10s}{:>10s}{:>4s}'.format("word:",word.lower(),"count:",str(word_counts[word])) + '\n')

    print('\n')
    foutput.write('\n')
    print('{:<10s}{:>3d}'.format("Unique words:", unique_wordcount))
    foutput.write('{:<10s}{:>3d}'.format("Unique words:", unique_wordcount) + '\n')
    most_frequent_word(word_counts)

# Returns the most common word in text, along with its frequency.
def most_frequent_word(input_dict):
    counts = []
    for word_counts in input_dict.values():
        counts.append(word_counts)
    max_freq = max(counts)

    for word in input_dict:
        if input_dict[word] == max_freq:
            print('{:<10s}{:>4s}'.format("Most frequent word:", word.lower()))
            foutput.write('{:<10s}{:>4s}'.format("Most frequent word:", word.lower()) + '\n')
            print('{:<10s}{:>3d}'.format("Frequency:", input_dict[word]))
            foutput.write('{:<10s}{:>3d}'.format("Frequency:", input_dict[word]) + '\n')

# Problem 2
# Parses an HTML file for strings between tags, and returns strings between tags.
def headlines():
    #Create list to hold HTML file as long string.
    input_list = []

    #Open file and parse strings between HTML <h3> and </h3> tags.
    with open('news_source.html','r') as file:
        for line in file:
            input_list.append(line)
    #Create empty string to use for regex parsing.
    #Uses a regex to find all strings between start and end tags (<h3>,</h3>)
    parsed_string = ''.join(input_list)
    headlines = re.findall("<h3>(.*?)</h3>", parsed_string)

    print('\n')
    foutput.write('\n')
    display_headline = "BREAKING NEWS"
    print(display_headline)
    foutput.write(display_headline + '\n')
    print('-' * len(display_headline))
    foutput.write('-' * len(display_headline) + '\n')
    for headline in headlines:
        print(headline)
        foutput.write(headline + '\n')
    return

def main():
    word_list()
    headlines()
    foutput.close()

main()





