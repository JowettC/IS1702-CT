def perm(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    for letter in s1:
        if letter not in s2:
            return False
        else:
            s2.remove(letter)
    return True

# print(perm('abcd','dcba'))