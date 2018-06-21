import numpy as np

# not really necessary as a new function
def strictly_decreasing(np_array):
    ''' are all elements of list strictly decreasing '''
    return np.all(np.diff(np_array) < 0)

# not really necessary as a new function
def shift(np_array, offset):
    ''' Circular shift 2D matrix samples by OFFSET (a [Y,X] 2-tuple),
        such that  RES(POS) = MTX(POS-OFFSET).  '''
    return np.roll(np_array, offset)

def matlab_round(np_array):
    ''' round equivalent to matlab function, which rounds .5 away from zero
        used in matlab_histo so we can unit test against matlab code.
        But numpy.round() would rounds .5 to nearest even number
        e.g. numpy.round(0.5) = 0, matlab_round(0.5) = 1
        e.g. numpy.round(2.5) = 2, matlab_round(2.5) = 3
        '''
    (fracPart, intPart) = np.modf(np_array)
    return intPart + (np.abs(fracPart) >= 0.5) * np.sign(fracPart)
