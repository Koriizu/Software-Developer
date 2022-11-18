from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
teller = 9
bewegen = True
while bewegen:
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        bewegen = False
    else:
        for x in range(0,teller):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,teller):
            robotArm.moveLeft()
        teller -=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()