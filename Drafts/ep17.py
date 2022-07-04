#If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
#how many letters would be used?
#NOTE: Do not count spaces or hyphens.
#For example, 342 (three hundred and forty-two) contains 23 letters
#and 115 (one hundred and fifteen) contains 20 letters.
#The use of "and" when writing out numbers is in compliance with British usage.
tall = list(range(1,1001))

import inflect

def n2w(n):
 p = inflect.engine()
 s = p.number_to_words(n)
 return s.replace(' ', '').replace('-', '')

res = 0

for i in tall:
 ts = str(n2w(i))
 bit = len(ts)
 res += bit

print(res)

#Process: First started manually listing numbers to twenty with the lettercount, and plan some sort
#of algorithm for lettercount considering digit order and digit count in string, adding the "and" for numbers over 100 not ending with 0 etc.
#Maybe grouping numbers with the same word count- but it all seemed too complicated and it would be very hard to verify that the code is
#behaving right(if I were to do it), and one wrong lettercount would be very hard to find.
#...so after searching for the magic number-to-word function, the results suggests that I was having the right idea.
#Not grouping by lettercount though,that would be cognitive hell.
#Copy-pasted the num2words-clause by "dansalmo" from https://stackoverflow.com/questions/19504350/how-to-convert-numbers-to-words-without-using-num2word-library

#...so getting output using the clause got complicated, and the code supposed to return words from the clause was nasty to write and look at.
#Trying a easier method from the same thread(link), and it works so far with test-numbers.

#Well, it works. Tried using strip() in hopes of it magically removing everything unwanted,
#figured out to use replace(), but not how to make it remove both spaces and hyphens, so wrote two of them.
#Happy to not have attempted the number-to-word code from scratch, this ready made function made it easy
#to check in on the variable values and verify the right range and output throughout.
