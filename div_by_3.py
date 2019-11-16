import numpy as np
a = np.arange(1, 101, 1).reshape(10,10)
b = a*a
print b
print "\n"
c = b[b%3==0]
print "The elements that are divisible by 3 are:", "\n", c