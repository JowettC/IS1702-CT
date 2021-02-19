from LinearDSLab import Stack, Queue

def factorial(n):
    s = Stack()
    s.push(n)
    res = 1
    while s.count() > 0:
        m = s.pop()
        res *= m
        if m > 1:
            s.push(m-1)
    return res

# print(0%2)
def mystery(x):
    s = Stack()
    out =""
    s.push(x)
    while s.count()>0:
        x = s.pop()
        out = str(x%2) + out
        x = x //2
        if x > 0:
            s.push(x)
    return out
# print(mystery(6))

def is_palindrome(word):
    q = Queue()
    q2 = Queue()
    for i in range(len(word)):
        q.enqueue(word[i])
        q2.enqueue(word[len(word)-1-i])
    while q.count() > 0:
        if (q.peek() != q2.peek()):
            return False
        q.dequeue()
        q2.dequeue()
    return True

def is_palindrome2(word):
    s = Stack()
    for i in range(len(word)//2):
        s.push(word[i])
        s.push(word[len(word)-(i+1)])
    while s.count()> 0:
        a = s.pop()
        b = s.pop()
        if a != b:
            return False
    return True

        
# print(is_palindrome2("1221"))

def dijkstra(a,b):
    s = Stack()
    s.push(a)
    s.push(b)
    while s.count() > 0:
        num1 = s.pop()
        num2 = s.pop()
        if num1 != num2:
            if num1 > num2:
                s.push(num1-num2)
                s.push(num2)
            else:
                s.push(num1)
                s.push(num2-num1)
        else:
            return num1

print(dijkstra(15,12))
