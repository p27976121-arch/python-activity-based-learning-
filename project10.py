text=input("Enter paragraph: ").lower()
words=text.split()
for w in set(words):
    if words.count(w)>1:
        print(w,"repeated",words.count(w),"times")
