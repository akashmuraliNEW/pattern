# 10 
# 10 8 
# 10 8 6 
# 10 8 6 4 
# 10 8 6 4 2
row = 6

for i in range(1,row):
    num = 10
    for j in range(i):
        print(num,end=' ')
        num-=2
    print()