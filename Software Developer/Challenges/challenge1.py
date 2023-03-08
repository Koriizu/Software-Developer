import math

# def litres(time):
#     return math.floor(time*0.5)

def litres(time):
    return time // 2

time = int(input("How many HOURS has Nathan been cycling? "))

print(f"Nathan needs to drink: {litres(time)} Liters of water")


