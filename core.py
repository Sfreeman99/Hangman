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


class Hangman:
    def __init__(self, answer, guesses_left, guessed_letters):
        self.answer = answer
        self.guesses_left = guesses_left
        self.guessed_letters = guessed_letters

    def guess_letter(self, letter):
        self.guessed_letters.add(letter)
        if letter not in self.answer:
            self.guesses_left -= 1

    def guess_view(self):
        return [
            l if l in self.guessed_letters or l == ' ' else None
            for l in self.answer
        ]
