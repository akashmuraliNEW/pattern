def swap_case(s):
    result=''
    lowToUp = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 
            'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
                'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
                'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
                'u': 'U', 'v': 'V', 'y': 'Y', 'w': 'W', 'x': 'X',
                'z': 'Z'} 
    upToLow = {}
    for key in lowToUp:
        upToLow[lowToUp[key]] = key
                    
    for i in s:
        if 'A'<=i<='Z':
            result+=upToLow[i]
        elif 'a'<=i<='z':
            result+=lowToUp[i]
        else:
            result+=i
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)