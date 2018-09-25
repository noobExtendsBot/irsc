# IRSC (Information Retrieval and Search Engine)
This repo constains few important scripts which implements the concepts of the Information Retrieval.

## Data Extraction
The data extraction script generally performs five basic functions:
* Tokenize the words. Which is basically extract all the words from the txt file.
* Filter the list_of_all_words from punctuations
* Removal of stop words
* Stem the words
* Generate a frequency table for stemmed words

### Dependencies

* pip3 install porter2stemmer
* pip3 install -U nltk

You are done with the dependencies but you still need to download dataset/models
 for nltk. In your python interpreter do the following:

 		>> import nltk 
 		>> nltk.download('popular')

Keyword `popular` will download the following resources:



	gazetteers 
	genesis    
	gutenberg  
	inaugural  
	movie_reviews 
	names		   
	shakespeare   
	stopwords     
	treebank	   
	twitter_samples 
	omw  			
	wordnet		
	wordnet_ic		
	words			
	maxent_ne_chunker 
	punkt				
	snowball_data		
	averaged_perceptron_tagger 
      
### Usage
	./extract.py filename.txt
