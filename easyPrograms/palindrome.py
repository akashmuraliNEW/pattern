# check palindrome

string =input('Enter any string: ')
reversed_str = string[::-1]
# print(reversed_str)
if string==reversed_str:
    print(f'{string} is palindrome')
else:
    print('not a palindrome')
