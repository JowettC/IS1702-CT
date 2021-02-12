import asyncio
import random
import time
NO_OF_REPETITIONS = 1000


def read_file_2a(file_name):
    my_list = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            id = int(line.split(",")[0])
            my_list.append(id)
    file.close()
    return my_list


def perform_once_2a(employee_list):
    # do nothing
    return employee_list


async def exist(id, employee_list):
    lower = -1
    upper = await len(employee_list)
    while True:
        mid = (upper + lower)//2
        if employee_list[mid] > id:
            upper = mid
        if employee_list[mid] < id:
            lower = mid + 1
        if employee_list[mid] == id:
            return True
        if lower + 1 == upper:
            return False


# (1) ----- prepare data -----
random_numbers = []  # list to store random numbers later
for i in range(NO_OF_REPETITIONS):
    # generate a random employee ID between 0 and 2000000
    random_numbers.append(random.randint(0, 2000000))
results = []  # used to store all your results later

# employees_1mil is similiar to employees_10.csv, except that it contains 1 million IDs
employee_list = read_file_2a("./content/employees_1mil.csv")

# make a clone of employee_list. This clone employee_list_clone will be used for correctness testing later
employee_list_clone = list(employee_list)  # CHANGED


# (2) ----- performance testing -----
print("Starting timer")
start_time = time.time()

print("Calling your perform_once function now")
employee_list = perform_once_2a(employee_list)  # does nothing for now

print("Calling exist " + str(NO_OF_REPETITIONS) + " times...")
for i in range(NO_OF_REPETITIONS):
    r = random_numbers[i]  # random number
    result = exist(r, employee_list)
    results.append(result)  # store current result in results. CHANGED

time_taken = time.time() - start_time
print("Execution time " + str(time_taken) +
      " seconds.")    # display time lapsed

# (3) ----- correctness checking ----- CHANGED
# check first 100 values in results
print("Checking the first 100 results now...")
all_correct = True
for i in range(min(100, NO_OF_REPETITIONS)):
    if results[i] != (random_numbers[i] in employee_list_clone):
        print("ERROR in your result when searching for employee ID " +
              str(random_numbers[i]))
        all_correct = False

# (4) ----- show results ----- CHANGED
if all_correct:
    print("Results are correct! - you may upload lab2a.py to the submission server")
else:
    print("Your exist function is not correctly written :-(")
