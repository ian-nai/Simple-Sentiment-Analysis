import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import io

class Sentiment(object):
  
    @staticmethod 
    def vader(file):
        analyzer = SentimentIntensityAnalyzer()
        with open(file, 'r') as in_file:
            text = in_file.read()
            sents = nltk.sent_tokenize(text)
            for s in sents:
                snt = analyzer.polarity_scores(s)
                print("{:-<40} {}".format(s, str(snt)))    
           
    @staticmethod
    def naive(file):
  
        
        train = [("It's practical to hope because the hope is for us to survive as a human species.", "pos"),
                 ("Italy's soccer players were unlucky to find themselves in a qualifying group with Spain", "neg"),
                 ("Instead, root for the Knights whose fans are childlike in their glee.", "pos"),
                 ("The overwhelming perception is that the European Union has done very little to alleviate this specifically Italian difficulty.", "neg"),
                 ("We are in for a period of painful social conflict, at the end of which perhaps we may remember why it once seemed wise to relegate certain emotions to the stadium.", "neg"),
                 ("The heartlessness of that is mind-boggling.", "neg"),
                 ("My father was an insatiable learner with intelligence that his baby brother once told me bordered on genius.", "pos"),
                ]
  
        
        dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
  
        
        t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
  
        
        classifier = nltk.NaiveBayesClassifier.train(t)
        
        with open(file, 'r') as in_file:
            text = in_file.read()
            sents = nltk.sent_tokenize(text)
            for s in sents: 
                test_data = s
                test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
  
                print s, (classifier.classify(test_data_features))
                
    @staticmethod 
    def blob(file):
        with io.open(file, 'r', encoding='utf-8') as in_file:
            text = in_file.read()
            sents = nltk.sent_tokenize(text)
            for s in sents:                
                q = TextBlob(s)
                print s, q.sentiment
                
