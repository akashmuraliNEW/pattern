    #         A  
    #        B C  
    #       D E F  
    #      G H I J  
    #     K L M N O  
    #    P Q R S T U  
    #   V W X Y Z [ \  
row =7
col=1
char_num = 65
for i in range(row,0,-1):
    for j in range(i):
        print(' ',end='')
    for k in range(col):
        print(chr(char_num),end=' ')
        char_num+=1
    print()
    
    col+=1