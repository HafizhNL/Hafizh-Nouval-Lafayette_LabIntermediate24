secret_word = "kronos"
long_word = len(secret_word)

for i in range(long_word):
    guess = input("Enter a word: ")
    if len(guess) > 1:
        print("Must input one word, Try Again!")
        break
    if guess.isalpha() == False:
        print("Must be a word, Try Again!")
        break
    if guess == secret_word[i]:
        print("Correct!")
    else:
        print("Incorrect!")
        

