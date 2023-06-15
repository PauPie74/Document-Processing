import nltk
from nltk.corpus import wordnet as wn
dog=wn.synset('dog.n.01')
cat=wn.synset('cat.n.01')
animal=wn.synset('animal.n.01')
mammal=wn.synset('mammal.n.01')
bird=wn.synset('bird.n.01')
hen=wn.synset('hen.n.01')
entity=wn.synset('entity.n.01')
#
for w in [animal,mammal,dog,cat,bird,hen]:
    print(w, entity.path_similarity(w))