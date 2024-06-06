import pyperclip
import tkinter as tk


UPPERCASES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASES = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'

def encrypt(input_text, output_text):
    message = input_text.get("1.0", "end-1c")


    translated = ''
    for char in message:
        if char.isupper():
            translated_char_index = (UPPERCASES.find(char) + 13) % 26
            translated += UPPERCASES[translated_char_index]
        elif char.islower():
            translated_char_index = (LOWERCASES.find(char) + 13) % 26
            translated += LOWERCASES[translated_char_index]
        elif char.isdigit():
            translated_char_index = (NUMBERS.find(char) + 13) % 10
            translated += NUMBERS[translated_char_index]
        else:
            translated += char

    output_text.delete("1.0", "end")
    output_text.insert("1.0", translated)

    try:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass