#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

pot = 1000

def getdig(pot):
    return str(2**pot)

a = str(getdig(pot))
b = sum(map(int, a))

print(b)

#Process: this problem seemed suspiciously easy, still managed to spend some time messing with
#the str,int, map, getting some variable-type-errors.
#Other than that- write the power of 2, return as string, sum as integers, print- easy. 
