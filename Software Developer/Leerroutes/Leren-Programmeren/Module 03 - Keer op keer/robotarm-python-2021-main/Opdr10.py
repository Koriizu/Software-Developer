from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

n = 8
x = 9
for j in range(5):
    robotArm.grab()
    for k in range(x):
        robotArm.moveRight()
    robotArm.drop()
    for p in range(n):
        robotArm.moveLeft()
    x-=2
    n-=2




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()