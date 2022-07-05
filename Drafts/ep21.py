#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b,
#then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.
from functools import reduce

#n = 220
tall = list(range(2,10001))

def d(n):
    raw = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) +1) if not n % i))
    return sum(raw) - n

def pairs():
    out = []
    for a in tall:
        s = d(a)
        x = d(s)
        b = d(x)
        if s in tall and s not in out and x == a and a != s:
            out.extend((a, b))
    return out

res = sum(pairs())
print(res)

#Process: reused divisors code from ep14. Had some trouble naming and keeping track of values,
#not in a bad way. Got the wrong answer several times checking with projecteuler, which led to trying
#to fix code that was working fine. Turns out I read 10_000 as 1000.
#Also- noticed that the d() funnction returns the divisors AND the number checked.
#Couldn't get into the details of it enough to fix it as I did not write it from scratch-
#fixed it by subtracting the n in the return.
