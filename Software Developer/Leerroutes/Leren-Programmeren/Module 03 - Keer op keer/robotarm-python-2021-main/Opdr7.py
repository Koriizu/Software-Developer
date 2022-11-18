from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5

for k in range(5):
    robotArm.moveRight()
    for x in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if k == 4:
            break
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

