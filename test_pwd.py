from pwd import check_password_strength

def test_strong_password():
    assert check_password_strength("Amrutha123") == "Strong Password"

def test_short_password():
    assert check_password_strength("Ab12") == "Weak Password"

def test_no_uppercase():
    assert check_password_strength("amrutha123") == "Weak Password"

def test_no_lowercase():
    assert check_password_strength("AMRUTHA123") == "Weak Password"

def test_no_digit():
    assert check_password_strength("Amrutha") == "Weak Password"
