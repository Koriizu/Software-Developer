import random
import time
def game():
    class Player():
        hp = 100
        energy = 0
        def __init__(self,name):
            self.name = name
            
        def normal_atk(self):
            attack = random.randint(0, 16)
            return attack
        
        def spec_attack(self):
            spec_attack = random.randint(20, 41)
            return spec_attack
        
        def healing(self):
            healing = random.randint(10, 35)
            return healing
        
        def perform_normal_attack(self, foe):
            player_normal_attack = self.normal_atk()
            foe.hp = foe.hp - player_normal_attack
            player_energy += 10
            time.sleep(1)
            print(f"\n {name} just did {player_normal_attack} damage!")
            print(f"{name} now has {player_hp} health and {player_energy} energy!")
            time.sleep(1)
            print(f"The {foe.name} now has {comp_hp} health and {comp_energy} energy!")
             
        

    def first_turn():
        go = random.randint(0, 2)
        if go == 0:
            return 'comp'
        else:
            return name
    
    wins = 0
    name = input("Fill in your name: ")
    turn = first_turn()
    loop = True
    
    while loop:
        player_hp = 100
        player_energy = 0
        comp_hp = 100
        comp_energy = 0

        player = Player('arda')
        comp = Player('comp')

        while player_hp > 0 and comp_hp > 0:
            print(f"\n{turn}'s turn")
            if turn != 'comp':
                try:
                    action = int(input(f"{name}, please choose an action:\n1) Normal Attack\n2) Special Attack\n3) Heal\n"))
                    if action == 1:
                        player.perform_normal_attack(comp)
                        # player_normal_attack = player.normal_atk()
                        # comp_hp = comp_hp - player_normal_attack
                        # player_energy += 10
                        # time.sleep(1)
                        # print(f"\n {name} just did {player_normal_attack} damage!")
                        # print(f"{name} now has {player_hp} health and {player_energy} energy!")
                        # time.sleep(1)
                        # print(f"The Computer now has {comp_hp} health and {comp_energy} energy!")
                        turn = 'comp'
                    elif action == 2 and player_energy >= 20:
                        player_special_attack = player.spec_attack()
                        comp_hp = comp_hp - player_special_attack
                        player_energy -= 20
                        time.sleep(1)
                        print(f"\n{name} just did {player_special_attack} damage!")
                        print(f"{name} now has {player_hp} health and {player_energy} energy!")
                        time.sleep(1)
                        print(f"The Computer now has {comp_hp} health and {comp_energy} energy!")
                        turn = 'comp'
                    elif action == 3 and player_energy >= 15:
                        player_heal = player.healing()
                        player_hp += player_heal
                        player_energy -= 15
                        time.sleep(1)
                        print(f"\n{name} just healed themselves for {player_heal}!")
                        print(f"{name} name has now {player_hp} health and {player_energy} energy!")
                        turn = 'comp'
                    elif action == 2 or action == 3 and player_energy < 15:
                        print(f"\n{name} you have {player_hp} health and {player_energy} energy.")
                        print(f"Your energy is too low, please choose 1) Normal Attack: ")
                    else:
                        print("Please enter a correct action. ")
                except:
                    print("Please enter a correct action. ")
            else:
                if comp_hp <= 50 and comp_energy >= 15:
                    comp_healing = comp.healing()
                    comp_hp += comp_healing
                    comp_energy -= 15
                    time.sleep(1)
                    print(f"\nThe Computer has healed themselves for {comp_healing} health!")
                    print(f"{name} now has {player_hp} health and {player_energy} energy!")
                    time.sleep(1)
                    print(f"The Computer now has {comp_hp} health and {comp_energy} energy!")
                    turn = name
                elif comp_energy >= 20:
                    comp_special_attack = comp.spec_attack()
                    player_hp = player_hp - comp_special_attack
                    comp_energy -= 20
                    time.sleep(1)
                    print(f"\n the Computer just did {comp_special_attack} damage!")
                    print(f"{name} now has {player_hp} health and {player_energy} energy!")
                    time.sleep(1)
                    print(f"The Computer now has {comp_hp} health and {comp_energy} energy!")
                    turn = name
                else:
                    comp_normal_attack = comp.normal_atk()
                    player_hp = player_hp - comp_normal_attack
                    comp_energy += 10
                    time.sleep(1)
                    print(f"\nThe Computer just did {comp_normal_attack} damage!")
                    print(f"{name} now has {player_hp} health and {player_energy} energy!")
                    print(f"The Computer now has {comp_hp} health and {comp_energy} energy!")
                    turn = name

        if player_hp <= 0:
            print("\nThe Computer has won this round!")
            print(f"\n{name} has won {wins} rounds, you can do better next time!")
        elif comp_hp <= 0:
            print(f"\n{name} has won this round!")
            wins +=1

        play_again = input("Do you want to play again? (Y/N) ").lower()
        if play_again != "y":
            print(f"Thanks for playing! Your final score is {wins}.")
            loop = False
        else:
            pass


game()