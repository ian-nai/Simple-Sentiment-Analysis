# Simple Sentiment Analysis
Simple scripts for performing sentiment analysis in Python. This repository is intended as a basic introduction to sentiment analysis using Python, and may be used as a launching point for more in-depth sentiment analysis work.

## Getting Started
Install the code's dependencies:
`pip install -r requirements.txt`

## Scrape a Website
Input urls you'd like to scrape in the urls.txt file, then run scrape.py:
`python scrape.py`
The script will save the text it scrapes as .txt files in the project's directory. The script searches for <p> tags by default, but what it looks for can easily be edited in the .py file. Just change the line `paragraphs = soup.find_all('p')` to search for things other than "p".
  
## Perform Sentiment Analysis
Open python, import sentiment.py, and perform sentiment analysis on your texts using Vader or the Naive Bays classifier:
```
>>> from sentiment import Sentiment
>>> Sentiment.vader('your_filename.txt')
>>> [your output]
```
or
```
>>> from sentiment import Sentiment
>>> Sentiment.naive('your_filename.txt')
>>> [your output]
```
  
 
