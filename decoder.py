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

reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_decrypt(text, key):
    decrypted_text = []
    key = generate_key(text, key)
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = (ord(char.upper()) - ord(key[key_index].upper()) + 26) % 26
            decrypted_char = chr(shift + ord('A'))
            # Preserve original casing
            if char.islower():
                decrypted_char = decrypted_char.lower()
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            decrypted_text.append(char)
    return "".join(decrypted_text)

def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    decoded_text = ''
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(reverse_morse_code_dict.get(letter, '') for letter in letters)
        decoded_text += decoded_word + ' '
    return decoded_text.strip()

def convert_binary_to_morse(binary_code):
    return binary_code.replace('1', '.').replace('0', '-')

# Input binary and key
binary_code = input("Decryption: ")
key = input("Key: ")

# Convert binary to Morse code
morse_code = convert_binary_to_morse(binary_code)
print(f'Morse Code: {morse_code}')

# Convert Morse code to text
morse_text = morse_to_text(morse_code)
print(f'Morse Decoded Text: {morse_text}')

# Decrypt the text using Vigenère cipher
decrypted_text = vigenere_decrypt(morse_text, key)
print(f'Vigenère Decrypted Text: {decrypted_text}')

input("press enter: ")

