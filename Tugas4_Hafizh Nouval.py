import random

secret_words = ["indonesia", "python", "programming", "hangman", "university"]

wins = 0
losses = 0

def hangman_game():
    global wins, losses, secret_words
    while secret_words:
        secret_word = random.choice(secret_words)
        secret_words.remove(secret_word)
        
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
                wins += 1
                break
        
        if remaining_chances == 0:
            print(f"Game over! The word was: {secret_word}")
            losses += 1
        
        print(f"Score: Wins - {wins}, Losses - {losses}")

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != "y":
            break
    
    print(f"Final Score: Wins - {wins}, Losses - {losses}")
    print("Thank you for playing!")

hangman_game()
