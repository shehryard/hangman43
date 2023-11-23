import random

create_word_list = ["pineapple", "mango", "watermelon", "cherry", "strawberry"]

class Hangman:
    def __init__(self, create_word_list, num_lives=5):
        self.create_word_list = create_word_list
        self.num_lives = num_lives
        self.select_random_word_from_list = random.choice(create_word_list)
        self.word_guessed = ['_' for _ in self.select_random_word_from_list]
        self.num_letters = len(set(self.select_random_word_from_list))  #using set to get unique letters
        self.list_of_guesses = []
        self.word_found = False  # Add a flag to track if the word has been found
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.select_random_word_from_list:
            for i in range(len(self.select_random_word_from_list)):
                if self.select_random_word_from_list[i] == guess:
                    self.word_guessed[i] = guess
            print(f"Good guess! '{guess}' is in the word. Word Guessed: {' '.join(self.word_guessed)}")
            self.num_letters -= 1  # Reduce the variable num_letters by 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again. Word Guessed: {' '.join(self.word_guessed)}")
            print(f"You have {self.num_lives} lives left.")
        
        if '_' not in self.word_guessed:  # Check if all letters have been guessed
            self.word_found = True

    def ask_for_input(self):
        while True:
            guess = input("Please enter your single letter guess: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                if self.word_found:  # Check if the word has been found
                    break
            
            if self.num_lives == 0:  # Added this as without it I was not getting the 'You lost' message and the loop continued asking for input. Thus this check was added as it checks if the user lost during the input process.
                break
                
    @staticmethod
    def play_game(create_word_list):
        num_lives = 5
        game = Hangman(create_word_list, num_lives)

        while True:
            if game.num_lives == 0:
                print("You lost!")
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break

Hangman.play_game(create_word_list)