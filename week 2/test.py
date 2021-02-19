import Robot

# robot age 4,5,6 reproduce 1 robot each week
weeks = 30
robotsArray=[]
firstRverRobot = Robot.Robot()
def grow_robot(robotsArray):
    for robot in robotsArray:
        robot.Robot.grow()
        
for i in range(30):
    grow_robot(robotsArray)
