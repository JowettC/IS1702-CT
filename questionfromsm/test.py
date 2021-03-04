def perm(s1,s2):
    if len(s1) != len(s2):
        return False
    for letter in s1:
        if letter not in s2:
            return False
    return True