def displayWord(chosenWord, guessedLetters):
    word = ""
    numberofDashes = 0
    for letter in chosenWord:
        if (letter in guessedLetters):
            word = word + letter + ""
            numberofDashes = numberofDashes
            print(word)
            return numberofDashes

            myList = ['Ronaldo', 'Messi', 'Yuvraj', 'Dance']
            chosenWord = random.choice(mylist)

            guessedLetters = []
            guess = 7
            numberofDashes = displayWord(chosenWor, guessedLetter)

            while (guess > 0):
                letter = (input("guess a letter. You have " +
                                str(guess) + " left.")).lower()
                if (letter in chosenWord):
                    guessedLetters.append(letter)
                else:
                    guess = guess - 1
                    numberofDashes = dispalyWord(chosenWord, guessedletters)
                    if (numberofDashes == 0):
                        print("You won. The word was " + chosenWord)
                        break

                        displayWord();



