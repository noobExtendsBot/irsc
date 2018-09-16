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

filtered_words = list(filter(lambda x: x not in string.punctuation, list_of_all_words))
#print(filtered_words)
#print("length of list before removal of stop words", len(filtered_words))


#clean the filtered_words from the stop words

stop_words = set(stopwords.words("english"))                                #load stopwords
#print(stop_words)
clean_words = list(filter(lambda x: x.lower() not in stop_words, filtered_words))

#print("length of list after removal of stop words", len(clean_words))
#print(clean_words)

#stem the words 

#stem_words = list(filter(lambda x: stem(x), clean_words))
print('''
        Final List Of words after removal of stop words and
       stemming''')

stem_words = list()
for i in clean_words:
    stem_words.append(stem(i))

stem_words = [x.lower() for x in stem_words]
print(stem_words)

#calculate the frequency table

stem_words_set = set(stem_words)

dict_count = dict()

for i in stem_words_set:
	dict_count[i] = stem_words.count(i)
    
#print the frequency table in order

for key,val in dict_count.items():
    print("The count of ",key, " is ",val)

