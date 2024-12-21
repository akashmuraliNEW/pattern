#           1 
#         1 2 
#       1 2 3 
#     1 2 3 4 
#   1 2 3 4 5 
rows = 5
col = 1
spaceRow = rows

for i in range(rows):
    num=1
    for j in range(spaceRow):
        print(' ',end=' ')
    for i in range(col):
        print(num,end=' ')
        num+=1
    print()
    col+=1
    spaceRow-=1

