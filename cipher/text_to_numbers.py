# text_to_numbers.py
UPPERCASES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASES = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'

def cipher_text_to_numbers(text):
    translated = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                char_index = UPPERCASES.find(char)
                translated += str((char_index + 13) % 26)
            else:
                char_index = LOWERCASES.find(char)
                translated += str((char_index + 13) % 26)
        elif char.isdigit():
            char_index = NUMBERS.find(char)
            translated += NUMBERS[(char_index + 13) % 10]
        else:
            translated += char
    return translated