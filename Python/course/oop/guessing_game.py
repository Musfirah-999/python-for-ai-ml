import random

class GuessingGame:
    def __init__(self):
        self.__secret = random.randint(1,100)
        self.__attempts = 0
        
    def check_guess(self, guess):
        self.__attempts+=1
        if guess > self.__secret:
            
            return "Too High!!"
        
        if guess < self.__secret:
            
            return "Too low!!"
        else:
            return "Correct!"
        
    def get_attempts(self):
        return self.__attempts
    def reset_game(self):
        self.__secret = random.randint(1,100)
        self.__attempts = 0
        

game = GuessingGame()
print(f"--------WELCOME---------")
while True:
    guess = int(input(f"Guess a number between 1 to 100:"))
    result = game.check_guess(guess)
    print(result)
    if result == "Correct!":
        print(f"Attepmts: {game.get_attempts()}")
        play_again = input("Do you want to play again? (y/n):")
        if play_again == "y":
             game.reset_game()
        else:
            break
           

        
        