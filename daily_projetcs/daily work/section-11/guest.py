
secret_word = "python"

guessed_letters = []


tries = 6


while tries > 0:

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)


    if display_word == secret_word:
        print("🎉 Congratulations! You guessed the word!")
        break


    guess = input("Guess a letter: ").lower()


    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue


    guessed_letters.append(guess)


    if guess in secret_word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print("❌ Wrong guess. Tries left:", tries)


if display_word != secret_word:
    print("Game Over! The word was:", secret_word)
