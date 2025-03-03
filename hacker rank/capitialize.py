def solve(s):
    dict1 = {}
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = 'abcdefghijklmnopqrstuvwxyz'
    j=0
    cap=True
    string1 = ''
    for i in low:
        dict1[i]=up[j]
        j+=1
    for k in s:
        k=str(k)
        if cap and k in dict1:
           
            string1+=dict1[k]
        else:
            string1+=k
        if k == ' ':
            cap = True
            
        else:
            cap = False
    
    return string1

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()