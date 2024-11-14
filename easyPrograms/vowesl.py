# print vowels

string =input('Enter any string: ')
vowels = 'aeiou'
vowels_str = ''
# for i in string:
#     if i in vowels:
#         vowels_str+=i
# print(vowels_str)


# count vowels
# vowel_count=0
# for i in string:
#     if i in vowels:
#         vowel_count+=1
# print(vowel_count)

# remove vowels
for i in string:
    if i not in vowels:
        vowels_str+=i
print(vowels_str)
