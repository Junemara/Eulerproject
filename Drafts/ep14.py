#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.
from functools import reduce

MILLION_NUMBERS = list(range(2,1_000_001))
n = 13

def terms(n):
    out = []
    while n > 1:
        if n % 2 == 0:
            n /= 2
            out.append(n)
        elif not n % 2 == 0:
            n = (n * 3) + 1
            out.append(n)
    return len(out) + 1

def numcheck():
    hehe = [8]
    tall = [8]
    for i in MILLION_NUMBERS:
        en = hehe[-1]
        to = terms(i)
        if to > en:
            hehe.append(to)
            tall.append(i)
    return hehe[-1], tall[-1]

allc = numcheck()
print(allc)


#Got some output(524) after running for 46.589 seconds(!). Got the problem instruction wrong yet again,
#but no worries- the solution was... still not right
#Got it half right, 524+1 was indeed the max term among all the numbers', but the problem asked for the terms' number.
#Biggest brainfart was trying to append both number and its calculated terms in the same list,
#when that list was for checking terms against last element. Fixed it by appending number to its own list,
#and HELL YES it worked. Takes 35.06 seconds to run.
#No reasoning behind appending term only if bigger than the last, other than being scared of long lists,
#but luckily it was handy for getting the right output after reinterpreting the problem.
#Pretty sure there are more efficient ways to do this, but today that is none of my business.
