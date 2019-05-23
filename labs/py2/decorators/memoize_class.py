'''
Your job in this lab is to implement a decorator called "memoize".
This decorator is already applied to the functions f, g, and h below.
You just need to write it.

HINT: The wrapper function only needs to accept non-keyword arguments
(i.e., *args). You don't need to accept keyword arguments in this lab.
(That is more complex to do, which is why it's saved for a later
next lab.)

>>> f(2)
CALLING: f 2
4
>>> f(2)
4
>>> f(7)
CALLING: f 7
49
>>> f(7)
49

>>> g(-6, 2)
CALLING: g -6 2
4
>>> g(-6, 2)
4

>>> g(6, 2)
CALLING: g 6 2
-2
>>> g(6, 2)
-2

>>> h(2, 4)
CALLING: h 2 4 42
7
>>> h(2, 4)
7

>>> h(3, 2, 31)
CALLING: h 3 2 31
6
>>> h(3, 2, 31)
6

Let's ensure @Memoize is a class-based decorator, not function-based.
>>> type(Memoize)
<type 'type'>

'''

# Write your code here:




# Do not edit any code below this line!

@Memoize
def f(x):
    print("CALLING: f {}".format(x))
    return x ** 2

@Memoize
def g(x, y):
    print("CALLING: g {} {}".format(x, y))
    return (2 - x) // y

@Memoize
def h(x, y, z=42):
    print("CALLING: h {} {} {}".format(x, y, z))
    return z // (x + y)

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
