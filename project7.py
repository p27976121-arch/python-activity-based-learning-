ids=["T1","T2","T3","T1"]
amounts=[100,200,300,100]
suspicious=[]
for i in range(len(ids)):
    if ids.count(ids[i])>1 or amounts[i]>500:
        suspicious.append(ids[i])
print("Suspicious:",suspicious)
