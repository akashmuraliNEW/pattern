n = int(input())
sizeList=[]
sizeList=input().split()
customers = int(input())
dict1 = {}

while customers>0:
    key,value = map(int,input().split)
    dict1[key]=value
    customers-=1
print(dict1)