# ddc_timekey_singleline.py
# Input prompt: "Enter Message:"
# Output single line: your msg: <DDC>~<DDMMYY> <HHMM>

from datetime import datetime

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def num_to_letter_mod26(n: int) -> str:
    v = n % 26
    return 'Z' if v == 0 else chr(ord('A') + v - 1)

def derive_key_from_now():
    dt = datetime.now()
    dd, mm, yy = dt.day, dt.month, dt.year % 100
    hh, minute = dt.hour, dt.minute
    sum_date = sum(int(ch) for ch in f"{dd:02d}{mm:02d}{yy:02d}")
    letters = [
        num_to_letter_mod26(sum_date),
        num_to_letter_mod26(mm),
        num_to_letter_mod26(dd),
        num_to_letter_mod26(hh),
        num_to_letter_mod26(minute),
    ]
    ts_ddmmyy = dt.strftime("%d%m%y")
    ts_hhmm = dt.strftime("%H%M")
    return "".join(letters), ts_ddmmyy, ts_hhmm

def expand_key_for_alpha(text, key):
    alpha_count = sum(c.isalpha() for c in text)
    if alpha_count == 0:
        return ""
    out = list(key)
    while len(out) < alpha_count:
        out.append(key[len(out) % len(key)])
    return "".join(out)

def vigenere_encrypt(text, key):
    enc, k = [], expand_key_for_alpha(text, key)
    i = 0
    for ch in text:
        if ch.isalpha():
            p = ord(ch.upper()) - ord('A')
            s = ord(k[i].upper()) - ord('A')
            enc.append(chr(ord('A') + (p + s) % 26))
            i += 1
        else:
            enc.append(ch)
    return "".join(enc)

def text_to_morse(text):
    return ' '.join(morse_code_dict.get(ch.upper(), '') for ch in text)

def morse_to_ddc(morse):
    return morse.replace('.', '1').replace('-', '0')

def main():
    plaintext = input("Enter Message: ")
    key5, ts_ddmmyy, ts_hhmm = derive_key_from_now()
    v_encrypted = vigenere_encrypt(plaintext, key5)
    morse = text_to_morse(v_encrypted)
    ddc = morse_to_ddc(morse)
    print(f"your msg: {ddc}~{ts_ddmmyy} {ts_hhmm}")

if __name__ == "__main__":
    main()
