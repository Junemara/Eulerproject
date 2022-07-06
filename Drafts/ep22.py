#Using names.txt (right click and 'Save Link/Target As...'),
#a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
#Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN,
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
#So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?

def sorting(filename):
  infile = open(filename)
  words = []
  for line in infile:
    temp = line.split(',')
    for i in temp:
      words.append(i)
  infile.close()
  words.sort()
  outfile = open("Drafts\ep22sorted.txt", "w")
  for i in words:
    outfile.writelines(i)
    outfile.writelines(" ")
  outfile.close()
#sorting("Drafts\ep22input.txt")
w = "AARON"
def wordval(w):
    wval = [ord(i) - 64 for i in w]
    return sum(wval)
#jj = wordval(w)
#print(jj)

def wordsum(filename):
      infile = open(filename)
      words = []
      for e in infile:
        temp = e.split(' ')
        for i in temp:
          i = i.replace('"', '').replace(',','')
          words.append(i)
      infile.close()
      wnums = []
      number = 0
      for x in words:
        number += 1
        bit = str(x)
        lsum = wordval(x)
        res = lsum * number
        wnums.append(res)
      outfile = open("Drafts\ep22nums.txt", "w")
      for o in wnums:
        bit = str(o)
        outfile.writelines(bit)
        outfile.writelines(",")
      outfile.close()
#wordsum("Drafts\ep22sorted.txt")


def sumnums(filename):
      infile = open(filename)
      nums = []
      for e in infile:
        temp = e.split()
        for i in temp:
          nums.append(i)
      infile.close()
      
      return sum(map(int, nums))
ferdig = sumnums("Drafts\ep22nums.txt")

print(ferdig)


#Process: assuming from previous research that the inputfile can be sorted and edited,
#let's try that.
#...a new file for sorted names could be necessary.

#Got this completely copy-pasted code from https://www.codespeedy.com/sorting-contents-of-a-text-file-using-a-python-program/
#for sorting the names. I will proudly add that I figured out to put the ',' in split as the names are separated by commas and not spaces.
#IT WORKS

#For figuring out the alphabetical value, I will avoid any looping through the alphabeth +=1,
#as there should exist some letter-integer correlation in basic libraries. (will eat my shoe if it isn't)

#It is. And the method is ... drumroll... ord().
#Weird thing about the ord()- instructions online tell me to subtract 96 to get the right ASCII value...
#did that, got wrong output, changed it to 64 as that was how much the output was off- and it works?

#while trying to create a second outputfile for wordvalues using the same method- I think it broke my computer
#Now need to really examine each step in the copied code I tried to reuse for numbers, not fun.

#Wow, this was a puzzle and I'm still not done. Created a new file for storing the total word values,
#but before getting there- I got some WEIRD output from for the letter sum. Big negative numbers all over the place.
#Tried about everything before figuring out that the weird values were caused by some punctuation
#from the text file being dragged into the wordval() funnction. Now I have to sum the damn thing.

#Getting typeerrors, and some hellishly long number as output(cant even reach the end of it.)
