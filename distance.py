import nltk

w1 = set('mapping')
w2 = set('mappings')
n = nltk.jaccard_distance(w1, w2)
print(n)