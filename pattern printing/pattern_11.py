# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5
row = 5
for i in range(1,row+1):
    for j in range(1,row+1):
       if j>i:
        print(j,end=' ')
       else:
        print(i,end=' ')
    print()