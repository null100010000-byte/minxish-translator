# Mapping dictionary for the cipher
CIPHER_MAP = {
    'a': 'Chinga', 'b': 'Chong', 'c': 'Ching', 'd': 'Cheng',
    'e': 'Chinge', 'f': 'Fing', 'g': 'Guangdong', 'h': 'Hong',
    'i': 'Yi', 'j': 'Jiang', 'k': 'Kong', 'l': 'Long',
    'm': 'Ming', 'n': 'Nigga', 'o': 'Osaka', 'p': 'Penis',
    'q': 'Qidong', 'r': 'Rice', 's': 'Suck', 't': 'Trachea',
    'u': 'Underwear', 'v': 'Vietnam', 'w': 'Wongwenxi', 'x': 'Xray',
    'y': 'Yotta', 'z': 'Zebrawoman', ' ': '-'
}

# Reverse mapping for decoding (Cipher word -> Letter)
REVERSE_MAP = {v.lower(): k for k, v in CIPHER_MAP.items()}


def encrypt_sentence(sentence):
    """Converts English text into the cipher words."""
    # Maps each character; if not found, it keeps the original character
    return " ".join(CIPHER_MAP.get(char, char) for char in sentence.lower())


def decode_description(encoded_text):
    """Converts the cipher words back into English."""
    words = encoded_text.split()
    decoded_result = ""
    for word in words:
        clean_word = word.lower()
        # Appends the character if found, otherwise keeps the word as-is
        decoded_result += REVERSE_MAP.get(clean_word, word)
    return decoded_result


def main():
    while True:
        print("\n" + "=" * 40)
        print("   Mingish Translator")
        print("=" * 40)
        print("1. English -> Mingish")
        print("2. Mingish -> English")
        print("3. Exit")

        choice = input("\nSelect(1-3): ")

        if choice == '1':
            text = input("Translate into Mingish: ")
            result = encrypt_sentence(text)
            print(f"\n[Encrypted Result]: {result}")

        elif choice == '2':
            text = input("Translate into English (space-separated): ")
            result = decode_description(text)
            print(f"\n[Decrypted Result]: {result}")

        elif choice == '3':
            print("Exiting the program. Get out")
            break

        else:
            print("Please enter 1, 2, or 3 u retard.")


if __name__ == "__main__":
    main()