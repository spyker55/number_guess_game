import random

def new_game():
    print("Welcome the Number Guess Game!")
    print("Guess a number in 1 and 100!")

    computer_number = random.randint(1, 100)

    game_range_for = 0
    game_range = input("Type 'easy' (10 tips) or 'hard' (5 tips) for level: ")

    if game_range == "easy":
        game_range_for = 11
    elif game_range == "hard":
        game_range_for = 6
    else:
        print("Invalid level chosen, please try again!")
        new_game()
    
    def game_over():
        """Ended the game"""
        continue_game = input("Would you like another game? 'y'-yes, 'n'-no: ")
        if continue_game == "y":
            new_game()
        else:
            quit()

    i = 1
    for i in range(game_range_for):
        i += 1
        if i == game_range_for:
            print(f"Not enough tips! My number was {computer_number}!")
            game_over()
        else:
            range_1 = 1 
            range_2 = 100
            tip = int(input("What is your tip? "))
            if tip == computer_number:
                print("You win!")
                game_over()
            elif tip < computer_number:
                range_1 == tip
                print("My number is bigger.")
            elif tip > computer_number:
                range_2 == tip
                print("My number is smaller.")
            else:
                print(f"You lost! My number was {computer_number}!")
                game_over()

new_game()
