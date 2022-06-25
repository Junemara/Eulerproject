#Extension. See ep10.py for problem description
#testing examplecode from https://switowski.com/blog/for-loop-vs-list-comprehension

MILLION_NUMBERS = list(range(2,2))

def transform(number):
    if any(number % n == 0 for n in range(2, number)):
       number = 0
    return number

def fizz_buzz2():
    output = 0
    for number in MILLION_NUMBERS:
        output += transform(number)
    return output

s = fizz_buzz2()
print(s)
#def fizz_buzz2_comprehension():
#    return [transform(number) for number in MILLION_NUMBERS]
#s = fizz_buzz2_comprehension()
#print(s)
