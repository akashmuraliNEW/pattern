# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5 
# 4 5 
# 5
row = 6

for i in range(1,row):
    num = i
    for j in range(i):
        print(num,end=' ')
        num+=1
    print()

