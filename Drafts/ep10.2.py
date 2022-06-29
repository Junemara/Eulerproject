#Extension #2. See ep10.py for problem description
#See ep10.1.py for context

n = 2000000
import numpy
def primesfrom3to(n):
    #""" Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return sum(2*numpy.nonzero(sieve)[0][1::]+1)

s = primesfrom3to(n) + 2
print(s)

#Some hours later... I have messed around with lambda, filter and a grotesque mixture of inspiration
#from forums and blogs discussing looping with large lists in python.
#Finally a code that works. Sadly it was copy-pasted and barely edited from
#https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
#Thanks to Robert William Hanks(which is not his real name) on stockoverflow- I can move on from this
#frustrating almost-got-it problem, and hopefully get back to it later.
