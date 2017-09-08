import core, random


def options():
    options = input('Would you like to make a phrase?\n[Y/N]').upper()
    if options == 'Y':
        phrase = [input('Create Phrase: ')]
        return phrase
    elif options == 'N':
        phrases = [
            'This is easy', 'Another random phrase',
            'Peter Piper Picked a peck of Pickled Peppers',
            'Beating a Dead Horse'
        ]
        return phrases


def main():
    print('Welcome to Hangman')
    phrase = options()
    print('Selecting a phrase')
    chosen_phrase = random.choice(phrase)
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

        if decision in correct_answer:
            change = [(indx, value)
                      for indx, value in enumerate(correct_answer)
                      if decision.lower() == value.lower()]
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
    if limit == 0:
        print('Gameover You lose')

    else:
        print(' '.join(underlined_phrase))
        print('You win!!!')


if __name__ == '__main__':
    main()