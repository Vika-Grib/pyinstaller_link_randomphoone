import tkinter as tk
import random

entry_count = 0
last_entered_link = ""

def generate_phone_number():
    link = link_entry.get()
    if link:
        prefix = "+375 ("
        operator = random.choice(["29", "44", "33", "25"])
        prefix += operator + ") "

        number = ''.join(random.choice("123456789") for _ in range(1))
        number += ''.join(random.choice("0123456789") for _ in range(2))
        number += " - " + ''.join(random.choice("0123456789") for _ in range(2))
        number += " - " + ''.join(random.choice("0123456789") for _ in range(2))

        phone_number.set(prefix + number)

        # Update statistics internally
        update_statistics(link)
    else:
        phone_number.set("Please enter a link first")

def update_statistics(link):
    global entry_count, last_entered_link
    entry_count += 1
    last_entered_link = link
    print(f"Link entered: {link}, Entry count: {entry_count}")

def main():
    window = tk.Tk()
    window.title("Phone Number Generator")

    # размер окна и расположение его в центре экрана
    window.geometry("400x200+400+200")

    # подложка
    padding = 10

    label = tk.Label(window, text="Enter Internet Link:")
    label.pack()

    global link_entry
    link_entry = tk.Entry(window)
    link_entry.pack(pady=padding)

    generate_button = tk.Button(window, text="Generate", command=generate_phone_number)
    generate_button.pack()

    global phone_number
    phone_number = tk.StringVar()
    phone_number_label = tk.Label(window, textvariable=phone_number)
    phone_number_label.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
