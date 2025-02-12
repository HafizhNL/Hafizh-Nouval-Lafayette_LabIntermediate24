def hangman(secret_word):
    guessed_letters = set()
    remaining_chances = 6
    
    while remaining_chances > 0:
        text = ""
        for char in secret_word:
            if char in guessed_letters:
                text += char + " "
            else:
                text += "_ "
        
        print(f"Word: {text.strip()}")
        print(f"Remaining chances: {remaining_chances}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) < 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetic character.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"'{guess}' is not in the word. Try again.")
            remaining_chances -= 1
        
        if all(char in guessed_letters for char in secret_word):
            print(f"Congratulations! You've successfully guessed the word: {secret_word}")
            return
        
    print(f"Game over! The word was: {secret_word}")

hangman("indonesia")