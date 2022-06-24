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

p = 1000/2
