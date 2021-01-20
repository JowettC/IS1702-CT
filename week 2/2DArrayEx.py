def t300(x):   #x is a 2D list
  #TODO
  count = 0
  for a1 in x:
    for num in a1:
      count += 1
  return count

def t301(x):   #x is a 2D list
  #TODO
  sum = 0
  for a1 in x:
    for num in a1:
      sum += num
  return sum

def t302(x):    #x is a 2D list 
  count = 0
  for arr in x:
    for num in arr:
      if num % 2 == 0:
        count += 1
        break
  return count

def t303(x):  #x is a 2D list
  #TODO
  total = 0
  for arr in x:
    total += arr[1]
  return total

def t304(x, n):  #x is a 2D list. n is an integer
  res = []
  for arr in x:
    if arr[1] > n:
      res.append(arr[0])
  return res

def t305(x):   # x is a 2D list
  res= []
  for i in range(len(x)):
    min = 99
    index = i
    for j in range(len(x)):
      if min > x[j][1] and x[j][0] not in res:
        x[j][0]
        min = x[j][1]
        index = j
    res.append(x[index][0])
  return res

  