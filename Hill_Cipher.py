import tkinter as tk
from tkinter import messagebox

def get_x(n, m):
    for x in range(m):
        if (n * x) % m == 1:
            return x
    raise ValueError("Key matrix is not appropriate")

def un_hill_cipher(ciphertext, key_matrix, key_matrix_3):
    ciphertext_nums = [ord(c) - 65 for c in ciphertext.upper()]

    if len(ciphertext_nums) % 2 != 0:
        cipher_matrix_3 = [[ciphertext_nums[i], ciphertext_nums[i + 1], ciphertext_nums[i + 2]] for i in range(0, 3, 3)]
        cipher_matrix_2 = [[ciphertext_nums[i], ciphertext_nums[i + 1]] for i in range(3, len(ciphertext_nums), 2)]

        key_matrix = [[int(key_matrix[0][0]), int(key_matrix[0][1])], [int(key_matrix[1][0]), int(key_matrix[1][1])]]
        det_key_matrix_2 = int(key_matrix[0][0]) * int(key_matrix[1][1]) - int(key_matrix[0][1]) * int(key_matrix[1][0])
        gx_2 = get_x(det_key_matrix_2, 26)
        key_matrix_beta_2 = [[int(key_matrix[1][1]) * gx_2, (26 - int(key_matrix[0][1])) * gx_2],
                             [(26 - int(key_matrix[1][0])) * gx_2, int(key_matrix[0][0]) * gx_2]]

        key_matrix_3 = [[int(key_matrix_3[0][0]), int(key_matrix_3[0][1]), int(key_matrix_3[0][2])],
                        [int(key_matrix_3[1][0]), int(key_matrix_3[1][1]), int(key_matrix_3[1][2])],
                        [int(key_matrix_3[2][0]), int(key_matrix_3[2][1]), int(key_matrix_3[2][2])]]
        a = key_matrix_3[0][0]
        b = key_matrix_3[0][1]
        c = key_matrix_3[0][2]
        d = key_matrix_3[1][0]
        e = key_matrix_3[1][1]
        f = key_matrix_3[1][2]
        g = key_matrix_3[2][0]
        h = key_matrix_3[2][1]
        i = key_matrix_3[2][2]
        det_key_matrix_3 = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
        gx_3 = get_x(det_key_matrix_3 % 26, 26)

        a1 = ((e * i) - (h * f))
        b1 = -((b * i) - (c * h))
        c1 = ((b * f) - (e * c))
        d1 = -((d * i) - (g * f))
        e1 = ((a * i) - (g * c))
        f1 = -((a * f) - (d * c))
        g1 = ((d * h) - (g * e))
        h1 = -((a * h) - (g * b))
        i1 = ((a * e) - (d * b))

        key_matrix_3[0][0] = (gx_3 * (a1 % 26)) % 26
        key_matrix_3[0][1] = (gx_3 * (b1 % 26)) % 26
        key_matrix_3[0][2] = (gx_3 * (c1 % 26)) % 26
        key_matrix_3[1][0] = (gx_3 * (d1 % 26)) % 26
        key_matrix_3[1][1] = (gx_3 * (e1 % 26)) % 26
        key_matrix_3[1][2] = (gx_3 * (f1 % 26)) % 26
        key_matrix_3[2][0] = (gx_3 * (g1 % 26)) % 26
        key_matrix_3[2][1] = (gx_3 * (h1 % 26)) % 26
        key_matrix_3[2][2] = (gx_3 * (i1 % 26)) % 26

        UNciphertext_matrix_3 = []
        for block in cipher_matrix_3:
            UNciphertext_block = [
                (block[0] * key_matrix_3[0][0] + block[1] * key_matrix_3[0][1] + block[2] * key_matrix_3[0][2]) % 26,
                (block[0] * key_matrix_3[1][0] + block[1] * key_matrix_3[1][1] + block[2] * key_matrix_3[1][2]) % 26,
                (block[0] * key_matrix_3[2][0] + block[1] * key_matrix_3[2][1] + block[2] * key_matrix_3[2][2]) % 26]
            UNciphertext_matrix_3.append(UNciphertext_block)

        UNciphertext_matrix_2 = []
        for block in cipher_matrix_2:
            UNciphertext_block = [(block[0] * key_matrix_beta_2[0][0] + block[1] * key_matrix_beta_2[0][1]) % 26,
                                  (block[0] * key_matrix_beta_2[1][0] + block[1] * key_matrix_beta_2[1][1]) % 26]
            UNciphertext_matrix_2.append(UNciphertext_block)

        UNciphertext_2 = ''.join([chr(num + 65) for block in UNciphertext_matrix_2 for num in block])
        UNciphertext_3 = ''.join([chr(num + 65) for block in UNciphertext_matrix_3 for num in block])

        UNciphertext = UNciphertext_3 + UNciphertext_2

    else:
        ciphertext_nums = [ord(c) - 65 for c in ciphertext.upper()]
        ciphertext_matrix = [[ciphertext_nums[i], ciphertext_nums[i + 1]] for i in range(0, len(ciphertext_nums), 2)]

        key_matrix = [[int(key_matrix[0][0]), int(key_matrix[0][1])], [int(key_matrix[1][0]), int(key_matrix[1][1])]]
        det_key_matrix = int(key_matrix[0][0]) * int(key_matrix[1][1]) - int(key_matrix[0][1]) * int(key_matrix[1][0])
        gx = get_x(det_key_matrix, 26)
        key_matrix_beta = [[int(key_matrix[1][1]) * gx, (26 - int(key_matrix[0][1])) * gx],
                           [(26 - int(key_matrix[1][0])) * gx, int(key_matrix[0][0]) * gx]]

        cipher_betatext_matrix = []
        for block in ciphertext_matrix:
            cipher_betatext_block = [(block[0] * key_matrix_beta[0][0] + block[1] * key_matrix_beta[0][1]) % 26,
                                     (block[0] * key_matrix_beta[1][0] + block[1] * key_matrix_beta[1][1]) % 26]
            cipher_betatext_matrix.append(cipher_betatext_block)

        UNciphertext = ''.join([chr(num + 65) for block in cipher_betatext_matrix for num in block])

    return UNciphertext

