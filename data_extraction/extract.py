#!/usr/bin/python3

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from stemming.porter2 import stem

import nltk
import sys
import string


# get the necessary data
nltk.download('punkt')
nltk.download('stopwords')

list_of_all_words = list()
filtered_words = list()
clean_words = list()
stem_words_list = list()
stem_words_set = set()
dict_count = dict()
file_name = sys.argv[1]

# add words to the list_of_all_words
def open_file():
    global file_name
    global list_of_all_words
    with open(file_name) as f:
        data = list(f)
    for line in data:
            temp = word_tokenize(line)
            for x in temp:
                list_of_all_words.append(x)


# clean the list_of_all_words from punctuations
def filter_words(list_of_all_words):
    global filtered_words
    filtered_words = list(filter(lambda x: x not in string.punctuation, list_of_all_words))
    # print("length of list before removing punctuation", len(list_of_all_words))
    


#clean the filtered_words from the stop words
def remove_stop_words(filtered_words):
    global clean_words
    #load stopwords
    stop_words = set(stopwords.words("english"))
    clean_words = list(filter(lambda x: x.lower() not in stop_words, filtered_words))


#stem the words

def stem_words(clean_words):
    global stem_words_list
    for i in clean_words:
        stem_words_list.append(stem(i))
    stem_words_list = [x.lower() for x in stem_words_list]
    # print(stem_words_list)

#calculate the frequency table
def frequency_table(stem_words_list):
    global dict_count
    stem_words_set = set(stem_words_list)
    for i in stem_words_set:
        dict_count[i] = stem_words_list.count(i)

    
#print the frequency table in order
def list_print():
    global dict_count
    for key,val in dict_count.items():
        print("The count of ",key, " is ",val)


if __name__ == '__main__':

    open_file()
    filter_words(list_of_all_words)
    remove_stop_words(filtered_words)
    stem_words(clean_words)
    frequency_table(stem_words_list)
    list_print()

