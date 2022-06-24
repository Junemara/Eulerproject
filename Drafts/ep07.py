num = 1
c = 1
while c < 100:
 for i in range(1, 1000):
  num = i
  i += 1
  if not any(i % n == 0 for n in range(2, num)):
     c += 1
     print(i)

  #print(c)
