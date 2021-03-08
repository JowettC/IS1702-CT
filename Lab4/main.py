
from helper import *
from lab4 import select_tweeters
from test import select_tweeters1
# Test case lab3
file_name = "case2.csv"  # <---- CHANGE CSV FILE NAME HERE to use a different social network

import time, copy
# (1) ----- prepare data ------
# read from file_name and store in followers
print("(1) Reading data from " + file_name + " now...\n")
followers = read_file(file_name)

# make a clone of the original followers. 
# original_followers will be used for calculating the score later using get_unique_followers.
# this is important just in case the select_tweeters method modifies the values in followers passed in!!
followers_clone = copy.deepcopy(followers)

# (2) ----- run the test case ------
print("(2) Starting timer...")
print("Calling your select_tweeters function now using followers read from " + file_name)
start_time = time.time()
answer = select_tweeters(followers) # calls your function
time_taken = time.time() - start_time
print("Stopping timer...")
print("Execution time " + str(time_taken) + " seconds.\n")    # display time lapsed

# (3) ----- correctness testing code ------ 
print("(3) Checking your answer...")
print("Your select_tweeters function returned this: " + str(answer))
error_message = get_error_message(answer)

if error_message == None:
  # all is good
  print("Your function returned a valid answer - you may upload lab4.py to red")
  reached_audience = get_unique_followers (answer, followers_clone)
  quality_score = len(reached_audience) + len(answer)

  print("The following users will get the advertisement : " + str(reached_audience))
  print("Quality score : " + str(quality_score))
else:
  # there is an error
  print("Your function is not correctly written :-(")
  print(error_message)