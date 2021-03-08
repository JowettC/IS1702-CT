

def mergeSort(myList):
    # print(myList)
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


def select_tweeters(followers):
    UserUnqiueCount= {}
    FollowersReached = []
    # sorted_followers = []
    # for user in followers:
    #     mergeSort(user)
    #     sorted_followers.append(user)



    # print (sorted_followers)
    # brute force appraoch ??
    res=[]
    for i in range(0,len(followers)):
        count = 0
        for j in range(0,len(followers[i])):
            if followers[i][j]:
                count += 1
                FollowersReached.append(followers[i][j])
        UserUnqiueCount[i] = count
    sorted_keys = sorted(UserUnqiueCount,key=UserUnqiueCount.get)
    print(sorted_keys)
    for i in range(0,5):
        res.append(sorted_keys[len(sorted_keys)-(i+1)])

    # print(get_unique_followers ([0,1,2,3,4], followers))
    # for i in range(0,len(sorted_followers)):


    # currently, this function always returns the first five users
    # obviously this arbitrary selection will result in a lousy quality score even though it's a "correct" answer :-/
    return res
