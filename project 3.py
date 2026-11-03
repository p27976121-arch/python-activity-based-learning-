balance=1000
transactions=[]
for i in range(3):
    t=input("Deposit/Withdraw: ")
    a=int(input("Amount: "))
    if t=="Deposit":
        balance+=a
        transactions.append("Deposit "+str(a))
    elif t=="Withdraw" and a<=balance:
        balance-=a
        transactions.append("Withdraw "+str(a))
    else:
        transactions.append("Rejected")
print("Balance =",balance)
print(transactions)
