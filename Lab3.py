import nltk
from nltk.corpus import *

#1
print(wordnet.synsets('dog'))
print(wordnet.synsets('dog', pos='v'))
dog = wordnet.synset('dog.n.01')
print(dog.hypernyms())
print(dog.hyponyms())

cat=wordnet.synset('cat.n.01')
print(dog.path_similarity(cat))

#2
print(gutenberg.fileids())

#3
print(inaugural.fileids())

#4
print(movie_reviews.categories())

#5
print(inaugural.sents('1909-Taft.txt'))

#6
adventure_texts = brown.words(categories='adventure')
print("ocean:", adventure_texts.count("ocean"))
print("mountains:", adventure_texts.count("mountains"))
print("Bungee jump:", adventure_texts.count("Bungee jump"))

#7

freq_in = nltk.FreqDist(inaugural.words())
print(freq_in.most_common(10))

#8
from nltk.book import *

books = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

def percentstopwords(text):
    sw = stopwords.words('english')
    words_ns = []
    for word in text:
        if word not in sw:
            words_ns.append(word)
    percent = len(words_ns)/len(text)
    print(percent)

for b in books:
    percentstopwords(b)
#9
print(sentiwordnet.senti_synset('journalist.n.01'))
print(sentiwordnet.senti_synset('writer.n.01'))
print(sentiwordnet.senti_synset('actor.n.01'))
print(sentiwordnet.senti_synset('singer.n.01'))

#10
def similarity(w1, w2):
    print(w1.path_similarity(w2))

pairs = [['boy','lad'],['journey','voyage'],['coast','hill'],['monk','slave'],['food','fruit'],['journey','car']]

for p in pairs:
    x = p[0]
    y = p[1]
    x = wordnet.synset(x + '.n.01')
    y = wordnet.synset(y + '.n.01')
    print(*p)
    similarity(x, y)

#11
texts = gutenberg.fileids()

for t in texts:
    sum_len_w = 0
    sum_len_s = 0
    sum_rep = 0
    for w in gutenberg.words(t):
        sum_len_w += len(w)
    av_w = sum_len_w / len(gutenberg.words(t))
    for s in gutenberg.sents(t):
         sum_len_s += len(s)
    av_s = sum_len_s / len(gutenberg.sents(t))
    freq_g = nltk.FreqDist(gutenberg.words(t))
    g_freq_list = freq_g.most_common(len(freq_g))
    for f in g_freq_list:
        sum_rep += g_freq_list[0][1]
    av_r = sum_rep / len(g_freq_list)
    print(t, "%.0f" % av_w, "%.0f" % av_s,"%.0f" % av_r)

#12
c_tag = brown.tagged_words('cr09',tagset='universal')
tag_freq = nltk.FreqDist(tag for (word, tag) in c_tag)
print(tag_freq.most_common())

#13
sentences = brown.sents()
tagged_brown = brown.tagged_words(tagset='universal')

n = 0
for w in tagged_brown:
    if w[0].lower() == 'to':
        if tagged_brown[n-1][1] == 'VERB':
            if tagged_brown[n+1][1] == 'VERB':
                print(tagged_brown[n-1][0],w[0],tagged_brown[n+1][0])
    n+= 1
    if n > 1500:
        break