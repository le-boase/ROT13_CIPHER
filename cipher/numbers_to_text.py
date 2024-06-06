# numbers_to_text.py
UPPERCASES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def numbers_to_text(numbers):
    text = ''
    for char in numbers:
        if char.isdigit():
            char_index = int(char)
            char_index = (char_index - 13) % 26
            if char_index < 0:
                char_index += 26
            text += UPPERCASES[char_index]
        else:
            text += char
    return text