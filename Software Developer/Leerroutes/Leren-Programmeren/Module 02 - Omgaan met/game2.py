import time
import sys

def delay_print1 (s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

def delay_print2 (s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print2("Would you like to play? ")
answer = input().lower().strip()

if answer in ("yes", "y", "ja"):
    delay_print2("""
You are in the middle of a zombie apocalypse in 2024 and you are all alone in a hotel filled with zombies.
You must get to the top of the building for the rescue brigade to save you.
Do what you must to survive. 
    """)
    delay_print2("""
You exit your room quietly..
You find yourself having to choose to go either left or right.
(You remember that you had seen a staircase on the right and an elevator on the left)
Go left or right? """)
    answer = input().lower().strip()

    if answer in ("left"):
        delay_print2("""
You slowly walk towards the elevator, when suddenly the door from the room next to yours breaks open..""")
        time.sleep(1)
        delay_print1("""
You can either fight them or run, possibly running into even more zombies.
Run or fight? """)
        answer = input().lower().strip()
        if answer in ("fight"):
            delay_print1("You tried your best fighting them, but ended up being eaten instead! Game over.")

        else:
            delay_print1("You decide to run but from all the noise that you made from running attracted other zombies and they all crowded ontop of you! Game over.")


    else:
        delay_print1("""
    You slowly walk towards the staircase..""")
        time.sleep(1)
        delay_print2("""
    You have successfully arrived at the staircase with no problems.""")
        time.sleep(0.5)
        delay_print2("""
    You slowly start to walk up the stairs, but you hear a lot of zombies on the next floor""")
        delay_print2("""
    Suddenly someone screams, all the zombies are attracted to the opposite side giving you the chance to go upwards""")
        time.sleep(0.3)
        delay_print1("""
    3 more floors till you get to the top..""")
        time.sleep(1)
        delay_print2("""
    After walking up to the next floor you discover that the stairs is blocked here.
    You can either go up from the balconies or go back down and try to take the elevator up..
    Go back down or up? 
        """)
        answer = input().lower().strip()
        if answer == "up":
            delay_print2("""
You decide to go up from the balconies, so you walk towards the closest door, hearing the gnarring of zombies, so you walk towards the next door..
            """)
            delay_print1("""
\x1B[3mYou knock on the door to attract the zombies in the room.\x1B[0m""")
            time.sleep(1)
            delay_print1("""
Nothing happens..""")
            delay_print2("""
You kick the door open and go straight towards the balcony before the zombies come and chase you..""")
            delay_print2("""
You stand on the edge of the balcony, taking a risky jump and grab the edge of the balcony above you and climb up.""")
            time.sleep(2)
            delay_print1("""
After climbing up you hear a noise behind the glass door... It's a zombie, all alone.""")
            delay_print2("""
Take the risk or go back down? """)
            answer = input().lower().strip()

            if answer in "take the risk":
                delay_print1("""
You decide to take the risk..""")
                delay_print2("""
In a rush you open the door and pull the zombie and push it on the ground.
You \x1B[3mwalk in the room, close the door\x1B[0m and take a sigh of relief...""")
                time.sleep(2)
                delay_print2("""
You decide to man up and get out of the room.""")
                delay_print1("""
\x1B[3mYou put your ear on the door and listen for any sound / movement.\x1B[0m You hear a couple zombies.""")
                time.sleep(3)
                delay_print2("""
After some thinking you got a plan. You're going to throw an item and make a run for the top.""")
                delay_print1("You found a soccerball.")
                time.sleep(1)
                delay_print2("""
You shoot the ball in the hall way and close the door again. All the zombies are attracted by the ball and are leaving.""")
                time.sleep(0.3)
                delay_print1("""
You make a run for the top and are safely on the roof, now you just have to wait an hour and you'll be saved by the brigade.""")
            else:
                delay_print2("""
You decide to go down, but a zombie got in the room and ate you up! Game over.""")


        else:
            delay_print2("""
You decide to go down, but the zombies were no longer attracted and crowded ontop of you! Game over.""")

else:
    delay_print2("That's too bad.")