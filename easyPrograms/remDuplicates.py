# ⦁	Write a Python program to remove duplicates from a list while preserving the order of element

list = ['aka','bro','aka','shit','rocket']
emptyDict={}
j=1
for i in list:
    if i not in emptyDict:
        emptyDict[i]=j
        j+=1
print(emptyDict)
finaList = [k for k in emptyDict if k]
print(finaList)



# tempList=[emptylist for i in list if i not in emptylist ]
# print(tempList)

# for num,content in enumerate(list):
#     print(num,content)
#     if content not in tempList:
#         tempList[num]=content
# filtered_list = [item for item in tempList if item]
# print(tempList)
# print(filtered_list)
