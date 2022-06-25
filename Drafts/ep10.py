#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

num = 100
tot = 0
for i in range(2,num):
  if not any(i % n == 0 for n in range(2, i)): #if num not divideable by any number between 2 and itself.
     tot += i
print(tot)



#Process: quick and easy reuse of ep07, works fine whith the example num = 10,
#BUT - doesnt work with two million, the program kept looping for two minutes before I aborted.
#Went searching online for python looping-advice... and I'm not sure this loop-method
#is the way to go about it.
#Found this blog: https://switowski.com/blog/for-loop-vs-list-comprehension
#"“For loop” is around 50% slower than a list comprehension..."
#Creating a new ep10 file for doing list comprehension
