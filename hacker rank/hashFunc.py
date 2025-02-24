# works only in python 2
n = int(raw_input())
integer_list = map(int, raw_input().split())
elements=tuple(integer_list) 
result=hash(elements) 
print(result)

