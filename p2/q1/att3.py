import copy
import time

def read_file(file_name):
    input = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            current_list = line.split(",")
            # 1st element is the index. assumption: the index is always in sequence: 0, 1, 2,.... etc
            index = int(current_list.pop(0))
            # convert all elements from strings into ints
            current_list = [int(i) for i in current_list]
            input.append(current_list)        # insert into list
    return input

<<<<<<< Updated upstream
def convertToGraph(arr):
    g = {}
    for i in range(len(arr)):
        g[i] = arr[i]
    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         if arr[i][j] in arr[i]:
    #             g[arr[i][j]].append(i)
    return g

def copyArr(Arr):
    res =[]
    for item in Arr:
        res.append(item)
    return res

def validate(g,arr):
    res = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] not in g[arr[i-1]]:
            continue
        else:
            res.append(arr[i])
    return res
def get_cycle(followers, s):
    g = convertToGraph(followers)
    print(g)
    # print(g)
    stack = []
    cycles = []
    visited = []
    stack.append(s)
    while len(stack) > 0:
        havedepth = False
        temp = stack[-1]
        del stack[-1]
        if temp not in visited:
            visited.append(temp)
            if s in g[temp]:
                cycles.append(copyArr(visited))
            # print(v)
        adjList = g[temp]
        for i in range(len(adjList)):
            n = adjList[len(adjList)-1-i]
            if n not in visited:
                havedepth = True
                stack.append(n)
        if havedepth == False:
            del visited[-1]
    # return cycles
    if len(cycles) == 0:
        return []
    else:
        cycles.sort(key=len,reverse=True)
        res = cycles[0]
        res = res + [s]
        res = validate(g,res)
        return list(reversed(res))
=======
def dfs(graph, start, end):
    fringe = [(start, [])]
    count = 0
    while fringe:
        count += 1
        if count > 100000:
            break
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

def get_cycle(followers,s):
    graph ={}
    for i in range(len(followers)):
        graph[i] = followers[i]
    print(graph)
    cycles = [[s]+path for path in dfs(graph, s, s)]
    if len(cycles) == 0:
        return []
    cycles.sort(key=len,reverse=True)
    return list(reversed(cycles[0]))

>>>>>>> Stashed changes

test = [10, 470, 467, 123, 457, 435, 347, 475, 311, 483, 247, 277, 74, 225, 216, 222, 383, 164, 102, 16, 411, 361, 317, 442, 402, 486, 384, 113, 44, 127, 187, 220, 37, 166, 396, 369, 346, 86, 458, 481, 211, 236, 31, 2, 460, 262, 288, 111, 61, 462, 299, 448, 240, 81, 109, 15, 70, 421, 374, 404, 437, 314, 289, 248, 259, 342, 142, 353, 461, 88, 469, 172, 454, 30, 254, 423, 155, 425, 145, 327, 430, 6, 215, 302, 140, 58, 249, 119, 173, 29, 487, 422, 400, 19, 148, 471, 99, 122, 83, 64, 465, 218, 459, 399, 121, 212, 490, 371, 348, 360, 234, 335, 179, 392, 26, 377, 78, 333, 82, 283, 432, 331, 174, 337, 143, 159, 204, 76, 24, 365, 332, 351, 444, 90, 391, 223, 36, 12, 28, 307, 280, 38, 226, 103, 59, 158, 358, 149, 25, 114, 390, 67, 419, 96, 420, 258, 213, 17, 132, 205, 352, 100, 268, 229, 426, 206, 367, 188, 203, 93, 321, 52, 478, 441, 69, 320, 135, 282, 260, 315, 278, 45, 209, 328, 46, 476, 266, 373, 279, 270, 51, 355, 397, 153, 322, 447, 75, 108, 261, 68, 80, 359, 344, 296, 452, 235, 434, 101, 436, 313, 171, 85, 128, 66, 147, 413, 330, 251, 324, 95, 264, 295, 318, 388, 394, 491, 189, 190, 417, 165, 4, 20, 237, 407, 199, 468, 416, 381, 50, 104, 484, 410, 71, 405, 34, 27, 463, 181, 157, 255, 84, 14, 257, 290, 243, 482, 271, 306, 370, 194, 112, 372, 474, 284, 246, 499, 156, 301, 73, 379, 415, 8, 116, 55, 378, 362, 182, 443, 232, 241, 89, 124, 92, 363, 169, 472, 466, 265, 7, 56, 177, 115, 178, 256, 366, 134, 94, 376, 228, 479, 131, 1, 72, 162, 97, 65, 439, 0, 110, 431, 338, 385, 364, 403, 146, 485, 168, 309, 245, 42, 253, 494, 305, 453, 408, 227, 498, 340, 418, 495, 427, 197, 170, 292, 184, 291, 160, 39, 54, 48, 300, 492, 269, 319, 53, 231, 263, 401, 150, 202, 287, 304, 456, 497, 393, 308, 196, 43, 297, 496, 201, 133, 49, 480, 294, 200, 325, 41, 117, 191, 126, 477, 414, 273, 445, 47, 336, 489, 175, 382, 242, 214, 473, 493, 349, 5, 195, 219, 120, 107, 186, 455, 350, 375, 33, 106, 230, 356, 239, 389, 244, 193, 488, 13, 334, 22, 32, 3, 35, 198, 129, 77, 380, 130, 180, 409, 345, 233, 450, 141, 11, 286, 368, 386, 440, 62, 18, 329, 281, 398, 446, 138, 354, 272, 464, 312, 167, 125, 303, 87, 274, 105, 137, 316, 343, 183, 424, 412, 293, 310, 221, 339, 298, 118, 207, 210, 79, 21, 208, 57, 98, 192, 23, 285, 429, 176, 433, 224, 151, 406, 144, 136, 10]
print(len(test))

# file_name = "case1a.csv"
s = 0
# followers = read_file(file_name)
a = [[5, 8, 10], [2, 6], [1, 3], [1, 5], [2, 5], [4, 6, 9], [1, 3, 9], [6], [7, 10], [0, 6, 8, 10], []]
# followers_clone = copy.deepcopy(followers)
test = [0, 5, 4, 2, 1, 6, 9, 0]
# test = [0, 9, 6, 1, 2, 4, 5, 0]
# g = {0: [5, 8, 10], 1: [2, 6], 2: [1, 3], 3: [1, 5], 4: [2, 5], 5: [4, 6, 9], 6: [1, 3, 9], 7: [6], 8: [7, 10], 9: [0, 6, 8, 10], 10: []}
# print(get_cycle(a,s))
# print(validate(g,test))
