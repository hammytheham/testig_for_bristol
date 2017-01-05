from sinc2d import *

def test_x0y0():
    assert sinc2d(0,0) == 1

def testx0():
    for i in range(2,90):
        assert sinc2d(0,i) == np.sin(i)/i

def testy0():
    for i in range(2,90):
        assert sinc2d(i,0) == np.sin(i)/i


