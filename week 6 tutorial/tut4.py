def pt (n,k):
    if k == 1:
        return 1
    if k == n+1:
        return 1
    return pt(n-1,k-1) + pt(n-1,k)
# print(pt(4,2))

def max_array(a):
    if len(a) == 1:
        return a[0]
    return max(a[0],max_array(a[1:]))
# print(max_array([1,1987,3,8]))

def isPanlindrome(s):
    if len(s)<2:
        return True
    if s[0] != s[-1]:
        return False
    return isPanlindrome(s[1:-1])
# print (isPanlindrome("123121"))

def dijikstra(a,b):
    if a == b:
        return a
    if a > b:
        return dijikstra(a-b,b)
    elif a < b:
        return dijikstra(a,b-a)
def euclid(a,b):
    if b == 0:
        return a
    return euclid(b,a % b)
# print (euclid(8,12))

def repeatString(s,n):
    if n == 1:
        return s
    return s+repeatString(s,n-1)
# print(repeatString("apple",3))

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
# print(sum(2))

def reverse(a):
    if len(a) == 1:
        return a
    return [a[-1]] + reverse(a[:-1])
# print(reverse([1,2,3,4,5,6]))

def power(x,n):
    if n == 0:
        return 1
    if n ==1:
        return x
    return x * power(x,n-1)

def f12_rec(x,n):
    if n == 1:
        return (1/power(x,1))
    return 1/power(x,n) + f12_rec(x,n-1)
# print (f12_rec(2,4))

def f13(x,y,n):
    if n == 1:
        return x
    if n % 2 == 0:
        return n*y + f13(x,y,n-1)
    else:
        return n*x + f13(x,y,n-1)
# print(f13(4,3,5))

def f14(x,n,n2 = 0, fact = 1):
    if n2 > n:
        return 0
    if n2 == 0:
        return 1 + f14(x,n,n2+1,fact)
    else:
        return x**n2/(fact*n2) +f14(x,n,n2+1,fact * n2)
# print(f14(2,4))
# O(n) complexity