secret_word = "kronos"
long_word = len(secret_word)

for i in range(long_word):
    guess = input("Enter a letter: ")
    if len(guess) > 1:
        print("Your guess is too high")
        break
    if guess.isalpha() == False:
        print("Must be a letter")
        break
        