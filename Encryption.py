# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # Space between words in Morse code is represented by '/'
}

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(text, key):
    encrypted_text = []
    key = generate_key(text, key)
    key_index = 0
    for char in text:
        if char.isalpha():
            # Encrypt the character
            x = (ord(char.upper()) + ord(key[key_index].upper())) % 26
            x += ord('A')
            encrypted_text.append(chr(x))
            key_index += 1
        else:
            # Preserve non-alphabet characters
            encrypted_text.append(char)
    return "".join(encrypted_text)

def text_to_morse(text):
    # Replace each letter in text with its Morse code equivalent
    morse_code = ' '.join(morse_code_dict.get(char.upper(), '') for char in text)
    return morse_code

def convert_morse_to_binary(morse_code):
    # Replace '.' with '1' and '-' with '0'
    binary_code = morse_code.replace('.', '1').replace('-', '0')
    return binary_code

# Input text and key
text = input("Encryption: ")
key = input("Key: ")

# Encrypt the text using Vigenère cipher
encrypted_text = vigenere_encrypt(text, key)
print(f'Vigenère Encrypted Text: {encrypted_text}')

# Convert the encrypted text to Morse code
morse_code = text_to_morse(encrypted_text)
print(f'Morse Code: {morse_code}')

# Convert the Morse code to binary
binary_code = convert_morse_to_binary(morse_code)
print(f'DDC: {binary_code}')

input("press enter: ")