from fib import *

#def test_case1():
#    if fib(1) != 1 and fib(0) != 1:
#       return False
#    else:
#        return True
def test_case1():
    assert fib(1) == 1 and fib(0) ==1

def test_case2():
    expected=5
    fib_calculated=fib(4)
    assert expected==fib_calculated
