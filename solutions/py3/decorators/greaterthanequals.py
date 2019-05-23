'''
>>> a = Angle(45)
>>> b = Angle(30)
>>> c = Angle(30)
>>> d = Angle(15)
>>> a == b
False
>>> b == c
True
>>> a > b
True
>>> b > a
False
>>> a >= b
True
>>> b >= a
False
>>> b >= b
True
>>> a >= d
True
'''

# Implement the greaterthanequals decorator here:


def greaterthanequals(klass):
    def ge(self, other):
        return self == other or self > other
    klass.__ge__ = ge
    return klass

# Do not edit any code below this line!

@greaterthanequals
class Angle:
    def __init__(self, value):
        '''
        Value in degrees.
        '''
        self.value = value % 360
    def __add__(self, other):
        return Angle(self.value + other.value)
    def __sub__(self, other):
        return Angle(self.value - other.value)

    def __eq__(self, other):
        return self.value == other.value
    def __gt__(self, other):
        return self.value > other.value


if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
