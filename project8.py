key="ABCDA"
answers=["ABCDA","ABCAC","AB__A"]
for a in answers:
    score=0
    for i in range(len(key)):
        if a[i]==key[i]:
            score+=2
        elif a[i]!="_":
            score-=1
    print(a,"Score =",score)
