#           1 
#         1 2 1
#       1 2 3 2 1
#     1 2 3 4 3 2 1
#   1 2 3 4 5 4 3 2 1
rows = 5
col=1
col2=0
for i in range(rows,0,-1):
    nums=1
    
    for j in range(i):
        print(' ',end=' ')
    for k in range(col):
        print(nums,end=' ')
        nums+=1
    for l in range(col2,0,-1):
        print(l,end=' ')
    col+=1
    col2+=1
    
    print()
    
