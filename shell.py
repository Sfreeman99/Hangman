def underline(phrase):
    ''' str -> Nonetype

    Takes in a string and changes it into '__'

    >>> underline('Hello')
    '__ __ __ __ __'
    '''
    return ('__ ' * len(phrase)).strip()


print('Welcome to Hangman')
phrases = ['Hello']
print(current_phrase)
