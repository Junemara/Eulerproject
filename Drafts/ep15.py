#Starting in the top left corner of a 2×2 grid,
#and only being able to move to the right and down,
#there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

import numpy as np
import itertools
a = [0, 0, 1, 1]
bla2 = np.array(list(set(itertools.permutations(a))))
#bla = bla2[np.lexsort(bla2.T[:8:1])] #For sorting matrix if that sounds like fun.
print(len(bla2))
#"Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2"
#For this code, testing show array lenght divided by 2 as n in this formula comes to the same result.
#For eulerproject's problem 15, n is 20- too big for this function to handle.
n = 20
import scipy.special
print(scipy.special.comb(2*n,n)) #This works
