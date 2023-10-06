# -*- coding: utf-8 -*-
import tkinter as tk
import random
import validators
import googletrans
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


entry_count = 0
last_entered_link = ""

name_list = []

def generate_name():
    global name_list
    with open('names.txt', 'r', encoding='utf-8') as file:
        text_names = file.readlines()
        for name in text_names:
            name_list.append(name[:-1])


    name = random.choice(name_list)
    print('Рандомное имя: ', name)
    return name

def generate_mail(name):
    prefix_list = ['mail', 'gmail', 'yandex', 'yahoo', 'vk']
    domen_list = ['com', 'by', 'ru', 'org']
    num = 1900 + random.randrange(64, 100)
    sym_list = 'qwertyuiopasdfghjklzxcvbnm'
    sym = random.choice(sym_list)
    translater = googletrans.Translator()
    translated_name = translater.translate(name)
    # print(translated_name.text)
    mail = translated_name.text + sym.upper() + str(num) + '@' + random.choice(prefix_list) + '.' + random.choice(domen_list)
    return mail


def open_link(name, mail, phone):
    global last_entered_link
    print(last_entered_link)

    o = Options()
    o.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=o)
    driver.get(last_entered_link)
    driver.maximize_window()
    user_name = driver.find_element(By.NAME, 'Name')
    user_mail = driver.find_element(By.NAME, 'Email')
    user_phone = driver.find_element(By.NAME, 'tildaspec-phone-part[]')
    user_name.send_keys(name)
    user_mail.send_keys(mail)
    user_phone.send_keys(phone)


def generate_phone_number():
    link = link_entry.get()
    check = check_link(link)
    if check:
        prefix = "+375 ("
        operator = random.choice(["29", "44", "33", "25"])
        prefix += operator + ") "
        if operator == '29':
            number = ''.join(random.choice("123456789") for _ in range(1))
        else:
            number = ''.join(random.choice("0123456789") for _ in range(1))
        number += ''.join(random.choice("0123456789") for _ in range(2))
        number += " - " + ''.join(random.choice("0123456789") for _ in range(2))
        number += " - " + ''.join(random.choice("0123456789") for _ in range(2))

        phone_number.set(prefix + number)

        # информация по подсчету количества вводов ссылочки
        update_statistics(link)

        name = generate_name()
        open_link(name, generate_mail(name), operator + number)
        return prefix + number
    else:
        phone_number.set("Please enter a link first")



def check_link(link):
    global last_entered_link
    if link.startswith("www"):
        link = link.replace('www.', 'http://')

    if validators.url(link):
        last_entered_link = link
        return True
    else:
        return False

def update_statistics(link):
    global entry_count
    entry_count += 1
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
