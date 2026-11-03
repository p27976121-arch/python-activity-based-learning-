units=int(input("Water units: "))
if units<=50:
    bill=units*2
elif units<=100:
    bill=100+(units-50)*4
else:
    bill=100+200+(units-100)*6
print("Water bill =",bill)
