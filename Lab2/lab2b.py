def read_file_2b(file_name):
    my_list = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            id = int(line.split(",")[0])
            year = int(line.split(",")[1])
            my_list.append([id, year])
    file.close()
    return my_list


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        elif left[i][1] == right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergesort(list):
    if len(list) < 2:
        return list

    middle = int(len(list)/2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)


def perform_once_2b(employee_with_birthyear_list):
    # merge sort to brithyear_list
    return mergesort(employee_with_birthyear_list)

def exist(year, employee_list):
    lower = -1
    upper = len(employee_list)
    while lower < upper:
        mid = (upper + lower)//2
        if employee_list[mid][1] > year:
            upper = mid
        elif employee_list[mid][1] < year:
            lower = mid + 1
        else:
            return mid
    return -1
# TODO:
# Write a function called get_IDs_with_birthyear that takes in a year (as an integer) and a list (employee_with_birthyear_list)
# It then returns a list of employee IDs (integers) that have matching birthyears.
def searchLeftAndRight(index,year,employee_with_birthyear_list):
  res = []
  # right
  for i in range(index, len(employee_with_birthyear_list)):
    if employee_with_birthyear_list[i][1] == year:
      res.append(employee_with_birthyear_list[i][0])
    else:
      break
  for i in range(index-1, -1,-1):
    if employee_with_birthyear_list[i][1] == year:
      res.append(employee_with_birthyear_list[i][0])
    else:
      break
  return res


def get_IDs_with_birthyear(year, employee_with_birthyear_list):
    return searchLeftAndRight(exist(year,employee_with_birthyear_list),year,employee_with_birthyear_list)