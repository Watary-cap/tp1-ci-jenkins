from app import addition

def test_addition_positive():
    assert addition(2, 3) == 5

def test_addition_negative():
    assert addition(-1, -2) == -3

    # Test des bords (zéro) [cite: 43, 45]
def test_addition_zero():
    assert addition(0, 0) == 0
    assert addition(5, 0) == 5

# Test des flottants [cite: 44, 47]
def test_addition_float():
    assert addition(2.5, 3.5) == 6.0