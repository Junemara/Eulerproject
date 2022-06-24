#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#inspo: https://www.cut-the-knot.org/pythagoras/

#Area of a triangle is obviously rp, where r is the inradius and p = (a + b + c)/2 the semiperimeter of the triangle. From the diagram, the hypothenuse c = (a - r) + (b - r), or r = p - c. The area of the triangle then is computed in two ways:
#p(p - c) = ab/2, which is equivalent to
#(a + b + c)(a + b - c) = 2ab, or (a + b)² - c² = 2ab. And finally
#a² + b² - c² = 0.
set = 1000
p = 1000/2
a = 1
b = 2
c = 500
ppc = p * (p - c)
#code works, needs cleanup
num = 499
while num >=249:
    i = 1
    while i <= num:
        ab = num*i
        c = set - num - i
        ppc = p * (p - c)
        if ab/2 == ppc:
         print(ab, c, num, i)
         print(num * i * c)
         #break
        i = i + 1
    num = num - 1

#Process: Can't believe this works.
#Highly experimental, chaothic, optimistic approach.
#Knowing right away I'm not pythagosas' best pal I went searching for all ways
#to write the pythagoras formula- in hopes of getting the given a+b+c(1000) isolated
#enough to squeeze it for more information. I found one at the website commented above.
#This pythagoras proof formula writes the triangles a+b+c for its semiperimeter,
#and the rest was just trying to recreate the formula while looping in a sensible range (a<b<c).
#If there is a simpler obvious solution I wouldn't know, still can't make a judgement,
#and would eighter way consider this approach to be a mathphobic work-around. But a fun one.
#Happy to reuse the code from bad-solution-want-to-keep-it-ep04.
