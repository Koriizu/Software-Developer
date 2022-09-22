from cgitb import text
import time
import sys
from tkinter.font import BOLD, ITALIC
from turtle import delay

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

delay_print1("Would you like to play? ")
answer = input().lower().strip()

if answer in ("yes", "y", "ja"):

    delay_print1("You've reached Dawn Island, and you find a purple fruit. Would you like to eat it? ")
    answer = input().lower().strip()
    if answer in ("yes", "y", "ja"):
        time.sleep(1)
        delay_print1("You start to feel dizzy"), delay_print2("...")
        time.sleep(3)
        delay_print2('''
3 hours later..''')

        delay_print2("""
SON! """), delay_print1("SON!!!")
        delay_print1("""
ARE YOU OKAY?!?!?
I THOUGHT YOU WERE DONE FOR
After 3 full days of resting..
Son, you're finally ready.. You're ready to set sail and travel the world to find the \33[1mOne Piece.""")

    else:
        delay_print1("After deciding to not eat the fruit, you bring the fruit to your home.")
        delay_print2("...")
        
else:
    print("That's too bad.")