s="Welcome Friends"
dict1 = {}
len = 0
newString=''
list1=[]
# Output : Friends Welcome

for j in s:
    
    if j == ' ':
        list1+=[newString]
        newString = ''
    else:
        newString+=j 
print(list1)
list1+=[newString]
newString = ''
for i in list1:
    len+=1
for k in list1:
    newString+=list1[len-1]
    newString+=' '
    len-=1
print(newString)
with open('file.txt','w') as file:
    file.write(newString)    