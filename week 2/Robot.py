class Robot:
    # default constructor 
    def __init__(self): 
        self.age = 1
  
    # a method for printing data members 
    def grow(self):
        self.age += 1

    def print_age(self): 
        print(self.age) 