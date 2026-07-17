import secrets
import string


def get_password_length():
    while True:
        raw_input_value = input("Enter desired password length (15-64 recommended): ").strip()

        if not raw_input_value.isdigit():
            print("❌ Please enter a valid whole number.\n")
            continue

        length = int(raw_input_value)

        if length < 4:
            print("❌ Length too short to be usable. Try at least 4.\n")
            continue

        if length < 15:
            print("⚠️  Warning: NIST 2024 guidelines recommend 15+ characters for high-security use.")

        if length > 64:
            print("❌ Length too long. Max supported is 64 characters.\n")
            continue

        return length


def generate_password(length, use_letters=True, use_digits=True, use_symbols=False):
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character set must be selected.")

    password = "".join(secrets.choice(char_pool) for _ in range(length))
    return password


def calculate_entropy(length, pool_size):
    import math
    return round(length * math.log2(pool_size), 2)


def main():
    print("=" * 50)
    print(" DecodeLabs — Enterprise Random Password Generator")
    print("=" * 50)

    length = get_password_length()

    include_symbols = input("Include special symbols (@, #, $, etc.)? (y/n): ").strip().lower() == "y"

    password = generate_password(length, use_letters=True, use_digits=True, use_symbols=include_symbols)

    pool_size = len(string.ascii_letters) + len(string.digits)
    if include_symbols:
        pool_size += len(string.punctuation)

    entropy = calculate_entropy(length, pool_size)

    print("\n✅ Your generated password:")
    print(f"   {password}")
    print(f"\n🔐 Estimated entropy: {entropy} bits")
    if entropy >= 80:
        print("   Strength: Excellent — resistant to modern cracking techniques.")
    elif entropy >= 60:
        print("   Strength: Good.")
    else:
        print("   Strength: Weak — consider increasing length.")


if __name__ == "__main__":
    main()
