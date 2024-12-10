def upperCase(func_text):
    def wrapper(): 
        result = func_text()
        return result.upper()

    return wrapper


def lowerCase(func_text):
    def wrapper():
        result = func_text()
        # print('started')

        return result.lower()
    return wrapper

@lowerCase
def lower_text():
    return 'HeY mY namE Is AK'
@upperCase
def upper_text():
    return 'HeY mY namE Is AK'

print(lower_text())
print(upper_text())