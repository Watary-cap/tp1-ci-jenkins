from app import addition

def test_addition_positive():
    assert addition(2, 3) == 5

def test_addition_negative():
    assert addition(-1, -2) == -3