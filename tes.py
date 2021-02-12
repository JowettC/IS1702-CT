import time

def three_second_rule():
    res = False
    t_end = time.time() + 3 
    i = 0
    while time.time() < t_end:
        i = i +1
        print("testing" + str(i))
three_second_rule()