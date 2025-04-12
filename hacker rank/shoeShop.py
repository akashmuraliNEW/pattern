n = int(input())
sizeList=[]
sizeList=input().split()
customers = int(input())
dict1 = {}

while customers>0:
    user_input = input("Enter key and value: ")  # Example: "6 55"

    key, value = map(int, user_input.split())
    if key in sizeList:
            
        dict1[key]=value
