#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:12:19 2020

@author: ellachang
"""

import nltk
from nltk.translate.bleu_score import sentence_bleu
import pandas as pd

source = [] # which file this pair comes from
pairs = [] # paraphrase pairs
gs = [] # gold standard values
ed = [] # edit distances
jc = [] # Jaccard distances
bl = [] # BLEU metric scores
wc = [] # word counts

# import files
test_file = open('test-STS.input.MSRpar.txt', 'r')
test_lines = test_file.readlines()
test_gs = open('test-STS.gs.MSRpar.txt', 'r')
test_gs_lines = test_gs.readlines()
train_file = open('train-STS.input.MSRpar.txt', 'r')
train_lines = train_file.readlines()
train_gs = open('train-STS.gs.MSRpar.txt', 'r')
train_gs_lines = train_gs.readlines()

i = 0
j = 0

# process test-STS
for line in test_lines:
    source.append("test-STS")
    
    # get pairs
    pair = test_lines[i].split('\t')
    pairs.append(pair)
    
    # get word counts
    pair_wc = []
    pair_wc.append(len(pair[0].split()))
    pair_wc.append(len(pair[1].split()))
    wc.append(pair_wc)
    
    # get edit distances
    edit = nltk.edit_distance(nltk.word_tokenize(pair[0]), nltk.word_tokenize(pair[1]))
    ed.append(edit)
    
    # get Jaccard distances
    jaccard = nltk.jaccard_distance(set(nltk.word_tokenize(pair[0])), set(nltk.word_tokenize(pair[1])))
    jc.append(jaccard)
    
    # get BLUE metric scores
    bleu = sentence_bleu([pair[0]], pair[1], weights = (1, 0, 0, 0))
    bl.append(bleu)

    i += 1

# process train-STS
for line in train_lines:
    source.append("train-STS")
    
    # get pairs
    pair = train_lines[j].split('\t')
    pairs.append(pair)
    
    # get word counts
    pair_wc = []
    pair_wc.append(len(pair[0].split()))
    pair_wc.append(len(pair[1].split()))
    wc.append(pair_wc)
    
    # get edit distances
    edit = nltk.edit_distance(nltk.word_tokenize(pair[0]), nltk.word_tokenize(pair[1]))
    ed.append(edit)
    
    # get Jaccard distances
    jaccard = nltk.jaccard_distance(set(nltk.word_tokenize(pair[0])), set(nltk.word_tokenize(pair[1])))
    jc.append(jaccard)
    
    # get BLUE metric scores
    bleu = sentence_bleu([pair[0]], pair[1], weights = (1, 0, 0, 0))
    bl.append(bleu)
    
    j += 1

# get golden standard values
for line in test_gs_lines:
    gs.append(float(line.rstrip('\n')))
for line in train_gs_lines:
    gs.append(float(line.rstrip('\n')))

table = {
    'Source File': source,
    'Sentence Pair': pairs,
    'Word Counts': wc,
    'Gold Standard Value': gs,
    'Edit Distance': ed,
    'Jaccard Distance': jc,
    'BLEU Metric Score': bl
    }

df = pd.DataFrame(table)
df.to_csv('/Users/ellachang/Desktop/STS.csv', index = True, header = True)