def hill_cipher(plaintext, key_matrix, key_matrix_3):
    plaintext_nums = [ord(c) - 65 for c in plaintext.upper()]

    if len(plaintext_nums) % 2 != 0:
        plaintext_matrix_3 = [[plaintext_nums[i], plaintext_nums[i + 1], plaintext_nums[i + 2]] for i in range(0, 3, 3)]
        plaintext_matrix_2 = [[plaintext_nums[i], plaintext_nums[i + 1]] for i in range(3, len(plaintext_nums), 2)]

        key_matrix = [[int(key_matrix[0][0]), int(key_matrix[0][1])], [int(key_matrix[1][0]), int(key_matrix[1][1])]]
        key_matrix_3 = [[int(key_matrix_3[0][0]), int(key_matrix_3[0][1]), int(key_matrix_3[0][2])],
                        [int(key_matrix_3[1][0]), int(key_matrix_3[1][1]), int(key_matrix_3[1][2])],
                        [int(key_matrix_3[2][0]), int(key_matrix_3[2][1]), int(key_matrix_3[2][2])]]

        ciphertext_matrix_3 = []
        for block in plaintext_matrix_3:
            ciphertext_block = [
                (block[0] * key_matrix_3[0][0] + block[1] * key_matrix_3[0][1] + block[2] * key_matrix_3[0][2]) % 26,
                (block[0] * key_matrix_3[1][0] + block[1] * key_matrix_3[1][1] + block[2] * key_matrix_3[1][2]) % 26,
                (block[0] * key_matrix_3[2][0] + block[1] * key_matrix_3[2][1] + block[2] * key_matrix_3[2][2]) % 26]
            ciphertext_matrix_3.append(ciphertext_block)

        ciphertext_matrix_2 = []
        for block in plaintext_matrix_2:
            ciphertext_block = [(block[0] * key_matrix[0][0] + block[1] * key_matrix[0][1]) % 26,
                                (block[0] * key_matrix[1][0] + block[1] * key_matrix[1][1]) % 26]
            ciphertext_matrix_2.append(ciphertext_block)

        ciphertext_2 = ''.join([chr(num + 65) for block in ciphertext_matrix_2 for num in block])
        ciphertext_3 = ''.join([chr(num + 65) for block in ciphertext_matrix_3 for num in block])

        ciphertext = ciphertext_3 + ciphertext_2

    else:
        plaintext_matrix = [[plaintext_nums[i], plaintext_nums[i + 1]] for i in range(0, len(plaintext_nums), 2)]

        key_matrix = [[int(key_matrix[0][0]), int(key_matrix[0][1])], [int(key_matrix[1][0]), int(key_matrix[1][1])]]

        ciphertext_matrix = []
        for block in plaintext_matrix:
            ciphertext_block = [(block[0] * key_matrix[0][0] + block[1] * key_matrix[0][1]) % 26,
                                (block[0] * key_matrix[1][0] + block[1] * key_matrix[1][1]) % 26]
            ciphertext_matrix.append(ciphertext_block)

        ciphertext = ''.join([chr(num + 65) for block in ciphertext_matrix for num in block])

    return ciphertext

