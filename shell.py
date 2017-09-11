import core, random, getpass, disk


def options():
    while True:
        options = input('Would you like to make a phrase?\n[Y/N]\n: ').upper()
        if options == 'Y':
            phrase = getpass.getpass('Create Phrase: ')
            return phrase
        elif options == 'N':
            phrases = disk.read()
            phrases = core.phrases(phrases)
            difficult = difficulty(phrases)
            return difficult
        else:
            print('Invalid Choice... Please Try again')


def difficulty(phrase):
    while True:
        level = input('Difficulty: \n\t-Easy\n\t-Medium\n\t-Hard\n: ').lower()
        if level == 'easy':
            return random.choice(phrase['Easy'])
        elif level == 'medium':
            return random.choice(phrase['Medium'])
        elif level == 'hard':
            return random.choice(phrase['Hard'])
        else:
            print('Invalid Choice... Please Try again')


def main():
    print('Welcome to Hangman')
    phrase = options()
    print('Selecting a phrase')
    game = core.Hangman(phrase)
    print(' '.join(game.underlined_phrase))
    while True:
        current_guess = input('Guess: ')
        print(game.guess(current_guess))
        boolean, message = game.gameover()

        if boolean != True:
            continue
        elif boolean == True:
            break

    print(message)


if __name__ == '__main__':
    main()