#In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#What is the greatest product of four adjacent numbers in the same direction
#(up, down, left, right, or diagonally) in the 20×20 grid?

from functools import reduce
from operator import mul
import numpy as np

def findp(filename):
    f = open(filename)
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    all = []
    for e in lines:
      temp = e.split(" ")
      nums = []
      for i in temp:
          i = int(i)
          nums.append(i)
      all.append(nums)
    f.close()
    return all

res = findp("Drafts\ep11input.txt")
#print(res)

def diag():
    prod = [1,2,1000000]
    bits = [1,2,3,4]
    lst = np.array(res)
    i = 1
    j = 1
    for lin in lst:
        i += 1
        for nx in lin:
            j += 1
            major = np.diagonal(lst, offset=(j - i))
            minor = np.diagonal(np.rot90(lst), offset=-lst.shape[1] + (j + i) + 1)
            idx = 0
            for t in major:
                idx += 1
                if idx <= len(major) - 4:
                 id2 = idx + 4
                 bit = major[idx:id2]
                 ppp = reduce(mul, bit)
                if ppp > prod[-1]:
                 prod.append(ppp)
                 bits.append(bit)
            for t in minor:
                idx += 1
                if idx <= len(minor) - 4: #and len(minor) >= 4:
                 id2 = idx + 4
                 bit = minor[idx:id2]
                 ppp = reduce(mul, bit)
                if ppp > prod[-1]:
                 prod.append(ppp)
                 bits.append(bit)

    return prod, bits
hoho = diag()
print(hoho)

def down():
    prod = [1,2,6000]
    bits = [1,2,3,4]
    lst = np.array(res)
    down = np.transpose(lst)
    for li in down:
        idx = 0
        for x in li:
            idx += 1
            if idx <= 15:
             id2 = idx + 4
             bit = li[idx:id2]
             ppp = reduce(mul, bit)
            if ppp > prod[-1]:
             prod.append(ppp)
             bits.append(bit)
    return prod, bits

#down = down()
#print(down)


#Process: First thought is creating a scewed version of the file- so I can use the same
#function for diagonal adjacent numbers, but I think not.

#For some reason trying to print arrays from the input file took a long time and I forgot
#what my plan was as there's been a couple of days since I've looked at this.

#Tried using index + 1 for each line to get the diagonal rows, too much code and it didn't work.
#Going to look for better methods for getting the diagonals.

#So I'm feeling SLOPPY and going with it. Will sacrifice having a readable draft and mess around
#as I'm kind of getting where I'm at right now.

#Have sucsessfully checked and returned products diagonally, down and sideways, but

#RIGHT ANSWER. After a couple of tries hehe. Had some lack of excitement before letting myself
#write and edit code with no intention of making it pretty, readable or directly reuseable,
#strategically the right choice- as the fun-fuel-tank was running dry.

#As for pure functionality- the first returns for diagonal numbers gave the wrong answer because
#forgot to loop through the diagonal lists, so only some of the diagonal numbers got checked.

#Got the "minor/major" diagonal-structure from "cs96" at https://stackoverflow.com/questions/46135906/pythonic-way-to-get-both-diagonals-passing-through-a-matrix-entry-i-j
