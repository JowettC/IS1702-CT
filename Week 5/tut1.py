def pt(n,k):
    if k ==1:
        return 1
    if k == n+1:
        return 1
    return pt(n-1,k-1) + pt(n-1,k)

# print(pt(4,3))

def max_array(a):
    if len(a)==0:
        return 0
    return max(a[0],max_array(a[1:]))

# print(max_array([0,3,56,78,43,8,4,32,44536,12341324,2345324]))

def isPalindrome(s):
    if len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])

# print(isPalindrome("mad3am"))
    
    
