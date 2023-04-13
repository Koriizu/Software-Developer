import random

class Africa:
    def getalofzo(self):
        getal = random.randint(0,5)
        return getal

hp = 10
africa_instance = Africa()  # create an instance of the Africa class
kevin_getal = africa_instance.getalofzo()  # call getalofzo() on the instance
hp = hp - kevin_getal

print(hp)