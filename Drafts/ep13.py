#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

tdig = open('ep13_input.txt', 'r') 
hehe = list(map(int, tdig.strip()))
print(sum(hehe))





#https://www.pythontutorial.net/python-basics/python-read-text-file/
