from RobotArm import RobotArm
from shutil import move


robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2

nummer = 1
for x in range(8):
    robotArm.moveRight()
for x in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for a in range(nummer):
            robotArm.moveRight()
            robotArm.drop()
        for p in range(nummer+1):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
        nummer+=1
        
    
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()