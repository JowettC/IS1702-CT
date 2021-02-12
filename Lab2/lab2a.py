def perform_once_2a(employee_list):
    # do nothing
    return set(employee_list)


def interpolationSearch(arr, lo, hi, x):
 
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
 
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
 
        # Condition of target found
        if arr[pos] == x:
            return True
 
        # If x is larger, x is in right subarray
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)
 
        # If x is smaller, x is in left subarray
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return False
def exist(id, employee_list):
    if id in employee_list:
        return True
    return False
    
# def exist(id, employee_list):
#     lower = -1
#     upper = len(employee_list)
#     while lower < upper:
#         mid = (upper + lower)//2
#         if employee_list[mid] > id:
#             upper = mid
#         elif employee_list[mid] < id:
#             lower = mid + 1
#         else:
#             return True
#     return False