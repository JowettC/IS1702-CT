def max_array(a):
    if len(a) == 1:
        return a[0]
    
    if a[0] > max_array(a[1:]):
        return a[0]
    else:
        return max_array(a[1:])

def isPalindrome(s):
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False
def f(n):
    if n == 0 or n == 1:
        return 1
    return -f(n-1) - f(n-2)

def dijkstra(a,b):
    if a == b:
        return a
    if a > b:
        return dijkstra(a-b,b)
    else:
        return dijkstra(a,b-a)

def euclid(a, b):
    if b == 0:
        return a
    return euclid(b,a%b)

def repeatString(s,n):
    if n == 1:
        return s
    return s + repeatString(s,n-1)
# print(repeatString("apple",3))

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
# print(sum(1))

def reverse(a):
    if len(a)==1:
        return [a[0]]
    return [a[-1]] + reverse(a[:-1])
# print(reverse([1,2,3,4,5,6]))

def power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * power(x, n-1)

def f12_rec(x,n):
    if n == 1:
        return 1/x
    return 1/power(x,n) + f12_rec(x,n-1)

# print(f12_rec(2,4))
import math
def f13_rec(x, y, n):
    if n == 1:
        return n*x
    if n % 2 ==0:
        return n*y + f13_rec(x,y,n-1)
    else:
        return n*x + f13_rec(x,y,n-1)
def factorial(n):
    if n == 1:
        return 1
    return float(n * factorial(n-1))
def f14(x,n):
    if n == 0:
        return 1
    return (x**n)/factorial(n) + f14(x,n-1)
print(f14(2,4))

