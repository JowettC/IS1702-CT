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

def dfs(graph, start, end):
    fringe = [(start, [])]
    count = 0
    print(fringe)
    while fringe:
        # count += 1
        # if count > 100000:
        #     break
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
    
    cycles = [[s]+path for path in dfs(graph, s, s)]
    if len(cycles) == 0:
        return []
    cycles.sort(key=len,reverse=True)
    return list(reversed(cycles[0]))

file_name = "case2.csv"
s = 10
followers = read_file(file_name)
print(len([10, 164, 85, 494, 446, 132, 84, 81, 430, 379, 333, 318, 454, 492, 323, 
366, 13, 105, 9, 293, 19, 100, 475, 342, 128, 74, 260, 374, 415, 409, 48, 30, 418, 37, 399, 298, 204, 147, 407, 86, 256, 200, 83, 369, 303, 14, 
472, 203, 279, 195, 89, 368, 315, 416, 271, 55, 80, 297, 355, 444, 310, 
458, 78, 328, 322, 473, 135, 129, 371, 136, 116, 481, 401, 180, 189, 169, 110, 231, 468, 421, 384, 308, 439, 184, 456, 461, 395, 281, 296, 245, 
411, 225, 160, 59, 300, 143, 233, 410, 214, 327, 302, 292, 426, 196, 124, 90, 367, 285, 340, 18, 354, 435, 183, 364, 175, 455, 66, 282, 242, 133, 330, 251, 60, 209, 230, 6, 254, 413, 199, 359, 62, 341, 23, 122, 484, 
8, 442, 482, 334, 22, 356, 102, 154, 445, 428, 68, 459, 146, 469, 249, 406, 187, 394, 172, 412, 216, 491, 236, 112, 219, 253, 490, 397, 448, 208, 15, 383, 67, 198, 58, 453, 29, 441, 190, 402, 92, 217, 226, 113, 148, 
382, 247, 436, 224, 107, 75, 370, 232, 12, 26, 295, 28, 348, 82, 304, 381, 103, 218, 352, 499, 278, 4, 40, 157, 38, 73, 32, 257, 104, 495, 414, 
294, 258, 485, 488, 392, 17, 419, 87, 27, 239, 1, 483, 117, 188, 393, 479, 378, 202, 301, 35, 290, 403, 385, 108, 457, 309, 386, 347, 237, 277, 
16, 159, 174, 79, 77, 138, 139, 207, 252, 205, 241, 429, 262, 388, 463, 
222, 144, 70, 179, 447, 337, 162, 223, 166, 450, 360, 423, 273, 24, 20, 
345, 197, 314, 283, 363, 487, 176, 42, 3, 220, 343, 25, 268, 229, 373, 357, 45, 41, 464, 451, 95, 437, 140, 156, 53, 496, 250, 289, 346, 405, 305, 264, 498, 47, 476, 331, 158, 471, 336, 123, 98, 163, 131, 486, 265, 115, 460, 212, 64, 465, 372, 215, 362, 152, 255, 320, 52, 182, 434, 210, 
221, 31, 339, 97, 125, 433, 228, 137, 391, 71, 349, 119, 306, 170, 332, 
478, 49, 317, 287, 443, 467, 353, 480, 291, 150, 194, 109, 338, 404, 51, 21, 351, 390, 165, 274, 358, 149, 477, 243, 389, 321, 34, 118, 211, 178, 424, 269, 177, 126, 497, 408, 319, 167, 398, 489, 365, 192, 462, 466, 
263, 272, 234, 376, 56, 493, 270, 57, 240, 275, 350, 311, 181, 329, 213, 425, 235, 361, 155, 206, 470, 324, 36, 248, 127, 432, 141, 431, 91, 61, 227, 422, 186, 43, 325, 474, 201, 316, 267, 63, 69, 261, 244, 191, 130, 33, 280, 72, 65, 259, 0, 101, 106, 120, 39, 50, 440, 377, 286, 76, 452, 96, 111, 420, 134, 121, 145, 193, 11, 44, 396, 168, 88, 54, 46, 288, 344, 93, 10]))
print(len([0, 110, 231, 323, 441, 80, 297, 142, 85, 468, 246, 55, 318, 448, 208, 5, 210, 196, 198, 200, 83, 242, 114, 252, 258, 293, 180, 379, 37, 105, 3, 220, 347, 397, 472, 401, 136, 116, 481, 260, 374, 48, 30, 77, 307, 8, 359, 394, 23, 122, 484, 154, 232, 236, 112, 84, 81, 271, 171, 159, 174, 79, 74, 455, 430, 282, 153, 6, 254, 322, 78, 328, 296, 256, 59, 300, 143, 411, 225, 160, 290, 104, 107, 140, 164, 459, 499, 298, 169, 224, 370, 406, 417, 247, 436, 216, 491, 187, 204, 147, 407, 223, 354, 435, 183, 364, 189, 67, 482, 334, 22, 418, 434, 4, 40, 157, 38, 73, 32, 496, 250, 209, 292, 426, 327, 302, 132, 99, 18, 375, 148, 382, 53, 233, 410, 214, 313, 310, 458, 469, 249, 315, 416, 368, 321, 203, 279, 195, 19, 94, 268, 241, 429, 262, 388, 463, 442, 14, 184, 492, 301, 35, 113, 135, 129, 371, 95, 437, 117, 188, 393, 479, 378, 202, 341, 413, 199, 150, 194, 109, 156, 475, 342, 128, 285, 340, 414, 294, 333, 383, 146, 66, 212, 64, 7, 412, 
217, 226, 58, 453, 29, 182, 245, 20, 345, 197, 454, 332, 478, 49, 343, 25, 71, 348, 89, 277, 16, 366, 392, 17, 419, 251, 60, 362, 152, 255, 320, 52, 384, 103, 218, 352, 82, 304, 381, 386, 172, 230, 309, 28, 402, 92, 
165, 166, 450, 360, 423, 273, 24, 495, 278, 398, 237, 190, 355, 464, 15, 88, 54, 46, 288, 344, 93, 10, 314, 308, 439, 390, 229, 306, 170, 485, 488, 133, 330, 415, 409, 396, 168, 219, 253, 490, 175, 457, 124, 395, 281, 42, 356, 102, 483, 12, 26, 295, 27, 239, 1, 456, 461, 13, 391, 257, 75, 90, 367, 444, 151, 149, 477, 243, 389, 349, 119, 173, 399, 380, 339, 97, 125, 433, 228, 137, 465, 372, 215, 177, 126, 497, 408, 319, 167, 373, 357, 45, 41, 222, 144, 70, 179, 447, 115, 460, 312, 421, 11, 44, 337, 162, 87, 427, 336, 123, 98, 163, 131, 486, 265, 403, 385, 108, 284, 494, 
9, 47, 476, 331, 158, 471, 289, 346, 405, 305, 264, 498, 283, 363, 487, 
176, 205, 445, 428, 68, 369, 178, 424, 269, 34, 118, 211, 274, 358, 338, 404, 51, 21, 351, 221, 31, 138, 139, 207, 111, 420, 134, 121, 145, 193, 317, 287, 443, 467, 353, 480, 291, 101, 106, 120, 39, 50, 440, 377, 286, 76, 452, 96, 489, 365, 192, 462, 466, 263, 272, 234, 376, 56, 493, 270, 57, 240, 275, 350, 311, 181, 329, 213, 425, 235, 361, 155, 206, 470, 324, 36, 248, 127, 432, 141, 431, 91, 61, 227, 422, 186, 43, 325, 474, 201, 316, 267, 63, 69, 261, 244, 191, 130, 33, 280, 72, 65, 259, 0] ))
print(get_cycle(followers,s))