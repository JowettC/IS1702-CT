from LinearDSLab import Queue, Stack
# def s_permutation2(s1, s2):
#     test1 = {}
#     test2 = {}
#         for letter in s1:
#             if letter 

def euclid_gcd_stack(a, b):

    s = Stack()

    s.push(a)

    s.push(b)


    while s.count() > 0:

        b = s.pop()

        a = s.pop()
        if a != b:
            if a>b:
                s.push(a-b)
                s.push(b)
            else:
                s.push(a)
                s.push(b-a)
        else:
            return a
print (euclid_gcd_stack(10,5))
            

