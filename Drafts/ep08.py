#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
#What is the value of this product?

from functools import reduce
from operator import mul

def findp(filename):
    infile = open(filename)
    nums = []
    for e in infile:
      temp = e.replace("\n","")
      for i in temp:
        i = int(i)
        nums.append(i)
    infile.close()
    idx = 0
    bmax = 0
    bitmax = 0
    for i in nums:
        bit = nums[idx:idx+13]
        prod = reduce(mul, bit)
        idx += 1
        if prod > bmax:
            bmax = prod
            bitmax = bit
    return bmax, bitmax

res = findp("Drafts\ep08input.txt")
print(res)

#Process: Had a really hard time getting the problemdescription, something about the word "adjacent"
#was confusing, + didn't  really get what the problem was asking before doing some other problems and
#getting familiar with how problems are set up with input etc.

#Currently in shock by getting the right answer checking with projecteuler.
#The whole function was written without testing, only looking to ep22 for the inputfile code.
#Was prepared for a list of errors to correct, and to scratch my brain a bit before backtracking
#and fixing everything. But it just works. Straight from my brain. Amazing.
