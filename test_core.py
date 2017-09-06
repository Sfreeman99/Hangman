import core


def test_underline_with_one_word():
    phrase = 'Hello'
    assert core.underline(phrase) == '__ __ __ __ __'
    assert core.underline('Goodbye') == '__ __ __ __ __ __ __'
    assert core.underline('a') != '__ '