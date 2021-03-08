def group(s):
    total = sum(s)
    s1 = []
    s2 = []
    if total % 2 == 1 or total ==0:
        return None,None
    else:
        sumToFind = total/2
        # sortS= rmSort(s)
        sortS = sorted(s, key=int, reverse=True)
        hasNegative = False
        negativePos = -1
        for i in range(len(sortS)):
            if sortS[i] < 0:
                hasNegative = True
                negativePos = i

        if hasNegative:
            for i in range(negativePos):
                if sum(s1) < sum(s2):
                     s1.append(sortS[i])
                else:
                    s2.append(sortS[i])
            for i in range(negativePos,len(sortS)):
                if sum(s1) < sum(s2) or sum(s2) + s[i] == sumToFind:
                    s2.append(sortS[i])
                elif sum(s1) > sum(s2) or sum(s1) + s[i] == sumToFind:
                    s1.append(sortS[i])

        else:
            for i in range(len(sortS)):
                if sum(s1) < sum(s2) or sum(s1)+ s[i] == sumToFind:
                    if s[i] < 0:
                        s2.append(sortS[i])
                    else:
                        s1.append(sortS[i])
                else:
                    if s[i] < 0:
                        s1.append(sortS[i])
                    else:
                        s2.append(sortS[i])
    return s1, s2