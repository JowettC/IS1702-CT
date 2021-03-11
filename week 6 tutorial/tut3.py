from LinearDSLab import Stack, Queue
def factorial(n):
    s = Stack()
    s.push(n)
    total = n
    while s.count() > 0:
        test = s.pop()
        if test == 1:
            return total
        else:
            total *= (test -1)
            s.push(test-1)
    return total

# print(factorial(6))

def mystery(x):
    s = Stack()
    s.push(x)
    out =""
    while x > 0:
        s.push(x//2)
        x = x//2
    while s.count()> 0:
        out += str(s.pop()%2)
    return out[1:]


# print(mystery(7))
def palindrome1(word):
    q1 = Queue()
    q2 = Queue()
    for i in range(0,len(word)):
        q1.enqueue(word[i])
        q2.enqueue(word[len(word)-1-i])
    while q1.count() > 0:
        if q1.dequeue() != q2.dequeue():
            return False
    return True
def palindrome(word):
    s = Stack()
    for letter in word:
        s.push(letter)
    for letter in word:
        if letter != s.pop():
            return False
    return True
# print (palindrome("tteett"))

def dijkstra(a,b):
    s = Stack()
    s.push(a)
    s.push(b)
    while s.count() >0:
        b = s.pop()
        a = s.pop()
        if (a == b):
            return a
        elif a > b:
            s.push(a-b)
            s.push(b)
        else:
            s.push(a)
            s.push(b-a)

s = Stack()
s.push(0)

print (s.count())