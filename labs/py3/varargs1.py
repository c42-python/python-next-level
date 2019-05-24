def print_args(*args):
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{} -> {}".format(key, value))

def print_all(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print("{} -> {}".format(key, value))

print_args()    
print_kwargs()
print_all()