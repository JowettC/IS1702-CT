def Factorial(n):
    if n <= 1:
        return n
    else:
        return n * Factorial(n-1)
def sumDigits(arr):
    if len(arr) < 2:
        return arr[0]
    else:
        return arr[0] + sumDigits(arr[1:])
def FibonacciL(n):
    if n <= 1:
        return n
    else:
        return (FibonacciL(n-1) + FibonacciL(n-2))

def ClassExQ1(x,n):
    if n <= 1:
        return x
    else:
        return x * ClassExQ1(x,n-1)

def ClassExQ2(x,n):
    if n ==0:
        return 1
    elif n == 1:
        return x
    if n % 2 == 1:
        return x * ClassExQ2(x,n//2)* ClassExQ2(x,n//2)
    else:
        return ClassExQ2(x,n//2)* ClassExQ2(x,n//2)
# print(ClassExQ2(6,3))

def reverse(a):
    if len(a)== 1:
        return [a]
    return [a[-1]] + reverse(a[:-1])

# print(reverse('apple'))

def max_array(a):
    if len(a) == 1:
        return a[0]
    return max(a[0],max_array(a[1:]))
print(max_array([8,9,12,16,32]))