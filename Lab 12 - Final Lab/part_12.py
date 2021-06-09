import random
import arcade


def intro_to_game():
    # This function introduces the player to the game.
    print("Welcome to the Guess the Number!")
    print("There's a number in my head from 1-20!")
    print("You will have five tries to guess this number.")
    print("If you guess the number correctly, you will win!")
    print("If you guess the number incorrectly after 5 tries, you will lose!")
    print("Plus, only numerical answers are accepted.")
    print("Oh, one more thing... The less tries taken, the higher your score!")
    print("Good luck, telepath!")
    print()


def generate_random_num():
    # This function will generate the number for the player to guess.
    number = random.randrange(1, 20)
    return number


def ask_user():
    # This function will retrieve the user's guess
    guess = input("Take a guess:").lstrip()
    guess = int(guess)
    return guess


def compare_guess(number, user_guess):
    # Compares the user's guess to the actual rand number.
    if user_guess < number:
        print("Sorry, your guess is smaller than my number.")
        return False
    elif user_guess > number:
        print("Sorry, your guess is larger than my number.")
        return False
    else:
        print("Correct! You guessed the right number. You win!")
        return True


def final_victory_graphic(score, tries):
    arcade.open_window(800, 800, "Guessing Game")
    arcade.start_render()
    arcade.set_background_color(arcade.csscolor.BLACK)
    for i in range(100):
        arcade.draw_circle_filled(10 * i, 20, 10, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(10 * i, 780, 10, arcade.csscolor.WHITE)
    arcade.draw_text(f"Congratulations, telepath! You have won! Your score was {score}.", 0, 400, arcade.csscolor.GOLD,
                     19, 800, "center")
    arcade.draw_text(f"That took you {tries} tries!", 0, 370, arcade.csscolor.GOLD,
                     19, 800, "center")
    arcade.finish_render()


def final_failure_graphic():
    arcade.open_window(800, 800, "Guessing Game")
    arcade.start_render()
    arcade.set_background_color(arcade.csscolor.BLACK)
    for i in range(100):
        arcade.draw_circle_filled(10 * i, 20, 10, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(10 * i, 780, 10, arcade.csscolor.WHITE)
    arcade.draw_text(f"Nice try, telepath! You failed to guess the number.", 0, 400, arcade.csscolor.GOLD, 19, 800,
                     "center")
    arcade.draw_text("Try again!", 0, 370, arcade.csscolor.GOLD,
                     19, 800, "center")
    arcade.finish_render()


def play_game():
    # This function actually executes the game.
    score = 5
    tries = 1
    intro_to_game()
    random_number = generate_random_num()
    for i in range(5):
        guess = ask_user()
        is_correct = compare_guess(random_number, guess)
        if is_correct:
            final_victory_graphic(score, tries)
            arcade.run()
            break
        if not is_correct:
            score -= 1
            tries += 1
            print(f"You have {score} tries left!")
    final_failure_graphic()
    arcade.run()


def main():
    play_game()


main()