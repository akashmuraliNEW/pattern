
nums = [2,3,4,5]
result = map(lambda x:x*2,nums)
print(list(result))

# <------------------------------------->

firstNames = ('franklin','aurthur','lester')
lastNames = (' HM',' Morgan',' city')
result = map(lambda x,y:x+y,firstNames,lastNames)
print(tuple(result))

# <------------------------------------->

def mapFunc(nums):
    return nums*2
result = map(mapFunc,nums)
print(list(result))

# <------------------------------------->

