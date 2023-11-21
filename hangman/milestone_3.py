import random
create_word_list = ["pineapple", "mango", "watermelon", "cherry", "strawberry"]
select_random_word_from_list = random.choice(create_word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in select_random_word_from_list:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please enter your single letter guess: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

    check_guess(guess)

ask_for_input()
