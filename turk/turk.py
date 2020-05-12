#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:07:18 2020

@author: ellachang
"""

import csv
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import statistics

babel_jaccard = []
babel_edit = []
babel_answer = []
mrpc_answer = []

# read the file
with open('turk.csv') as csvfile:
    turk = csv.reader(csvfile)
    count = 0
    for row in turk:
        if count == 0:
            count = 1
            continue
        babel_jaccard.append(float(row[3]))
        babel_edit.append(int(row[4]))
        babel_answer.append(int(row[10]))
        mrpc_answer.append(int(row[11]))

# hist/mean/median for rows 1-69 of babel_answer
print("mean of rows 1-69 of babel_answer is: ", str(statistics.mean(babel_answer[0:69])))
print("median of rows 1-69 of babel_answer is: ", str(statistics.median(babel_answer[0:69])))
hist1 = plt.hist(babel_answer[0:69], [0, 1, 2, 3, 4, 5, 6])
table1 = {}
table1['babel answer'] = [0, 1, 2, 3, 4, 5]
table1['count'] = hist1[0].tolist()
df1 = pd.DataFrame(table1, columns=['babel answer', 'count'])
df1.to_csv('/Users/ellachang/Desktop/first_babel.csv', index=False, header=True)

# hist/mean/median for rows 70-170 of babel_answer
print("mean of rows 70-170 of babel_answer is: ", str(statistics.mean(babel_answer[69:170])))
print("median of rows 70-170 of babel_answer is: ", str(statistics.median(babel_answer[69:170])))
hist2 = plt.hist(babel_answer[69:170], [0, 1, 2, 3, 4, 5, 6])
table2 = {}
table2['babel answer'] = [0, 1, 2, 3, 4, 5]
table2['count'] = hist2[0].tolist()
df2 = pd.DataFrame(table2, columns=['babel answer', 'count'])
df2.to_csv('/Users/ellachang/Desktop/second_babel.csv', index=False, header=True)

# hist/mean/median for mrpc_answer
print("mean of mrpc_answer is: ", str(statistics.mean(mrpc_answer)))
print("median of mrpc_answer is: ", str(statistics.median(mrpc_answer)))
mrpc_hist = plt.hist(mrpc_answer, [0, 1, 2, 3, 4, 5, 6])
mrpc_table = {}
mrpc_table['mrpc answer'] = [0, 1, 2, 3, 4, 5]
mrpc_table['count'] = mrpc_hist[0].tolist()
mrpc_df = pd.DataFrame(mrpc_table, columns=['mrpc answer', 'count'])
mrpc_df.to_csv('/Users/ellachang/Desktop/mrpc_answer.csv', index=False, header=True)

# correlation between babel_jaccard and babel_answer
print("Correlation between babel_jaccard and babel_answer:")
print(stats.spearmanr(babel_jaccard, babel_answer))

# correlation between babel_edit and babel_answer
print("Correlation between babel_edit and babel_answer:")
print(stats.spearmanr(babel_edit, babel_answer))