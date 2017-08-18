import re
import math
import collections

text = "hello from the other side!"
def getWords(word): return re.findall('\w+',word)

all = []

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


target = input("please enter the word: ")

result = alternatives(target)

for word in set(alternatives(target) ):
    for word2 in set(alternatives(word)):
        result.append(word2)


candidates = known(set(result))

def prob(word):
    return counter[word]/N

if( len(candidates) > 0):
    print(max(candidates, key= prob))
else:
    print("We dont know!")

