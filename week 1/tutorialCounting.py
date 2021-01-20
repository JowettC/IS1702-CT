# question 2
n = 100
count = 0
for i in range (n,1000):
    if i % 3 == 0 and i % 4 == 0:
        count = count + 1
print (count)
