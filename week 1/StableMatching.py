male_preference = [[1,3,2,4],[1,2,4,3],[1,2,3,4],[2,3,1,4]]
female_preference = [[2,1,3,4],[4,3,2,1],[1,2,3,4],[3,4,2,1]]

males = {
    "M1": False,
    "M2": False,
    "M3": False,
    "M4": False,
}
females = {
    "F1": False,
    "F2": False,
    "F3": False,
    "F4": False,
}
malesName = list(males.keys())
femalesName = list(females.keys())
def returnIndex(str):
    return int(str[1:]) -1

for male in malesName:
    if (males[male] == False):
        name = male
        index = returnIndex(name)

# in progress
