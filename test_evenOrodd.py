from evenorodd import even_odd

def test_even():
    assert even_odd(18) == "The number is even"

def test_odd():
    assert even_odd(17) == "The number is odd"