import time

nummer = 30

print("Lancering over 30..")
while True:
    nummer -= 1
    time.sleep(1)
    print(nummer)
    if nummer == 0:
        print ("Lancering gaat van start")
        break