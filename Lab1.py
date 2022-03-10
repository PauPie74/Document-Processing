import nltk
from nltk.book import *
import pandas as pd

books = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

# 1
def common_context(text):
   return text.common_contexts(["time", "world"])

[common_context(t) for t in books]

# 2

def lexical_diversity(text):
    return len(text)/len(set(text))

rows = ["text1","text2","text3","text4","text5","text6","text7","text8","text9"]
col = ["liczba słów","słowa różne","lexical_diversity"]

df = pd.DataFrame(index=rows, columns=col)
df['liczba słów'] = list([len(t) for t in books])
df['słowa różne'] = list([len(set(t)) for t in books])
df['lexical_diversity'] = list(["{:.2f}".format(lexical_diversity(t)) for t in books])
print(df)

# 3
fourletters = [w for w in set(text1) if len(w) == 4 and w.isalpha()]
print(len(fourletters))

#  4
longwords = [w for w in set(text1) if len(w) > 17 and w.isalpha()]
print(longwords)

# 5
sents = [sent1,sent2,sent3,sent4,sent5,sent6,sent7,sent8]

def dict(sent):
     return (sorted((set(sent))))

sent_dict = []

for sent in sents:
    sent_dict.append(dict(sent))
    print(sent_dict)
    sent_dict=[]

dict_all=[]

for s in sents:
    dict_all.append(dict(s))

print(dict_all)

# 6
def VocabSize(t):
    return (len(sorted((set(t)))))

for b in books:
    print(VocabSize(b))

# 7
freq_text1 = nltk.FreqDist(text1)
print(freq_text1.most_common(10))

# 8
def longest_word(t):
    l = ''
    for w in t:
        if len(w) > len(l):
            l = w
    return l

for t in books:
    print(longest_word(t))
