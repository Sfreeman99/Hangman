import random


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
    def __init__(self, answer):
        self.answer = list_iteration(answer)
        self.guesses = set()
        self.tries = 5
        self.underlined_phrase = underline(self.answer)

    def guess(self, current_guess):
        if current_guess in self.guesses:
            return 'You already guessed that'
        elif (current_guess.lower() in self.answer) or (
                current_guess.upper() in self.answer):
            self.guesses.add(current_guess)
            change = [(indx, value) for indx, value in enumerate(self.answer)
                      if (current_guess.upper() == value) or (
                          current_guess.lower() == value)]
            for index, l in change:
                self.underlined_phrase.insert(index, l)
                self.underlined_phrase.pop(index + 1)
            message = 'There are {} {}(\'s)\n {}'.format(
                self.answer.count(l.upper()) + self.answer.count(l.lower()),
                current_guess, ' '.join(self.underlined_phrase))
            return message
        else:
            self.tries -= 1
            self.guesses.add(current_guess)
            message = 'You guessed wrong.. {} tries left\n {} '.format(
                self.tries, ' '.join(self.underlined_phrase))
            return message

    def solve_puzzle(self, phrase):
        if phrase.upper() == ''.join(self.answer).upper():
            message = 'That is it... You win!!!'
            boolean = True
            return boolean, message
        self.tries -= 1
        boolean = False
        message = 'That is wrong.. Nice Try Though\n {} guesses left'.format(
            self.tries)
        return boolean, message

    def gameover(self, phrase):
        if self.tries == 0:
            boolean = True
            message = 'Game Over ... You lose'
            return boolean, message
        elif self.underlined_phrase == self.answer:
            boolean = True
            message = 'Game Over... You Win'
            return boolean, message

        else:
            boolean = False
            message = None
            return boolean, message


class WheelofForturne:
    def __init__(self, answer, current_player):
        self.answer = answer
        self.rounds = 0
        self.current_player = current_player

    def spin(self):
        choices = [1500, 500, 'Lose a Turn', 'Bankrupt', 200, 250, 10000]
        choice = random.choice(choices)
        return choice

    def solve_puzzle(self, phrase):
        if phrase.upper() == ' '.join(self.answer).upper():
            return True
        return False

    def turn(self, player):
        decision = input('{}.. What would you like to do'.format(player.name))
        if decision == 'Spin':
            luck = WheelofForturne.spin()
            if luck == 'Lose a Turn':
                return None
            elif luck == 'Bankrupt':
                player.score = 0
            else:
                g = input('Guess: ')
                return player.guess(g, luck)


class Player:
    def __init__(self, name):
        self.guesses = set()
        self.name = name
        self.score = 0

    def guess(self, current_guess, spin):
        if current_guess in self.guesses:
            message = 'You already guessed that'
        elif (current_guess.lower() in self.answer) or (
                current_guess.upper() in self.answer):
            self.guesses.add(current_guess)
            change = [(indx, value) for indx, value in enumerate(self.answer)
                      if (current_guess.upper() == value) or (
                          current_guess.lower() == value)]
            for index, l in change:
                self.underlined_phrase.insert(index, l)
                self.underlined_phrase.pop(index + 1)

            self.score += (
                self.answer.count(l.upper()) + self.answer.count(l.lower())
            ) * spin
            message = 'There are {} {}(\'s)\n Money: {}\n {}'.format(
                (self.answer.count(l.upper()) + self.answer.count(l.lower())),
                current_guess, self.score, ' '.join(self.underlined_phrase))
            return message
        else:
            message = '{} is not in the phrase'.format(current_guess)
            return message

    def __repr__(self):
        return 'Player({}, ${})'.format(self.name, self.score)

    def __str__(self):
        return 'Name: {} || Money: {}'.format(self.name, self.score)
