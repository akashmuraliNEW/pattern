# Write a Python program that uses a "while" loop to repeatedly ask the user to input a number until they input a 
# negative number,and then prints out the sum of all the positive numbers they entered.

isPostive = True
result=0

while isPostive:
    n = int(input('enter a number : '))
    if n <0:
        isPostive=False
    else:
        result+=n
        
print(f'final result {result}')

