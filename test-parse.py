pairs = []
scores = []
fives = []

file1 = open('test-STS.input.MSRpar.txt', 'r')
lines = file1.readlines()
pair_count = 0
for line in lines:
    pairs.append(lines[pair_count].split('\t'))
    pair_count += 1

file2 = open('test-STS.gs.MSRpar.txt', 'r')
scores = file2.readlines()

for i, score in enumerate(scores):
    if (score == "5.000\n"):
        five = pairs[i]
        five.append(str(i))
        fives.append(five)
        
file3 = open('test-output.txt', 'w')
for five_pair in fives:
    file3.write(five_pair[2] + '\n')
    file3.write(five_pair[0] + '\n')
    file3.write(five_pair[1] + '\n\n')