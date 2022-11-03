from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for x in range(7):
    robotArm.moveRight()
robotArm.grab()
for x in range(2):
    robotArm.moveRight()
robotArm.drop()
for x in range(7):
    for x in range(3):
        robotArm.moveLeft()
    robotArm.grab()
    for x in range(2):
        robotArm.moveRight()
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()