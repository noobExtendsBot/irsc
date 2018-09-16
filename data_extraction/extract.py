#!/usr/bin/python3

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from stemming.porter2 import stem

import string

list_of_all_words = list()
filtered_words = list()

# add words to the list

with open("sample.txt") as f:
    data = list(f)
    #print(data)
    for line in data:
        temp = word_tokenize(line)
        for x in temp:
            list_of_all_words.append(x)

#print(list_of_all_words)

# clean the list_of_all_words from punctuations
#filtered_words = filter(lambda x: x not in string.punctuation, list_of_all_words)

filtered_words = list(filter(lambda x: x not in string.punctuation, list_of_all_words))
#print(filtered_words)

#clean the filtered_words from the stop words

stop_words = set(stopwords.words("english"))                                #load stopwords
clean_words = list(filter(lambda x: x not in stop_words, filtered_words))
#print(clean_words)

#stem the words 
#stem_words = list(filter(lambda x: stem(x), clean_words))
print('''
        Final List Of words after removal of stop words and
       stemming''')
#print(stem_words)

stem_words = list()
for i in clean_words:
    stem_words.append(stem(i))

print(stem_words)

