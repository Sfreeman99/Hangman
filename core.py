def underline(phrase):
    ''' str -> Nonetype

    Takes in a string and changes it into '__'

    >>> underline('Hello')
    '__ __ __ __ __'
    >>> underline('Hello World')
    '__ __ __ __ __   __ __ __ __ __'
    '''
    result = []
    for i in phrase:
        if i == ' ':
            result.append(' ')
        else:
            result.append('__')
    return ' '.join(result)
