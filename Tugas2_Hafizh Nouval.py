secret_word = "kronok"
guessed_letters = set()
hidden_word = ["_"] * len(secret_word)
attempts = 6

while "_" in hidden_word and attempts > 0:
    print("\nWord: ", "".join(hidden_word))
    print(f"Attempts left: {attempts}")
    user_input = input("Input a letter: ").lower()

    if len(user_input) != 1 or not user_input.isalpha():
        print("Must input a single letter")
        continue
    if user_input in guessed_letters:
        print("You already guessed that letter")
        continue

    guessed_letters.add(user_input)

    if user_input in secret_word:
        for i, letter in enumerate(secret_word):
            if letter == user_input:
                hidden_word[i] = user_input
    else:
        attempts -= 1
        print("Incorrect!")

if "_" not in hidden_word:
    print(f"Congratulations, Secret word: {secret_word}")
else:
    print(f"Game over! The secret word was: {secret_word}")
