# 1
# 3 2
# 6 5 4
# 10 9 8 7
row = 5
current_num=2
k=0
for i in range(1,row+1):
    for j in range(1,i):
   
        current_num-=1
        print(current_num,end=' ')
    k+=i
    current_num=k+1
    print()
    

