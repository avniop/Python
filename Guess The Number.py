import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Welcome to Guess the Number!")
    player_name = input("What is your name? ")
    want_to_play = input("Hi {}, would you like to play the game? (Enter Yes/No) ".format(player_name))
    show_score()
    attempts = 0
    while want_to_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            attempts += 1
            if int(guess) == random_number:
                print("Nice! You got it in {} attempts".format(attempts))
                attempts_list.append(attempts)
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                show_score()
                attempts = 0
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That's cool, have a good day!")
                    break
            elif int(guess) > random_number:
                print("It's lower")
            elif int(guess) < random_number:
                print("It's higher")
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good day!")
if __name__ == '__main__':
    start_game()