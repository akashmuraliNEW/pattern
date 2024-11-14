# ⦁	Write a Python program to remove duplicates from a list while preserving the order of element

list = ['aka','bro','aka','shit','rocket']
emptylist=[]

tempList=[emptylist for i in list if i not in emptylist ]
 

for num,content in enumerate(list):
    print(num,content)
    if content not in tempList:
        tempList[num]=content
filtered_list = [item for item in tempList if item]

print(filtered_list)