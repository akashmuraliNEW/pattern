def upperCase(func_text):
    def wrapper(*arg): 
        result = func_text(*arg)
        return result.upper()

    return wrapper


# def lowerCase(func_text):
#     def wrapper():
#         result = func_text()
#         # print('started')

#         return result.lower()
#     return wrapper

# @lowerCase
# def lower_text():
#     return 'HeY mY namE Is AK'
# @upperCase
# def upper_text():
#     return 'HeY mY namE Is AK'

# print(lower_text())
# print(upper_text())


# decorators with arguments


def decorator(func):
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper
@decorator
@upperCase

def arg_text(name):
    return f'hey my name is {name}'
print(arg_text('akash'))