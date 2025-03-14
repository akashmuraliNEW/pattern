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