def encrypt():
    key_matrix = []
    key_matrix_3 = []

    try:
        for i in range(2):
            row = [int(x) for x in key_matrix_entries[i].get().split()]
            if len(row) != 2:
                raise ValueError
            key_matrix.append(row)

        for i in range(3):
            row = [int(x) for x in key_matrix_3_entries[i].get().split()]
            if len(row) != 3:
                raise ValueError
            key_matrix_3.append(row)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid key matrix values. Please enter integers.")
        return

    plaintext = plaintext_entry.get().upper()
    if not plaintext.isalpha():
        messagebox.showerror("Input Error", "Plaintext must contain only alphabetic characters.")
        return

    ciphertext = hill_cipher(plaintext, key_matrix, key_matrix_3)
    ciphertext_label.config(text="Ciphertext: " + ciphertext)

def decrypt():
    key_matrix = []
    key_matrix_3 = []

    try:
        for i in range(2):
            row = [int(x) for x in key_matrix_entries[i].get().split()]
            if len(row) != 2:
                raise ValueError
            key_matrix.append(row)

        for i in range(3):
            row = [int(x) for x in key_matrix_3_entries[i].get().split()]
            if len(row) != 3:
                raise ValueError
            key_matrix_3.append(row)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid key matrix values. Please enter integers.")
        return

    ciphertext = ciphertext_label.cget("text").split(": ")[1]
    if not ciphertext.isalpha():
        messagebox.showerror("Input Error", "Ciphertext must contain only alphabetic characters.")
        return

    unciphertext = un_hill_cipher(ciphertext, key_matrix, key_matrix_3)
    unciphertext_label.config(text="Unciphertext: " + unciphertext)

root = tk.Tk()
root.title("Hill Cipher")

# Key Matrix 2x2
tk.Label(root, text="Enter 2x2 key matrix:").grid(row=0, column=0, columnspan=2)
key_matrix_entries = []
for i in range(2):
    entry = tk.Entry(root, width=10)
    entry.grid(row=i+1, column=0, columnspan=2)
    key_matrix_entries.append(entry)

# Key Matrix 3x3
tk.Label(root, text="Enter 3x3 key matrix:").grid(row=3, column=0, columnspan=3)
key_matrix_3_entries = []
for i in range(3):
    entry = tk.Entry(root, width=15)
    entry.grid(row=i+4, column=0, columnspan=3)
    key_matrix_3_entries.append(entry)

# Plaintext Entry
tk.Label(root, text="Enter plaintext:").grid(row=7, column=0)
plaintext_entry = tk.Entry(root)
plaintext_entry.grid(row=7, column=1)

# Encrypt and Decrypt Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=8, column=0)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=8, column=1)

# Result Labels
ciphertext_label = tk.Label(root, text="Ciphertext: ")
ciphertext_label.grid(row=9, column=0, columnspan=2)

unciphertext_label = tk.Label(root, text="Unciphertext: ")
unciphertext_label.grid(row=10, column=0, columnspan=2)

root.mainloop()
