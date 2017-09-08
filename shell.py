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
    chosen_phrase = phrase
    correct_answer = core.list_iteration(chosen_phrase)
    underlined_phrase = core.underline(chosen_phrase)
    print(' '.join(underlined_phrase))
    limit = 5
    # This is how to check if your answer has been selected already
    guesses = set()
    while limit != 0:
        print('{} guesses left'.format(limit))
        decision = input('Guess: ')
        if decision in guesses:
            print('You already chose that... try again')
            continue
        print('You selected {}'.format(decision))
        guesses.add(decision)

        if (decision.lower() in correct_answer) or (
                decision.upper() in correct_answer):
            change = [
                (indx, value) for indx, value in enumerate(correct_answer)
                if (decision.upper() == value) or (decision.lower() == value)
            ]
            # change = []
            # for indx, value in enumerate(correct_answer):
            #     if decision.lower() == value.lower():
            #         change.append((indx, decision))

            for index, l in change:
                underlined_phrase.insert(index, l)
                underlined_phrase.pop(index + 1)
            if correct_answer == underlined_phrase:
                break
            print(' '.join(underlined_phrase))
        else:
            print('Wrong')
            limit -= 1
            print(' '.join(underlined_phrase))

    if limit == 0:
        print('Gameover You lose')
        print('Answer: \n{}'.format(chosen_phrase))

    else:
        print('You win!!!')


if __name__ == '__main__':
    main()