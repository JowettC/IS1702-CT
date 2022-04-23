def solve(n, date):
    # Write your code here
    dictGame = dict()
    for i in range (1,n+1):
        dictGame[i] = date[i]
    # populate dates
    dictDate = dict()
    for i in range(findMaxDate(date)):
        dictDate[i] = 0
    
    for key in dictGame.keys():
        for day in range(dictGame[key][0],dictGame[key][1]+1):
            dictDate[day] += 1
    res = 0
    for key in dictDate.keys():
        if (dictDate[key] > res):
            res = dictDate[key]
    return res


def findMaxDate(date):
    res = 0
    for i in date:
        if i[0] > res:
            res = i[0]
        elif i[1] > res:
            res = i[0]
        else:
            continue
    return res

solve(3,[[1,2],[2,4],[2,4]])