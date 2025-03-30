N = int(input())
arr = []
for i in range(N):
    code = input().split()
    command = code[0]
    if command == 'insert':
        arr.insert(int(code[1]),int(code[2]))
        
    elif command == 'print': 
        print(arr)
    elif command == 'remove':
        arr.remove(int(code[1])) 
    elif command == 'append':
        arr.append(int(code[1])) 
    elif command == 'sort': 
        arr.sort() 
        sdasda

    elif command == 'reverse': 
        arr.reverse() 
    
    