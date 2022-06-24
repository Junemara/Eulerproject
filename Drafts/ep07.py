#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
nth = 10001
c = 0
i = 1
while c < nth:
  i += 1
  if not any(i % n == 0 for n in range(2, i)): #if num not divideable by any number between 2 and itself.
     c += 1

print(i)

#Process: first tried googling some formula listing all primenumbers,
#Paul on quora wrote there is none. Figured I'd have to loop for and check
#each natural number for primeness, and count the prime ones all the way to the nth.
#The weird part was setting a sensible diviseability range for any nth,
#and the most satisfying to figure out.
#Also first time finding and using all/any-function,
#definetily not the first time needing it. Bliss.
