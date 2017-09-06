import core, random


def underline(phrase):
    ''' str -> Nonetype

    Takes in a string and changes it into '__'

    >>> underline('Hello')
    '__ __ __ __ __'
    '''
    return ('__ ' * len(phrase)).strip()


print('Welcome to Hangman')
phrases = ['Hello', 'Good', 'Shedlia']
current_phrase = random.choice(phrases)
print(current_phrase)
print(underline(current_phrase))
