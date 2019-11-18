import numpy as np
X = np.random.randint(1,101,25).reshape(5,5)
print "Random 5x5 array is:", "\n", X
print "\n"
xbar = np.mean(X)
xstd = np.std(X)
Z = (X - xbar) / xstd
print "Normalized array is:", "\n", Z
