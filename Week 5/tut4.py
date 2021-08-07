def max_array(a):
    if len(a) == 1:
        return a[0]
    return max(a[0],max_array(a[1:]))
# print(max_array([1,2,3,4,5,6]))
def isPalindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])

# print(isPalindrome("12321"))

def dijkstra(a,b):
    if a == b:
        return a
    if a > b:
        return dijkstra(a-b,a)
    else:
        return dijkstra(a,b-a)
# print(dijkstra(101,25))
def euclid(a,b):
    if b == 0:
        return a
    t = b 
    b = a % b
    return euclid(t,b)
# print(euclid(106,26))

def repeatString(s,n):
    if n == 1:
        return s
    return s + repeatString(s,n-1)
# print(repeatString("apple", 3))
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
# print(sum(1))
def reverse(a):
    if len(a) == 1:
        return a
    return [a[-1]] + reverse(a[:-1])
# print(reverse([1,2,3,4,5,6,7]))

def power(x,n):
    if n ==0:
        return 1
    if n ==1:
        return x
    return x*power(x,n-1)

def f12_rec(x, n):
    if n == 1:
        return 1/x
    return 1/power(x,n) + f12_rec(x,n-1)
# print(f12_rec(2,4))
def f13_rec(x, y, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return n * y + f13_rec(x,y,n-1)
    else:
        return n * x + f13_rec(x,y,n-1)
# print(f13_rec(4,3,5))


def f14(x, n):
    sum = 1
    for j in range(1, n+1):
        sum += (power(x, j) / factorial(j))
    return sum


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def f14_rec(x,n,test = 1,fact =1):
    if n == test:
        # print(fact*(test))
        return (x**test/(fact * (test))) + 1
    # print(x**test)
    return x**test/(fact * (test)) + f14_rec(x,n,test = test + 1, fact = fact * (test))
print(f14_rec(2,4))