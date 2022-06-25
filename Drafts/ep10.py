#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

num = 10
tot = 0
i = 1
for i < num:
  i += 1
  if not any(i % n == 0 for n in range(2, i)): #if num not divideable by any number between 2 and itself.
     tot += i
print(tot)

#Process: quick and easy reuse of ep07, works fine whith the example num = 10,
#BUT - doesnt work with two million, the program kept working for two minutes before I aborted.
#Went searching for python memory problem while looping...
