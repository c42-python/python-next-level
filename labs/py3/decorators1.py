def printlog(func):
    def wrapper(*args):
        print("CALLING: " + func.__name__)
        return func(*args)
    return wrapper

@printlog
def f(x, y):
    return x+y

@printlog
def print_name(name):
    print(f"My name is {name}")

print(f(3, 4))    
# print_name('Arun')