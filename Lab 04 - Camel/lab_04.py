import random
import sys
# Imports random for random numbers and sys for exiting the function quietly.
# Note: I purposely omitted the canteen functionality because I thought having limited drinks was stupid.
# It's so much more fun when  you have unlimited drinks.


def main():
    # Main function and sets up the code to run
    retailer_distance = -20
    player_distance = 0
    win_condition = False
    player_thirst = 0
    camel_tiredness = 0
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the Gobi desert.")
    print("The camel retailers want their camel back and are chasing you down! Survive your")
    print("desert trek and outrun the retailers.")
    total_player_distance = 0
    questions(retailer_distance, player_distance, win_condition, player_thirst,
              camel_tiredness, total_player_distance)

def questions(retailer_distance, player_distance, win_condition, player_thirst,
              camel_tiredness, total_player_distance):
    # Asks the questions and converts user input to readable input
    print("A. Drink from your canteen.")
    print("B. Ahead at moderate speed.")
    print("C. Accelerate at full speed.")
    print("D. Stop for the night.")
    print("E. Status Check.")
    print("Q. Quit")
    choice = input("What is your choice? ")
    choice = choice.upper()
    choice = choice.lstrip()
    print(choice)
    game_action(choice, retailer_distance, player_distance, win_condition, player_thirst,
                camel_tiredness, total_player_distance)


def game_action(choice, retailer_distance, player_distance, win_condition, player_thirst,
                camel_tiredness, total_player_distance):
    # Checks if the player is dead, and if the player is not, sends the input to determine what happened in the turn.
    if camel_tiredness > 5:
        print("Your camel died. Next time, try to rest to help your camel!")
        print("Thank you so much for playing Camel! Feel free to come back and play again!")
        sys.exit()
    elif player_thirst >= 6:
        print("You died of thirst. Thanks for playing! Next time, try to stop and drink from your canteen.")
        print("Thank you so much for playing Camel! Feel free to come back and play again!")
        sys.exit()
    elif total_player_distance - retailer_distance <= 0:
        print("The retailers caught up to you, and took your camel back!")
        print("Thank you so much for playing Camel! Feel free to come back and play again!")
        sys.exit()
    elif total_player_distance > 200:
        print("Congratulations! You escaped the desert with your newly stolen camel!")
        sys.exit()

    while not win_condition:
        player_move(choice, retailer_distance, player_distance, win_condition, player_thirst,
                    camel_tiredness, total_player_distance)


def player_move(choice, retailer_distance, player_distance, win_condition, player_thirst,
                camel_tiredness, total_player_distance):
    # Checks what move the player picked, and executes it accordingly.
    if choice == "A":
        retailer_distance = random.randrange(0, 3) + retailer_distance
        player_thirst = 0
        print(f"You drank out of your canteen, temporarily quenching your thirst. "
              f"Keep going! Your thirst level is {player_thirst}. Don't get too thirsty!")
        questions(retailer_distance, player_distance, win_condition, player_thirst,
                  camel_tiredness, total_player_distance)
    if choice == "B":
        player_distance = random.randrange(5, 8)
        total_player_distance = player_distance + total_player_distance
        print(f"You travelled {player_distance} miles.")
        player_thirst += 1
        camel_tiredness = camel_tiredness + 0.5
        retailer_distance = random.randrange(3, 7) + retailer_distance
        questions(retailer_distance, player_distance, win_condition, player_thirst,
                  camel_tiredness, total_player_distance)
    if choice == "C":
        player_distance = random.randrange(8, 12)
        total_player_distance = player_distance + total_player_distance
        print(f"You travelled {player_distance} miles.")
        player_thirst = player_thirst + 1
        camel_tiredness = camel_tiredness + 1
        retailer_distance = random.randrange(5, 9) + retailer_distance
        questions(retailer_distance, player_distance, win_condition, player_thirst,
                  camel_tiredness, total_player_distance)
    if choice == "D":
        print(f"You stopped for the night, and your camel thanks you greatly. Your camel's tiredness is now zero.")
        camel_tiredness = 0
        retailer_distance = random.randrange(7, 11) + retailer_distance
        questions(retailer_distance, player_distance, win_condition, player_thirst,
                  camel_tiredness, total_player_distance)
    if choice == "E":
        print(f"Your thirst level is currently at {player_thirst}.")
        print(f"You have travelled {total_player_distance} miles. Keep it up!")
        print(f"The retailers are {total_player_distance - retailer_distance} miles away from you. Be careful!")
        print(f"Your camel's tiredness level is {camel_tiredness}.")
        questions(retailer_distance, player_distance, win_condition, player_thirst,
                  camel_tiredness, total_player_distance)
    if choice == "Q":
        print("Thanks for playing camel! Feel free to come back soon!")
        sys.exit()
    else:
        print("Sorry, that is not a choice. Please try again.")
        questions(retailer_distance, player_distance, win_condition, player_thirst,
                  camel_tiredness, total_player_distance)


main()
