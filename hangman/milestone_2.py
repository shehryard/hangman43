import random
create_word_list = ["pineapple", "mango", "watermelon", "cherry", "strawberry"]
print(create_word_list)
select_random_word_from_list = random.choice(create_word_list)
print(select_random_word_from_list)

guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")