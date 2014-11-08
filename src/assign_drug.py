
def assign_drug(filename):
    test = filename[-5]
    result = ''
    if (int(test) % 2)==1:
        result= 'tylenol'
    else:
        result= 'placebo'
    return result

import sys
filename = sys.argv[1]
print assign_drug(filename)

assert assign_drug("inflammation_1.dat")=="tylenol"
assert assign_drug("inflammation_4.dat")=="placebo"
