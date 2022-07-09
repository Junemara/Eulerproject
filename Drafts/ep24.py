#A permutation is an ordered arrangement of objects.
#For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
#The lexicographic permutations of 0, 1 and 2 are:
#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import numpy as np
import itertools
from itertools import permutations

def perm():

 bla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 a = permutations(bla)
 count = 0
 res = 0
 for i in list(a):
   count += 1
   if count >= 1_000_000:
       i = str(i)
       res = i.replace(", ","")
       break
 return res, count

vis = perm()
print(vis)

#Process: Excited to see a permutations problem, as I was really having a time trying to use permutations
#to solve ep15.

#Trying the lexiographical permutations method from https://www.pythonpool.com/python-permutations/#Find_the_order_in_lexicographical_sorted_order

#So I now got a code working with the example, returning the right permutation for input-number, but
#it feels like it's taking a long time to run allready.

#I was wrong, this WORKS! 1.04 seconds, not bad at all. Got the output as a list,
#considered just writing the numbers to the eulerproject-checker in the right order-
#but after the big variable-type-error and unwanted-charachters-in-string battles from ep22,
#I felt confident in just throwing a replace()-function in the mix and getting a copy-paste friendly output.
