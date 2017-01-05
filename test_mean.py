from mean import *

def test_ints():
    input=[1,2,3,4,5]
    calculated_value=mean(input)
    expected_value =3
    assert calculated_value == expected_value

def test_string():
    input='string'
    try:
        calculated_value=mean(input)
    except TypeError:
        value = 0
    if value == 0:
        return "Type error, test working"
    else:
        return "No type error so yuge error, calculated val = %d" %(calculated_value)


