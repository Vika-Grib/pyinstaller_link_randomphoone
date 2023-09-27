import tkinter as tk
import random

def generate_phone_number():
    prefix = "+375 ("
    operator = random.choice(["29", "44", "33", "25"])
    prefix += operator + ") "

    number = ''.join(random.choice("123456789") for _ in range(1))
    number += ''.join(random.choice("0123456789") for _ in range(2))
    number += " - " + ''.join(random.choice("0123456789") for _ in range(2))
    number += " - " + ''.join(random.choice("0123456789") for _ in range(2))

    phone_number.set(prefix + number)

def main():
    window = tk.Tk()
    window.title("Phone Number Generator")

    label = tk.Label(window, text="Enter Internet Link:")
    label.pack()

    link_entry = tk.Entry(window)
    link_entry.pack()

    generate_button = tk.Button(window, text="Generate", command=generate_phone_number)
    generate_button.pack()

    global phone_number
    phone_number = tk.StringVar()
    phone_number_label = tk.Label(window, textvariable=phone_number)
    phone_number_label.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
