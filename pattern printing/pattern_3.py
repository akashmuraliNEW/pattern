#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
rows = 5
col=1
for i in range(rows,0,-1):
    for j in range(i):
        print(' ',end='')
    for k in range(col):
        print('*',end='')
    col+=1
    print()
