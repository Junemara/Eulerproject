#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open("drafts\ep22nums.txt")
lines = f.readlines()
lines = [line.rstrip() for line in lines]


print(str(sum(map(int, lines))))



#Process: so I spent hours scratching my head about getting the output 22660 over and over,
#when the problem is asking for the first ten digits of the sum. Then figured that 22660 is about
#what I should get actually, considering I'm adding 5000 digits seemingly at random values between 0 and 9.
#Obviously read the problem wrong, and now that I know that each line should be added as a complete number-
#I really regret spending so much time figuring out how to remove the line-breaks.
#Also- spent way too much time trying to get the script to find the input-file, even if it's in the same folder.

#After getting the problem right and figuring out the inputfile there was not much to it.
#Was scrolling through many forums for inspo, but no spesific source for doing the sum and first 10 digits part.
