# Simple Sentiment Analysis
Simple scripts for performing sentiment analysis in Python. This repository is intended as a basic introduction to sentiment analysis using Python, and may be used as a launching point for more in-depth sentiment analysis work. The actual sentiment analysis work is done using the [Natural Language Toolkit (NLTK)](http://www.nltk.org/) and [TextBlob](http://textblob.readthedocs.io/en/dev/). Additional documentation on using NLTK for sentiment analysis can be found [here](http://www.nltk.org/howto/sentiment.html).

## Getting Started
Install the code's dependencies:
`pip install -r requirements.txt`

## Scrape a Website
Input urls you'd like to scrape in the urls.txt file, then run scrape.py:
`python scrape.py`
The script will save the text it scrapes as .txt files in the project's directory. The script searches for `<p>` tags by default, but what it looks for can easily be edited in the .py file. Just change the line `paragraphs = soup.find_all('p')` to search for things other than "p".
  
## Perform Sentiment Analysis
Open python, import sentiment.py, and perform sentiment analysis on your texts using [Vader](https://www.nltk.org/_modules/nltk/sentiment/vader.html), NLTK's [Naive Bayes classifier](https://www.nltk.org/_modules/nltk/classify/naivebayes.html), or TextBlob. The training sentences for the Naive Bayes classifier can easily be swapped out for your own. 
```
>>> python
>>> from sentiment import Sentiment
>>> Sentiment.vader('your_filename.txt')
>>> [sentiment analysis of your text]
```
for the Naive Bayes classifier:
```
>>> python
>>> from sentiment import Sentiment
>>> Sentiment.naive('your_filename.txt')
>>> [sentiment analysis of your text]
```
or for TextBlob:
```
>>> python
>>> from sentiment import Sentiment
>>> Sentiment.blob('your_filename.txt')
>>> [sentiment analysis of your text]
```
