# pascal Triangle 

row= 9
spaceRow=1
for i in range(row):
    num=1
    # for k in range(spaceRow): 
    for j in range (i+1):
        print(num,end=' ')
        num=num*(i-j)//(j+1)
    print()