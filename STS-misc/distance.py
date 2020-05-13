import nltk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

test_edit = []
test_jaccard = []
train_edit = []
train_jaccard = []
four = []
five = []
six = []
j_small = []

test_file = open('test-STS.input.MSRpar.txt', 'r')
test_lines = test_file.readlines()
test_count = 0
for line in test_lines:
    pair = test_lines[test_count].split('\t')
    edit_score = nltk.edit_distance(nltk.word_tokenize(pair[0]), nltk.word_tokenize(pair[1]))
    test_edit.append(edit_score)
    if (edit_score == 4): four.append(pair)
    if (edit_score == 5): five.append(pair)
    if (edit_score == 6): six.append(pair)
    j_score = nltk.jaccard_distance(set(nltk.word_tokenize(pair[0])), set(nltk.word_tokenize(pair[1])))
    test_jaccard.append(j_score)
    if (j_score <= 0.175): j_small.append(pair)
    test_count += 1

train_file = open('train-STS.input.MSRpar.txt', 'r')
train_lines = train_file.readlines()
train_count = 0
for line in train_lines:
    pair = train_lines[train_count].split('\t')
    edit_score = nltk.edit_distance(nltk.word_tokenize(pair[0]), nltk.word_tokenize(pair[1]))
    train_edit.append(edit_score)
    if (edit_score == 4): four.append(pair)
    if (edit_score == 5): five.append(pair)
    if (edit_score == 6): six.append(pair)
    j_score = nltk.jaccard_distance(set(nltk.word_tokenize(pair[0])), set(nltk.word_tokenize(pair[1])))
    train_jaccard.append(j_score)
    if (j_score == 0.0): print(pair)
    if (j_score <= 0.175): j_small.append(pair)
    train_count += 1

es = open('edit_small.txt', 'w')
es.write('Sentences with an edit score of 4:\n\n')
for p in four:
    es.write(p[0] + '\n')
    es.write(p[1] + '\n')
es.write('Sentences with an edit score of 5:\n\n')
for p in five:
    es.write(p[0] + '\n')
    es.write(p[1] + '\n')
es.write('Sentences with an edit score of 6:\n\n')
for p in six:
    es.write(p[0] + '\n')
    es.write(p[1] + '\n')

# Jaccard: 0.175
js = open('jaccard_small.txt', 'w')
js.write('Sentences with a Jaccard score of 0.175 or lower:\n\n')
for p in j_small:
    js.write(p[0] + '\n')
    js.write(p[1] + '\n')

edit_bins = []
edit_value = []
edit_score = test_edit + train_edit
for i in range (4, 30):
    edit_bins.append(i)
a = 4
while (a <= 28):
    edit_value.append(a)
    a += 1
edit_count = plt.hist(edit_score, bins=edit_bins)
edit_count = edit_count[0].tolist()
edit_table = {}
edit_table['edit value'] = edit_value
edit_table['edit count'] = edit_count
df1 = pd.DataFrame(edit_table, columns=['edit value', 'edit count'])
df1.to_csv('/Users/ellachang/Desktop/edit_table.csv', index=False, header=True)

jaccard_bins = []
jaccard_value = []
jaccard_score = test_jaccard + train_jaccard
b = 0.0
while (b <= 1.0):
    jaccard_bins.append(b)
    b += 0.05
c = 0.025
while (c <= 0.975):
    jaccard_value.append(c)
    c += 0.05
jaccard_count = plt.hist(jaccard_score, bins=jaccard_bins)
jaccard_count = jaccard_count[0].tolist()
jaccard_table = {}
jaccard_table['jaccard value'] = jaccard_value
jaccard_table['jaccard count'] = jaccard_count
df2 = pd.DataFrame(jaccard_table, columns=['jaccard value', 'jaccard count'])
df2.to_csv('/Users/ellachang/Desktop/jaccard_table.csv', index=False, header=True)


"""
print(min(test_edit))
print(max(test_edit))

print(min(test_jaccard))
print(max(test_jaccard))

print(min(train_edit))
print(max(train_edit))

print(min(train_jaccard))
print(max(train_jaccard))

testedit = open('test-edit.txt', 'w')
for s in test_edit:
    testedit.write(str(s) + '\n')

testjaccard = open('test-jaccard.txt', 'w')
for s in test_jaccard:
    testjaccard.write(str(s) + '\n')

trainedit = open('train-edit.txt', 'w')
for s in train_edit:
    trainedit.write(str(s) + '\n')

trainjaccard = open('train-jaccard.txt', 'w')
for s in train_jaccard:
    trainjaccard.write(str(s) + '\n')
"""