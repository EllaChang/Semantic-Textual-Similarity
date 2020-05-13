import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

all_lengths = []
bins = []

test_file = open('test-STS.input.MSRpar.txt', 'r')
test_lines = test_file.readlines()
test_count = 0
test_lengths = []
for line in test_lines:
    pair = test_lines[test_count].split('\t')
    pair_lengths = []
    pair_lengths.append(len(pair[0].split()))
    pair_lengths.append(len(pair[1].split()))
    all_lengths.append(len(pair[0].split()))
    all_lengths.append(len(pair[1].split()))
    test_lengths.append(pair_lengths)
    test_count += 1
test_output = open('test-lengths.txt', 'w')
for lpair in test_lengths:
    test_output.write(str(lpair[0]) + ' ' + str(lpair[1]) + '\n')

train_file = open('train-STS.input.MSRpar.txt', 'r')
train_lines = train_file.readlines()
train_count = 0
train_lengths = []
for line in train_lines:
    pair = train_lines[train_count].split('\t')
    pair_lengths = []
    pair_lengths.append(len(pair[0].split()))
    pair_lengths.append(len(pair[1].split()))
    all_lengths.append(len(pair[0].split()))
    all_lengths.append(len(pair[1].split()))
    train_lengths.append(pair_lengths)
    train_count += 1
train_output = open('train-lengths.txt', 'w')
for lpair in train_lengths:
    train_output.write(str(lpair[0]) + ' ' + str(lpair[1]) + '\n')
    
print(np.median(all_lengths)) # 17.0
print(np.mean(all_lengths)) # 17.8453

lengths = []
for i in range (5, 32):
    bins.append(i)
for i in range (5, 31):
    lengths.append(i)
length_hist = plt.hist(all_lengths, bins=bins)
counts = length_hist[0].tolist()
table = {}
table['word count'] = lengths
table['count'] = counts
df = pd.DataFrame(table, columns=['word count', 'count'])
df.to_csv('/Users/ellachang/Desktop/word_count.csv', index=False, header=True)