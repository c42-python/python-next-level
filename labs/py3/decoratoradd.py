def add(increment):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return increment + func(*args, **kwargs)
        return wrapper
    return decorator

@add(3)
def f(n):
    return n + 2    

# should print 9
print(f(4))    