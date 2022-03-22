import nltk
from nltk.corpus import nps_chat
print('liczba postow',len(nps_chat.xml_posts()))
posts=nltk.corpus.nps_chat.xml_posts()
classes=set([post.get('class') for post in posts])
print('liczba klas',len(classes))
print('klasy',classes)

# 1

for c in classes:
    l = 0
    for post in posts:
        if post.get('class') == c:
            l += 1
    print(c, l)

#2


for post in posts:
     if post.get('class') == 'ynQuestion':
         print(post.text)

