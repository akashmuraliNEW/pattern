# ⦁	Write a code to print all the prime numbers between 1 to n numbers.
numbers = int(input('enter a number : '))
for number in range(2,numbers):
    if number==2:
         continue
    for i in range(2,int(number/2)+1):
        if number%i==0:
            # print('not prime')
            break
    else:
            print(number)