string = 'CrhH'
lower=''
for i in string:
    if not 'a' <= i <='z':
        lower += chr(ord(i)+32)
    else:
        lower+=i
print(lower)