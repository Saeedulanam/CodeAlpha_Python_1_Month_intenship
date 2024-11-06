import random

list_of_words = ["random" , "pandas" , "numpy" , "developer" , "duebugging" , "python" , "internship" , "algorithm"]


def hangman_guessing_words():
    PC_choice_random_word = random.choice(list_of_words)
    underscore_len_of_word = ["_"] * len(PC_choice_random_word)
    chance_limit = 5
    user_correct_letter_list = []

    print("Welcome Hangman!")
    print(" ".join(underscore_len_of_word))

    # Loop until the player runs out of attempts or guesses the word
    while chance_limit > 0:     
        user_guess_letter = input("Guess a letter: ").lower()

        if user_guess_letter in user_correct_letter_list:
            print("You already guessed that letter!")
            continue

        user_correct_letter_list.append(user_guess_letter)  # Add the new guess to the list of guessed letters

        if user_guess_letter in PC_choice_random_word:
            # Show the letters that the player guessed correctly in the hidden word
            for i , input_letter in enumerate(PC_choice_random_word):   # Loop over each letter in the word
                if input_letter == user_guess_letter:
                    underscore_len_of_word[i] = user_guess_letter # Replace underscores with the correctly guessed letter

            print("Good Guess: " , " ".join(underscore_len_of_word))

        else:
            chance_limit -= 1
            print(f"Wrong guess! you have {chance_limit} attempts left")

        if "_" not in underscore_len_of_word:
            print("Congriculation! You have successfully guess: " , PC_choice_random_word)
            break

    else:
        print("You have run out of attempts , the word was: " , PC_choice_random_word)


hangman_guessing_words()

