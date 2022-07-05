#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!
n = 100
from functools import reduce
from operator import mul

tall = [n]
while n >= 2:
    n -= 1
    tall.append(n)

number = str(reduce(mul,tall))

sumdig = sum(map(int, number))

print(sumdig)

#Process: not much to it. Remembered the reduce(mul, x) from researching an earlier problem.
#Guessing I would find library-functions for both listing numbers up to number and reversing a list if I went looking,
#didn't need to. As said for summing digits in ep17- return as string- sum as integer- easy.
