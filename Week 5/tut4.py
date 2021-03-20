def max_array(a):
    if len(a) == 1:
        return a[0]

    temp = max_array(a[1:])
    if a[0] > temp:
        return a[0]
    else:
        return temp

# print(max_array([1,2,3,4,5,6]))

def isPalindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])
# print(isPalindrome("madam"))
# print(isPalindrome("madman"))

def dijkstra(a,b):
    if a == b:
        return a
    if a > b:
        return dijkstra(a-b,a)
    else:
        return dijkstra(a,b-a)
# print(dijkstra(6,8))

def euclid(a,b):
    if b == 0:
        return a
    return euclid(b,a%b)

# print(euclid(12,8))

def repeatString(s,n):
    if n == 1:
        return s
    return s+repeatString(s,n-1)

# print(repeatString("apple", 3))

def sum(n):
    if n == 1:
        return 1
    return n+ sum(n-1)

# print(sum(1))
# print(sum(2))
# print(sum(3))

def reverse(a):
    if len(a) == 1:
        return a
    return [a[-1]] + reverse(a[:-1])

# print(reverse([1,2,3,4,5]))
def power(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * power(x,n-1)

# print(power(5,2))
def f12(x,n):
    if n == 1:
        return float(1/x)
    return 1/power(x,n) + f12(x,n-1)

# print(f12(2,4))

def f13(x,y,n):
    if n == 1:
        return n*x
    if n % 2 == 1:
        return n*x + f13(x,y,n-1)
    else:
        return n*y + f13(x,y,n-1)
# print(f13(4,3,5))
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def f14_rec(x,n,factorial = None, n2 = None):
    if factorial == None:
        factorial = 1
    if n2== None:
        n2 = 1
    factorial *= n2
    if n2 == n:
        return 1  + (x**n)/factorial
    print(factorial)
    return ((x**n2)/factorial) + f14_rec(x,n,factorial,n2+1)

print(f14_rec(2,4))

# def f14(x, n, n2 = None, factorial = None):
#     if n2 == None:
#         n2 = 1
#     if factorial == None:
#         factorial = 1
#     factorial *= n2
#     if n2 == n:
#         return 1 + (x ** n)/ factorial
#     return x ** n2/ factorial + f14(x, n, n2 + 1, factorial)
    
# print(f14(2, 4))