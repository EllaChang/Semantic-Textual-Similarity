import nltk
from scipy import stats

gs = []
jaccard = []
edit = []

test = open('test-STS.input.MSRpar.txt', 'r')
train = open('train-STS.input.MSRpar.txt', 'r')
test_gs = open('test-STS.gs.MSRpar.txt', 'r')
train_gs = open('train-STS.gs.MSRpar.txt', 'r')

def process_input():
    
    test_jaccard = []
    test_edit = []
    train_jaccard = []
    train_edit = []
    
    test_scores = test_gs.readlines()
    train_scores = train_gs.readlines()
    
    global gs
    for score in test_scores:
        gs.append(float(score.rstrip('\n')))
    for score in train_scores:
        gs.append(float(score.rstrip('\n')))
    
    test_lines = test.readlines()
    train_lines = train.readlines()
    
    test_i = 0
    for line in test_lines:
        pair = test_lines[test_i].split('\t')
        j_score = nltk.jaccard_distance(set(nltk.word_tokenize(pair[0])), set(nltk.word_tokenize(pair[1])))
        test_jaccard.append(j_score)
        edit_score = nltk.edit_distance(nltk.word_tokenize(pair[0]), nltk.word_tokenize(pair[1]))
        test_edit.append(edit_score)
        test_i += 1
        
    train_i = 0
    for line in train_lines:
        pair = train_lines[train_i].split('\t')
        j_score = nltk.jaccard_distance(set(nltk.word_tokenize(pair[0])), set(nltk.word_tokenize(pair[1])))
        train_jaccard.append(j_score)
        edit_score = nltk.edit_distance(nltk.word_tokenize(pair[0]), nltk.word_tokenize(pair[1]))
        train_edit.append(edit_score)
        train_i += 1
    
    global jaccard
    jaccard = test_jaccard + train_jaccard
    global edit
    edit = test_edit + train_edit

def jaccard_gs_correlation():
    print("Correlation between Jaccard and GS:")
    print(stats.spearmanr(jaccard, gs))

def edit_gs_correlation():
    print("Correlation between edit distance and GS:")
    print(stats.spearmanr(edit, gs))

process_input()
jaccard_gs_correlation()
print('\n')
edit_gs_correlation()