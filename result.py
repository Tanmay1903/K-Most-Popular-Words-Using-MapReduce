#!usr/bin/python3
import sys
import heapq

# dictionary to store word count
word_count = {}

# read input from standard input
for line in sys.stdin:
    # split line into word and count
    line = line.strip()
    word, count = line.split('\t', 1)
    # add word count to dictionary
    word_count[word] = int(count)

# use heapq to get the top 100 words based on their count
top_words = heapq.nlargest(100, word_count.items(), key=lambda x: x[1])

# print the top 100 words and their count
for word, count in top_words:
    print(word, count)