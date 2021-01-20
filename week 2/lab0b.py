# lab0b.py - TO BE SUBMITTED to RED
# All statements should only be in functions. Do not include statements outside functions in this file.
# fill up the weight_category method to return either "underweight", "overweight" or "normal" 
# depending on the height (in cm) and weight (in kg)

# Name: 
# Section: 

def weight_category(weight, height):
  bmi = weight/(height/100)**2
  if bmi > 25:
    return "overweight"
  elif bmi < 18.5:
    return "underweight"
  else:
    return "normal"
  return "dummy_value"  