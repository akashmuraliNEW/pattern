# A  
# B C  
# D E F  
# G H I J  
# K L M N O  
# P Q R S T U  
# V W X Y Z [ \ 
a = "ABCDEFGHIJKLMNOPQRSTUVWZYZ[\\"
dict={}
j=0
for i in a:
    dict[j]=i
    j+=1

print(dict)
index = 0
for i in range(1,j):
    for k in range(1,i):
        if index==28:
            break
        print(dict[index],end=' ')
        index+=1
    print()
