s=input("Enter string: ")
result=""
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        result+=s[i-1]+str(count)
        count=1
result+=s[-1]+str(count)
print("Encoded:",result)
print("Original length:",len(s))
print("Encoded length:",len(result))
