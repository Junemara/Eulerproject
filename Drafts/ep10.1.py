#Extension. See ep10.py for problem description
#testing examplecode from https://switowski.com/blog/for-loop-vs-list-comprehension

MILLION_NUMBERS = list(range(2,2_000_000))

blabla = [number for number in MILLION_NUMBERS if not any(number % n == 0 for n in range(2, number))]

print(sum(blabla))

#this also doesn't work with the big range...
#Want to keep it. Creating a new file for trying things (10.2.py)
