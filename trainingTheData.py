import re
import math
import collections

text = "hello from the other side!"
def getWords(word): return re.findall('\w+',word)

all = []
import nltk
from nltk import word_tokenize import re
NounList=[]
def detectNoun(msg): global NounList text=word_tokenize(msg) text=nltk.pos_tag(text) print(text)
for i in text : nouns=re.findall(“[a-zA-Z]+“, str(i))
if nouns[1].find(‘NN’) >= 0 and len(nouns[0]) is not 1: NounList.append(nouns[0])
detectNoun(“i want to reserve in marriot”) print(NounList)

hotels = open('hotels.txt').read()
all = hotels.split(";")

all += getWords(hotels)

N = len(all)
counter = collections.Counter()

for i in all:
    counter[i.lower()] += 1

def alternatives(wrong):
    transpose = []
    alph = "abcdefghijklmnopqrstuvwxyz"
    for letter in alph:
        for i in range(0,len(wrong)):
            transpose.append(wrong[:i] + letter + wrong[i+1:])

    delete = []
    for i in range(0,len(wrong)):
        delete.append(wrong[:i] + wrong[i+1:])

    swaps =[]
    for i in range(0,len(wrong)-1):
        swaps.append(wrong[:i] +wrong[i+1] + wrong[i] + wrong[i+2:])

    insert = []
    for letter in alph:
        for i in range(0,len(wrong)):
            insert.append(wrong[:i] + letter + wrong[i:])

    return insert + swaps + delete + transpose


def known(words):
    return set(w for w in words if w in set(all))


result = alternatives("Ahwahne")

result2 = []
for word in alternatives("Ahwahne"):
    for word2 in alternatives(word):
        result2.append(word2)


result += result2

print(len(set(result)))

candidates = known(set(result))

def prob(word):
    return counter[word]/N

print(max(candidates, key= prob))


