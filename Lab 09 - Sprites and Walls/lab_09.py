# Defining players score
def check_players_guess(guess, answer):
    global score
    guessing = True
    attempt = 0
    while guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print ("Correct")
            score = score + 1
            guessing = False
        else:
            if attempt < 2:
                guess = input("Incorrect, try again")
                attempt = attempt + 1
            if attempt == 3:
                print("The Correct answer is", answer)

# Initial Score
score=0
# Begin Quiz
#Question1
guess1 = input("Who is the King Of Pop?")
guess1=guess1.lstrip()
check_players_guess(guess1, "Michael Jackson")

#Question2
guess2=input("What is the most populated country in the world?")
guess2=guess2.lstrip()
check_players_guess(guess2, "Russia")

#Question3
guess3=input("Who is the founder of the Overlake School?")
guess3=guess3.lstrip()
check_players_guess(guess3, "Charles Clarke")

#Question4
guess4=input("How many times did Italy attempt to invade Ethiopia?")
guess4=guess4.lstrip()
check_players_guess(guess4, "2 times")

#Question5
guess5=input("Which artist has the most grammys?")
guess5=guess5.lstrip()
check_players_guess(guess5, "Georg Solti")

percentage = score/5 * 100
print(f"Your success percentage was {percentage}%!")
#End Of Quiz

