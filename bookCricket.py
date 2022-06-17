import random
score = 0
scoreInfo = []
while score < 500:
    scoreValues = random.randint(1,30)
    score = score + scoreValues
    scoreInfo.append(scoreValues)
print('flips',len(scoreInfo),scoreInfo,score)
