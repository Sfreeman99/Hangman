def underline(phrase):
    ''' str -> list

    Takes in a string and changes it into '__'

    >>> underline('Hello')
    ['__', '__', '__', '__', '__']
    >>> underline('Hello World')
    ['__', '__', '__', '__', '__', ' ', '__', '__', '__', '__', '__']
    '''
    result = []
    for i in phrase:
        if i == ' ':
            result.append(' ')
        else:
            result.append('__')
    return result


def list_iteration(phrase):
    ''' str -> list

    takes in a phrase and splits it up in a list

    >>> list_iteration('Hello')
    ['H', 'e', 'l', 'l', 'o']
    >>> list_iteration('Hello World')
    ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
    '''
    result = []
    for letters in phrase:
        result.append(letters)
    return result


def phrases(disk):
    ''' None -> Dict

    returns a list of phrases

    '''
    phrase = {'Easy': [], 'Medium': [], 'Hard': []}
    for item in disk:
        i = item.strip().split(' | ')
        phrase[i[0]].append(i[1])
    return phrase