# EXTRACT THIS CODE & SUBMIT AS p1q1.py TO RED!!!
# Filename: p1q1.py
# Name:    Kim Han Nah
# Section: G4

# Except import statements, all other statements should only be in functions.

def group(s):
    # TODO: edit this function.
    s1=[]
    s2=[]
    
    s.sort(reverse=True)
    #check if numbers can be divided into 2.
    if(sum(s)%2!=0):
        return None,None
    else:
        #number match
        average = sum(s)//2
        first=s[0]
        last = s[len(s)-1]
        s1=[first]
        #remaining values inside
        #check for negative number in list
        have_neg= False
        first_neg_pos=0
        for k in range(len(s)):
            if s[k]<0 and first_neg_pos == 0:
                have_neg=True
                first_neg_pos=k
                print(s,first_neg_pos)
            if(have_neg):    
                for i in range(1,first_neg_pos):
                    if sum(s1)<sum(s2):
                        s1.append(s[i])
                    if sum(s1)>sum(s2):
                        s2.append(s[i])
                for j in range(first_neg_pos,len(s)):
                    if (sum(s1)+ s[j]) == average or sum(s1)<sum(s2):
                        s1.append(s[j])
                    elif sum(s1)+ s[j]== average or sum(s1)>sum(s2):
                        s2.append(s[j])
                else:
                    for i in range(len(s)):
                        if sum(s1)<sum(s2):
                            s1.append(s[i])
                        elif sum(s1)>sum(s2):
                            s2.append(s[i])   
           
      
      
    return s1,s2

  

import time

#test case 1a (based on e.g. 1)
s = [-1, 1, 4, 2, 8, 0]

print("Calling your group function now using s = " + str(s))
start_time = time.time()
s1, s2 = group(s) # calls your function
time_taken = time.time() - start_time
print("Execution time " + str(time_taken) + " seconds.\n")    # display time lapsed

sum_s1 = sum(s1)
sum_s2 = sum(s2)

# print outcome
print("Your function returned: ")
print("    s1 = " + str(s1) +", sum(s1) = " + str(sum_s1))
print("    s2 = " + str(s2) +", sum(s2) = " + str(sum_s2))

# check correctness
if sum_s1 == sum_s2:
  print("test case passed")
else: 
  print("test case FAILED")