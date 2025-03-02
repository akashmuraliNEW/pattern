input = input("")
input= input.split()
N= int(input[0])
M= int(input[1])
patron=".|."
for i in range (0, int((N)/2)):
    numRepet = (i+1+i)
    print((numRepet*patron).center(M,"-"))
print("WELCOME".center(M,"-"))
for k in range(int((N)/2),0,-1):
    
    print ((numRepet*patron).center(M,"-"))
    