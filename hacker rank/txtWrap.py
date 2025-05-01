def wrap(string, max_width):
    dict1={}
    j=0
    str1=''
    index=1
    for i in string:
        if j == max_width:
            dict1[str1]=index
            j=0
            index+=1
            str1=''
        str1+=i
        j+=1
    dict1[str1]=index
    wrapStr=''
    print(dict1)
    for k in dict1:
        wrapStr+=k+'\n'
   
    return wrapStr



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)   

    