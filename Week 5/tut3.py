def max_array(a):
    if len(a)== 1:
        return a[0]
    return max(a[0],max_array(a[1:]))

# print(max_array([3,4,2,5,6,2]))

def isPanlindrome(s):
    if len(s) == 1:
        return True
    elif s[0] != s[-1]:
        return False
    return isPanlindrome(s[1:-1])

# print (isPanlindrome("nimao"))
# print (isPanlindrome("mdm"))
# print (isPanlindrome("lol"))

def disjkstra(a,b):
    if a == b:
        return a
    if a > b:
        return disjkstra(a-b,b)
    else:
        return disjkstra(a,b-a)

# print(disjkstra(20,12))

def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(1))

def euclid(a,b):
    if b == 0:
        return a
    return euclid(b, a % b)

def euclid1(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

# print (euclid(5,10))
# print (euclid1(5,10))

def repeatString(s,n):
    if n == 1:
        return s
    return s + repeatString(s,n-1)
# print(repeatString('apple',3))

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

# print(sum(3))

def reverse(a):
    if len(a) == 1:
        return a
    return [a[-1]] + reverse(a[:-1])

print(reverse([1,2,3,4]))

def power(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * power(x,n-1)

def f12_rec(x,n):
    print (n)
    if n == 1:
        return 1/power(x,n)
    return (1/power(x,n)) + f12_rec(x,n-1)

# print(f12_rec(2,4))

def f13_rec(x,y,n):
    if n == 1:
        return x
    if n%2 == 1:
        return n*x + f13_rec(x,y,n-1)
    else:
        return n*y +  f13_rec(x,y,n-1)
print(f13_rec(4,3,5))

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
def power(x,n):
    if n == 1 :
        return x
    return x * power(x,n-1)

def f14(x,n):
    if n == 0:
        return 1
    return power(x,n)/factorial(n) + f14(x,n-1)
print(f14(2,4))