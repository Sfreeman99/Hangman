import core, random, getpass, disk


def main():
    decision = input(
        'What would you like to play? \n\t-Hangman\n\t-Wheel of Fortune\n: '
    ).upper()
    if decision == 'HANGMAN':
        print(hangman_main())
    else:
        print(wheel_main())


def wheel_main():
    return 'In Progress... Please try again later'


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


def hangman_main():
    print('Welcome to Hangman')
    phrase = options()
    print('Selecting a phrase')
    game = core.Hangman(phrase)
    print(' '.join(game.underlined_phrase))
    while True:
        current_guess = input('Guess: ')
        print(game.guess(current_guess))
        boolean, message = game.gameover(phrase)
        if boolean == True:
            break
        decision = input('\nwould you like to solve? \n[Y/N}\n:').upper()
        if decision == 'Y':
            solve = input('What is it: ')
            boolean, message = game.solve_puzzle(solve)
            if boolean == True:
                break
            print(message)
            continue
        elif decision == 'N':
            continue

    if boolean == True:
        return message
    elif solve_phrase == True:
        return message


if __name__ == '__main__':
    main()