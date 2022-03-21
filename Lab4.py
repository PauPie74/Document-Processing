import nltk
from nltk.corpus import nps_chat as nps
import random

posts = nps.xml_posts()

def extract_features(post):
    features = {}
    for word in nltk.word_tokenize(post.text):
        features['contains({})'.format(word.lower())] = True
    return features

fposts = [(extract_features(p), p.get('class')) for p in posts]
test_size = int(len(fposts) * 0.1)
train_set = fposts[test_size:]
test_set =  fposts[:test_size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)

###############
fposts = [(extract_features(p), p.get('class')) for p in posts]
test_size = int(len(fposts) * 0.1)
train_set = fposts[5000:]
test_set =  fposts[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)
###############
fposts = [(extract_features(p), p.get('class')) for p in posts]
test_size = int(len(fposts) * 0.1)
train_set = fposts[1000:]
test_set =  fposts[:1500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)