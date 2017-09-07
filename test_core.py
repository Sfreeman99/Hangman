import core


def test_underline_with_one_word():
    phrase = 'Hello'
    assert ' '.join(core.underline(phrase)) == '__ __ __ __ __'
    assert ' '.join(core.underline('Goodbye')) == '__ __ __ __ __ __ __'
    assert ' '.join(core.underline('a')) != '__ '


def test_underline_with_a_phrase():
    phrase = 'This is a phrase'
    assert ' '.join(core.underline(
        phrase)) == '__ __ __ __   __ __   __   __ __ __ __ __ __'

    assert core.underline('Hello World') != '__ __ __ __ __ __ __ __ __ __ __'


def test_spliting_word():
    word = 'Hello'
    assert core.list_iteration(word) == ['H', 'e', 'l', 'l', 'o']
    assert core.list_iteration('Goodbye') == [
        'G', 'o', 'o', 'd', 'b', 'y', 'e'
    ]
