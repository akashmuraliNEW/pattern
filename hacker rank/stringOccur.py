def count_substring(string, sub_string):
    subCount = 0
    stringCount = 0
    count=0
   
    for k in sub_string:
        subCount+=1
    print(subCount)
    for j in string:
        stringCount+=1
    print(stringCount)
    length = stringCount-subCount
    print(length)
    index = subCount
    for i in range(length+1):
        print(string[i:index])
        if string[i:index]==sub_string:
            count+=1
        index+=1
        
        
        
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
