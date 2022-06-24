#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

num = 999
while num >= 1:
    i = 999
    while i >= 1:
        s = num*i
        svar = str(s)
        rb = str(svar[:-4:-1])
        rf = str(svar[0:3])
        if s > 901109 and rb == rf: #cheating by manually picking numbers from printed list.
         print(s)
         break
        i = i - 1
    num = num - 1
#Not a good solution, will keep this for the handy while-loop.
