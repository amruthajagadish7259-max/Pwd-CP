def check_password_strength(password):
    if len(password) < 8:
        return "Weak Password"

    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"


if __name__ == "__main__":
    # Sample input
    password = "Amrutha123"

    print(check_password_strength(password))