
def t200(x):   # x is a list of integers
  sum =0
  for num in x:
    sum += num
  return sum


def t201(x):   # x is a list of values
  str = ""
  for i in range(0, len(x), 2):
    str += x[i] +" "
  print (str[:-1])
  

def t203(x):
  max = x[0]
  for num in x:
    if max < num:
      max = num
  return max

def t204(x, n):
  count = 0
  for num in x:
    if num ==n:
      count += 1 
  return count
def t205(x, n):
  res=[]
  for num in x:
    if num > n:
      res.append(num)
  return res
def t206(x):
  #TODO
  max = x[0]
  min = x[0]
  for num in x:
    if max < num:
      max = num
    if min > num:
      min = num
  return [max,min]

def t207(x1, x2):
  # return sorted(x1 + x2)
  joinedList = x1 + x2
  lastAdded = joinedList[0]
  res=[]
  for i in range(len(joinedList)):
    for num in joinedList:
      if lastAdded > num:
        lastAdded = num
    joinedList.remove(lastAdded)
    res.append(lastAdded)
    if len(joinedList) > 0:
      lastAdded = joinedList[0]
  return res

def t208(x1, x2):
  res = []
  for i in range(len(x1)):
    res.append(x1[i])
    res.append(x2[i])
  return res
def t209(x1, x2):
  res=[]
  for num in x1:
    if num in x2:
      res.append(num)
  return res

    
    
    