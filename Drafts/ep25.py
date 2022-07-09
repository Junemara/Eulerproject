#The Fibonacci sequence is defined by the recurrence relation:
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#F1 = 1 F2 = 1 F3 = 2 F4 = 3 F5 = 5 F6 = 8
#F7 = 13 F8 = 21 F9 = 34 F10 = 55 F11 = 89 F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

tall = list(range(1,1_000_00))

def fibo():
    #fibl = [1, 1, 2]
    #findx = 3
    #for i in fibl:
    #    if i in tall:
    #     n = sum(fibl[-2:])
    #     fibl.append(n)
    #     findx += 1
    #     l = len(str(n))
    #    if l == 1000:
    #      break

    #return l, findx

def fibo2():
    f = 1
    a = 1
    b = 2
    index = 2
    for i in tall:
     index += 2
     f += a
     a += b
     b = f + a
     l = len(str(a))
     if l == 1000:
        break
    return index, l

res = fibo2()
print(res)

#Process: back at it with the big numbers. Code working perfectly fine with the smaller ones, but how
#to get to the big big range...
#Right now the code is doing a lot of work for each loop, prime suspect is the len() with the if.
#Considering doing list comprehension, and also have a think about the formula as it's not as unpredictable
#as prime numbers.

#New plan, as the current code is creating a fibonacci-list, I will try to NOT do that.
#Need to step out of the bad habit of returning as many values as possible to keep track.

#It works. Right answer.
#So while checking the output on the don't-create-a-ridiculously-long-list funnction fibo2()-
#I had to add two steps to the index each loop to get it right. Figured worst case would be checking the
#answer twice, I think its close enough.
