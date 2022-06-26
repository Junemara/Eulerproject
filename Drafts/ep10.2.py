#Extension #2. See ep10.py for problem description
#See ep10.1.py for context

import numpy as np
from functools import reduce
from operator import add



MILLION_NUMBERS = list(range(2,10))

filtered = np.cumsum(filter(lambda number: not any(number % n == 0 for n in range(2, number)), MILLION_NUMBERS))
print(filtered)
#a = np.array(filtered)
#print(filtered.cumsum())
#blabla = [number for number in MILLION_NUMBERS if not any(number % n == 0 for n in range(2, number))]

#reduce(mul,blabla)

#print(reduce(add,filtered))

#Process: this also doesn't work with the big range...
#UNTIL I introduced the reduce function, and it still doesn't work...
#Some hours later... I have messed around with lambda, filter and a grotesque mixture of inspiration
#from forums and blogs discussing looping with large lists in python.
