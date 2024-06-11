import tkinter as tk

from cipher.encrypt import encrypt
from cipher.decrypt import decrypt

root = tk.Tk()
root.title("Lesego's Cipher")

# Text encryption/decryption
main_frame = tk.Frame(root)
main_frame.pack(pady=10)

input_label = tk.Label(main_frame, text="Enter message:")
input_label.pack()

input_text = tk.Text(main_frame, height=12, width=60)
input_text.pack()

encrypt_button = tk.Button(main_frame, text="Encrypt", command=lambda: encrypt(input_text, output_text))
encrypt_button.pack()

decrypt_button = tk.Button(main_frame, text="Decrypt", command=lambda: decrypt(input_text, output_text))
decrypt_button.pack()

output_label = tk.Label(main_frame, text="Encrypted/Decrypted message:")
output_label.pack()

output_text = tk.Text(main_frame, height=12, width=60)
output_text.pack()

root.mainloop()