#  Write a program that generates a list of 20 random
# numbers between -50 and 50, and then prints out the sum of all the positive numbers in
# the list using a for loop and an if condition
import random
list1 = []
for i in range(20):
    val = random.randint(-50,50)
    list1 += [val]

sum=0
for i in list1:
    if i > 0:
        sum+=i
print(sum)