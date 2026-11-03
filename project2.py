present=int(input("Classes attended: "))
total=int(input("Total classes: "))
need=int(input("Required percent: "))
p=100
extra=0
while p<need:
    present+=1
    total+=1
    p=present*100//total
    extra+=1
print("Attend",extra,"more classes")
