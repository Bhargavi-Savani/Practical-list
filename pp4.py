score=input().split()
score.sort()
fl = sl = score[0]

for i in range(len(score)):
    if(i+1 < len(score)):
        if(score[i+1] > score[i]):
            fl=score[i+1]
            sl=score[i]
print("The runner up is:",sl)