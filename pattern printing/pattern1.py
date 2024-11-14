import string 
# row =int(input('enter : '))
# for i in range(row):
#     for j in range (i):
#           print(' ',end='')
   
#     for k in range(row-i):
#             print('*',end=' ')


#    next one 


# user_input = input('enter a string : ')

# count_list = {}
# for i in user_input:
#     if i in count_list:
#         count_list[i] +=1
#     else:
#         count_list[i]=1
# for j in count_list:
#     if count_list[j]==1:
#         print(f'{j} is {count_list[j]} time')
        
# print(count_list)





# user_input = 'texteditor'
# count_list = {}



# for i in user_input:
#     if i in count_list:
#         count_list[i] +=1
#     else:
#         count_list[i]=1


# for j in count_list:
#     if count_list[j] ==1:
#         print(j,'is one time')

# row = 6
# for i in range(row):
#     for j in range(row):
#         if i ==0 :
#             continue
#         if i == row // 2 and j == row // 2:
#             print(' ', end=' ')  # middle space
#         elif i == 1 or i == row - 1 or j == 0 or j == row - 1:
#             print(i, end=' ')  # border
#         else:
#             print(' ', end=' ')  # inner space
#     print()


# 	1)Reverse pyramid pattern
#ABCDEFGHI
# ABCDEFG
#  ABCDE
#   ABC
#    A
# row = 6
# for i in range(row):
#     for j in range(i):
#         print(' ', end='')
#     for k in range(row - i):
#         print(chr(65 + k), end='')
#     print()


# row = 6

#for i in range(row):
#     for j in range(1,i+1):
#         print(j, end='')
#     print()

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

# row = 5
# k=0
# for i in range(row,0,-1):
#     k+=1
#     for j in range(i):
#         print(k,end='')
#     print()


# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5
# row = 5
# for i in range(row,0,-1):
#     for j in range(i):
#         print(row,end='')
#     print()

# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1

# row = 5
# k=0
# for i in range(row,0,-1):
    
#     for j in range(0,i+1):
        
        
#         print(j,end='')
    
#     print()

# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9


# row = 5
# k=-1
# for i in range(1,row+1):
#     k+=2
#     for j in range(i):
#         print(k,end='')
#     print()

# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

# row = 5

# for i in range(row,0,-1):
#     for j in range(i):
#         print(i,end='')
#     print()

# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1

# row = 5
# for i in range(row+1):
#    for j in range(i,0,-1):
#       print(j,end='')
#    print()

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# row = 5
# for i in range(row,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()

# 1
# 3 2
# 6 5 4
# 10 9 8 7
# start = 1
# stop = 2
# current_num=stop

# for row in range(2,6):
#     for col in range(start,stop):
#         current_num-=1
#         print(current_num,end=' ')
#     print('')
#     start = stop
#     stop+=row
#     current_num = stop


#           1 
#         1 2 
#       1 2 3 
#     1 2 3 4 
#   1 2 3 4 5

# row = 6
# for i in range(row):
#     num=1
#     for j in range(row,0,-1):
#         if j >i:
#             print(' ',end=' ')
#         else:
#             print(num,end=' ')
#             num+=1
#     print()


# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1
# row = 7

# for i in range(row):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# 1  
# 2  4  
# 3  6  9  
# 4  8  12  16  
# 5  10  15  20  25  
# 6  12  18  24  30  36  
# 7  14  21  28  35  42  49  
# 8  16  24  32  40  48  56  64  

# row = 8
# for i in range(1,row):
#     for j in range(1,i+1):
#         print(i*j,end=' ')
#     print() 


#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * 

# row = 5
# n=0
# for i in range(row,0,-1):
#     n+=1
#     for j in range(i):
#        print('',end=' ')
#     for k in range(n):
#       print('*',end='')
   
#     print()

#     * * * * * * 
#      * * * * * 
#       * * * * 
#        * * * 
#         * * 
#          * 
# row = 6
# p=6
# for i in range(row):
#     p-=1
#     for j in range(i+1):
#         print('',end=' ')
#     for k in range(p,0,-1):
#         print('*',end=' ')
#     print()

#         *   
#        *  *   
#       *  *  *   
#      *  *  *  *   
#     *  *  *  *  *   
#    *  *  *  *  *  *   
#   *  *  *  *  *  *  * 
# row = 6
# p=0
# for i in range(row,0,-1):
#     p+=1
#     for j in range(i):
#         print('',end=' ')
#     for k in range(p):
#          print('*',end=' ')
#     print()

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 
# row = 6
# p=0
# col=0
# for i in range(row,0,-1):
#     p+=1
#     for j in range(i):
#        print('',end=' ')
#     for k in range(p):
#         print('*',end='')
#     print()
    
# for i in range(row,0,-1):
#     col+=1   
#     for l in range(col+1):
#         print('',end=' ')
#     for m in range(i-1):
#         print('*',end='')
#     print()


# row = 10
# string = 'javapoint'
# for i in range(row):
#     for j in range(i):
#         print(string[j],end='')
#     print()

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
# row = 5
# for i in range(row,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()


#    1 
#    2    1 
#    4    2    1 
#    8    4    2    1 
#   16    8    4    2    1 
#   32   16    8    4    2    1 
#   64   32   16    8    4    2    1 
#  128   64   32   16    8    4    2    1 


# row = 8
# for i in range(row):
#     for j in range (1,i):
         
#         print(j**i,end=' ')
#     print()

# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1

# rows = 7
# triangle = []

# for i in range(rows):
#     templist = []
#     for j in range(i + 1):
#         if j == 0 or j == i:
#             templist.append(1)
#         else:
#             templist.append(triangle[i-1][j-1] + triangle[i-1][j])
#     triangle.append(templist)


# for row in triangle:
#     print(row)

# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5

# row = 5
# for i in range(row):
#     for j in range(1,row+1):
#         if i>=j:
#             print(i,end='')
#         else:
#          print(j,end='')
#     print()

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10
# row =4
# curent_num=1
# stop=2
# for i in range(row):
#     for j in range(1,stop):
#         print(curent_num,end=' ')
#         curent_num+=1
#     print()
#     stop+=1


# 1 
# 2 3 4 
# 5 6 7 8 9

# row = 3
# current_num=1
# stop = 2
# r=6
# for i in range(row):
#     for k in range(r):
#         print(' ',end=' ')
#     for j in range(1,stop):
#         print(current_num,end=' ')
#         current_num+=1
#     print()
#     stop+=2
#     r-=1

# 10 
# 10 8 
# 10 8 6 
# 10 8 6 4 
# 10 8 6 4 2

# row = 5

# stop = 2
# for i  in range(row):
#     current_num = 10
#     for j in range(1,stop):
#         print(current_num,end=' ')
#         current_num-=2
#     print()
#     stop+=1
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1

# row = 5
# k=0
# for i in range(1,row):
#     for j in range(i+k):
#         print('s',end='')
#     print()
#     k+=1

# 1  
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9
row = 5
i=0
val=1

for i in range(1,row+1):
    for j in range(i):
        print(val,end='')
    print()
    val+=2

   