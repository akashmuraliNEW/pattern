#    1 
#    2    1 
#    4    2    1 
#    8    4    2    1 
#   16    8    4    2    1 
#   32   16    8    4    2    1 
#   64   32   16    8    4    2    1 
#  128   64   32   16    8    4    2    1 


row = 8
for i in range(row):
    for j in range (1,i):
         
        print(j**i,end=' ')
    print()
