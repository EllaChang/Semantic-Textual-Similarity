import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

test_scores = []
train_scores = []
scores = []

test_file = open('test-STS.gs.MSRpar.txt', 'r')
test_scores = test_file.readlines()
        
train_file = open('train-STS.gs.MSRpar.txt', 'r')
train_scores = train_file.readlines()

for s in test_scores:
    s = s[0:5]
    scores.append(float(s))
for s in train_scores:
    s = s[0:5]
    scores.append(float(s))

value = [0.1, 0.3, 0.5, 0.7, 0.9,
         1.1, 1.3, 1.5, 1.7, 1.9,
         2.1, 2.3, 2.5, 2.7, 2.9,
         3.1, 3.3, 3.5, 3.7, 3.9,
         4.1, 4.3, 4.5, 4.7, 4.9]


hist, bins = np.histogram(scores, bins = 25)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.title('Distribution of Golden Standard Scores')
plt.xlabel('Golden Standard Scores')
plt.ylabel('Number of Sentence Pairs')
plt.bar(center, hist, align='center', width=width)
plt.show()

count = plt.hist(scores, 25)
count = count[0].tolist()

table = {}

table['value'] = value
table['count'] = count

df = pd.DataFrame(table, columns=['value', 'count'])
df.to_csv('/Users/ellachang/Desktop/table.csv', index=False, header=True)