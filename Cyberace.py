#=============================================================
#   Please, don't delete this text
#   Cyberace V1.01
#   https://github.com/kikimori-dev
#   made by kikimori in 2026
#=============================================================
import random
import sys
theend = 0
def menu():
    global theend
    if theend == 50:
        end()
    print("Do you wanna start race?")
    answer = str(input())
    if answer == "Yes":
        gameplay()
    elif answer == "No":
        print("See you later")
        sys.exit()
    elif answer == "Where I'm?":
        story()
    else:
        print("error")
        sys.exit()

def gameplay():
    global theend
    car_1 = (random.randint(50, 1000))
    car_2 = (random.randint(50, 1000))
    print("Change your speed")
    player = int(input())
    if player >= 1000:
        if player == 1987:
            print("Freddy Fazbear")
            menu()
        else:
            print("You're a car, not a rocket. The race isn't in orbit.")
            menu()
    if player == 67:
        print("Ha-ha. Last Monday you live with your 67.")
        menu()
    print(f"Car 1 speed: {car_1}")
    print(f"Car 2 speed: {car_2}")
    print(f"Your speed: {player}")
    if player > car_1 and player > car_2:
        print("You win!")
        theend += 1
        menu()
    elif player < car_1 and player < car_2:
        print("You lose!")
        menu()
    else:
        print("You second. Good.")
        menu()
def story():
    print("Beyond the vast, neon-lit city lies a plaina no-man's-land.")
    print("The acrid stench of gasoline and rubber already permeated the air, yet you had no intention of giving up.")
    print("You came here, and you weren't leaving without a victory.")
    menu()
def end():
    print("After you conquered the peak, you wanted more.")
    print("You decided to try your hand at racing across the wastelands destroyed by nuclear weapons.")
    print("Who knows, maybe you'll conquer the peak not just of your city...")
    print("The end. #made by kikimori in 2026")
print("Cyberace #made by kikimori in 2026")
menu()
