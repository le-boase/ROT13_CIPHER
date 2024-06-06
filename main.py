
import tkinter as tk

from cipher.encrypt import encrypt
from cipher.decrypt import decrypt
from cipher.text_to_numbers import cipher_text_to_numbers
from cipher.numbers_to_text import numbers_to_text





root = tk.Tk()
root.title("Lesego's Cpiher")

# Text encryption/decryption
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10)

input_label = tk.Label(left_frame, text="Enter message:")
input_label.pack()

input_text = tk.Text(left_frame, height=5, width=40)
input_text.pack()




encrypt_button = tk.Button(left_frame, text="Encrypt", command=lambda: encrypt(input_text, output_text))
encrypt_button.pack()

decrypt_button = tk.Button(left_frame, text="Decrypt", command=lambda: decrypt(input_text, output_text))
decrypt_button.pack()

output_label = tk.Label(left_frame, text="Encrypted/Decrypted message:")
output_label.pack()

output_text = tk.Text(left_frame, height=5, width=40)
output_text.pack()


def convert_to_numbers():
    message = numbers_input_text.get("1.0", "end-1c")
    converted_text = cipher_text_to_numbers(message)
    numbers_output_text.delete("1.0", "end")
    numbers_output_text.insert("1.0", converted_text)

def convert_from_numbers():
    numbers = numbers_input_text.get("1.0", "end-1c")
    converted_text = numbers_to_text(numbers)
    numbers_output_text.delete("1.0", "end")
    numbers_output_text.insert("1.0", converted_text)


# Convert to/from numbers
right_frame = tk.Frame(root)
right_frame.pack(side=tk.LEFT, padx=10)

numbers_input_label = tk.Label(right_frame, text="Enter message or numbers:")
numbers_input_label.pack()

numbers_input_text = tk.Text(right_frame, height=5, width=40)
numbers_input_text.pack()

numbers_rotation_label = tk.Label(right_frame, text="Enter rotation value:")
numbers_rotation_label.pack()

numbers_rotation_entry = tk.Entry(right_frame)
numbers_rotation_entry.pack()



convert_button = tk.Button(right_frame, text="Convert to Numbers", command=lambda: convert_to_numbers())
convert_button.pack()

convert_from_button = tk.Button(right_frame, text="Convert from Numbers", command=lambda: convert_from_numbers())
convert_from_button.pack()

numbers_output_label = tk.Label(right_frame, text="Converted message/numbers:")
numbers_output_label.pack()

numbers_output_text = tk.Text(right_frame, height=5, width=40)
numbers_output_text.pack()

root.mainloop()