from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 1


for y in range(1,5): 
    for z in range(y):
        robotArm.grab()
        for y in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()

    




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()