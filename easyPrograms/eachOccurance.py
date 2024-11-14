# Implement a Python program to count the occurrences of each word in a given text.
string = input('enter the string : ')
temp={}
for i in string:
    if i in temp:
        temp[i]+=1
    else:
        temp[i]=1
print(temp)
