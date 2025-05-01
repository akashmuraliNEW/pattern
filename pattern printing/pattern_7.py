# 1
# 3 2
# 6 5 4
# 10 9 8 7
row = 6
current_num =2
col = 1
stop = 1
for i in range(row):
     for j in range(i):
          current_num -= 1
          print(current_num,end=' ')
     col+=stop
     stop+=1

     print() 