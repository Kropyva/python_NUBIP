import json
import http.client
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


## Update information
def update(first_part, second_part, country):
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "e18063930fmsh479c75bb05b434bp1e641bjsn49bf81d7ecdc",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()

    parsed_json = json.loads(data.decode("utf-8"))

    if first_part:
        list = []
        for i in parsed_json:
            list.append(i['Country'])
        return list

    if second_part:
        for i in parsed_json:
            if country in parsed_json[parsed_json.index(i)]["Country"]:
                stat_name(parsed_json[parsed_json.index(i)]["Country"]).grid(row=3,
                                                                             column=0, stick='wens', padx=5, pady=5)
                stat_name(parsed_json[parsed_json.index(i)]["TotalCases"]).grid(row=3,
                                                                                column=1, stick='wens', padx=5, pady=5)
                stat_name(parsed_json[parsed_json.index(i)]["TotalDeaths"]).grid(row=3,
                                                                                 column=2, stick='wens', padx=5, pady=5)
                stat_name(parsed_json[parsed_json.index(i)]["TotalRecovered"]).grid(row=3,
                                                                                    column=3, stick='wens', padx=5,
                                                                                    pady=5)
                stat_name(parsed_json[parsed_json.index(i)]["ActiveCases"]).grid(row=3,
                                                                                 column=4, stick='wens', padx=5, pady=5)
                stat_name(parsed_json[parsed_json.index(i)]["TotalTests"]).grid(row=3,
                                                                                column=5, stick='wens', padx=5, pady=5)
                stat_name("Country").grid(row=2, column=0, stick='wens', padx=5, pady=5)
                stat_name("Total Cases").grid(row=2, column=1, stick='wens', padx=5, pady=5)
                stat_name("Total Deaths").grid(row=2, column=2, stick='wens', padx=5, pady=5)
                stat_name("Total Recovered").grid(row=2, column=3, stick='wens', padx=5, pady=5)
                stat_name("Active Cases").grid(row=2, column=4, stick='wens', padx=5, pady=5)
                stat_name("Total Tests").grid(row=2, column=5, stick='wens', padx=5, pady=5)


## Operating functions
def enter_country():
    isTrue = True
    list = update(True, False, None)
    for i in list:
        if finder.get() == list[list.index(i)]:
            isTrue = False
            update(False, True, finder.get())
            finder.delete(0, tk.END)
    if isTrue:
        messagebox.showinfo("Attention!", "Wrong country!")
        finder.delete(0, tk.END)
        return


def press_key(event):
    if event.keycode == 13:
        enter_country()
    if event.keycode == 17:
        update(False, True, countries.get())
    if event.char.isdigit():
        finder.delete(0, tk.END)
    if event.char in '~₴!@"#№$;%^:&?/*()-_=+<,>.[{]}|\\\'':
        finder.delete(0, tk.END)


## Button functions
def make_update_button(name):
    return tk.Button(text=name, bd=10, font=('Helvetica', 14),
                     command=lambda: update(False, True, countries.get()))


def make_enter_button(name):
    return tk.Button(text=name, bd=10, font=('Helvetica', 14),
                     command=enter_country)


def stat_name(name):
    return Label(win, text=name, font=('Helvetica', 13, 'bold'), bg='#%02x%02x%02x' % (210, 230, 220))


## Window
win = tk.Tk()
win.geometry(f"1055x250")
win['bg'] = '#%02x%02x%02x' % (240, 240, 220)
win.minsize(1055, 250)
win.maxsize(1055, 250)
win.title('Covid Statistics')
win.bind('<Key>', press_key)

for i in range(0, 6):
    win.grid_columnconfigure(i, minsize=160)
    win.grid_rowconfigure(i + 1, minsize=60)

## Finder
finder = tk.Entry(win, justify=tk.RIGHT, font=('Helvetica', 20), width=39)
finder.grid(row=0, column=0, columnspan=6, stick='we', padx=5, pady=5)

## Combobox Build
countries = ttk.Combobox(win, font=("Courier", 14, "bold"), state='readonly')
countries['values'] = (update(True, False, None))
countries.current(0)

## Buttons and Combobox
make_update_button('Update').grid(row=1, column=1, columnspan=2, stick="wens", padx=5, pady=13)
make_enter_button('Enter').grid(row=1, column=4, columnspan=2, stick="wens", padx=5, pady=13)
countries.grid(row=1, column=0, stick='wens', padx=5, pady=13)

win.mainloop()
