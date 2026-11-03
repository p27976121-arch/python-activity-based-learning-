units=int(input("Units: "))
if units<=100:
    bill=units*3
elif units<=200:
    bill=300+(units-100)*5
else:
    bill=300+500+(units-200)*8
bill=bill+50
print("Bill =",bill)
