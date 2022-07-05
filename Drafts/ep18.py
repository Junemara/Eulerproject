#By starting at the top of the triangle below and moving to adjacent numbers on the row below,
#the maximum total from top to bottom is 23.
#3
#7 4
#2 4 6
#8 5 9 3
#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom of the triangle below:
#(see ep18input.txt)
#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However,
#Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

f = open("drafts\ep18input.txt")
lines = f.readlines()
lines = [int(line) for line in lines]

g = []
for line in lines:
    g.append(line[-1])

print(g)
