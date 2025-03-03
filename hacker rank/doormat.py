# input = input("")
# input= input.split()
# N= int(input[0])
# M= int(input[1])
# patron=".|."
# for i in range (0, int((N)/2)):
#     numRepet = (i+1+i)
#     print((numRepet*patron).center(M,"-"))
# print("WELCOME".center(M,"-"))
# for k in range(int((N)/2),0,-1):
#     numRepet = (k-1+k)
#     print ((numRepet*patron).center(M,"-"))
dict1 = {}
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low = 'abcdefghijklmnopqrstuvwxyz'
j=0
cap=False
string1 = ''
for i in low:
    dict1[i]=up[j]
    j+=1
print(dict1)
dict1 = {}
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low = 'abcdefghijklmnopqrstuvwxyz'
j = 0
cap = True
string1 = ''

# Creating the mapping of lowercase to uppercase letters
for i in low:
    dict1[i] = up[j]
    j += 1

s = "hello world"  # Example input

for k in s:
    if cap and k in dict1:
        string1 += dict1[k]  # Convert first letter of each word to uppercase
    else:
        string1 += k  # Keep the original character

    cap = k == ' '  # Reset capitalization after space

print(string1)