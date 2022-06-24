#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#inspo: https://www.cut-the-knot.org/pythagoras/
set = 1000
a = 1
b = 1000
c = 500
for n in range(1,500):
 if a < b:
   a += 1
 if c > b:
    c -= 1
 if b < c:
    b += 1

 if a + b + c == set:
    print(a, b, c)
