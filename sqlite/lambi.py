import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *


# ühendus andmebaasiga
conn = sqlite3.connect('epood_vlootus.db')
cur = conn.cursor()

# päringu käivitamine andmebaasi kõigi ridade lugemiseks
cur.execute("SELECT * FROM vlootus")
data = cur.fetchall()

# tabeli veergude loomine
columns = [
    {"text": "id", "stretch": False},
    {"text": "Eesnimi", "stretch": True},
    {"text": "Perenimi", "stretch": True},
    {"text": "Email", "stretch": True},
    {"text": "Auto mark", "stretch": True},
    {"text": "Auto mudel", "stretch": True},
    {"text": "Auto aasta", "stretch": True},
    {"text": "Auto hind", "stretch": True},
]

# tabeli ridade loomine
rows = []
for row in data:
    rows.append(row)

# loome peamise akna
my_w = ttk.Window()
my_w.geometry("800x500")

# loome tabeli
my_w.style.theme_use("cyborg")
table = Tableview(
    master=my_w,
    coldata=columns,
    rowdata=rows,
    paginated=True,  # lehekülgede jagamine
    pagesize=10,  # ridade arv ühel lehel
    height=10,  # tabeli kõrgus
    stripecolor=(my_w.style.colors.dark, None),
    searchable=True,  # otsingu võimalus
    bootstyle="darkly",  # ttkbootstrap dark_theme
)
table.autofit_columns()
table.grid(row=0, column=0, padx=10, pady=5)

# loome nupu uue rea lisamiseks
def add_row():
    def save_data():
        # võtame väljade sisestatud väärtused
        eesnimi = eesnimi_entry.get()
        perenimi = perenimi_entry.get()
        email = email_entry.get()
        mark = mark_entry.get()
        mudel = mudel_entry.get()
        aasta = aasta_entry.get()
        hind = hind_entry.get()

        # lisame andmed tabelisse
        cur.execute("INSERT INTO vlootus (ees_nimi, pere_nimi, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (eesnimi, perenimi, email, mark, mudel, aasta, hind))
        conn.commit()
        update_table()
        # sulgeme lisamisakna
        add_window.destroy()

    # loome uue akna lisamiseks
    add_window = ttk.Toplevel(my_w)
    add_window.title("Lisa uus rida")

    # lisame väljad andmete sisestamiseks
    eesnimi_label = ttk.Label(add_window, text="Eesnimi")
    eesnimi_entry = ttk.Entry(add_window)
    perenimi_label = ttk.Label(add_window, text="Perenimi")
    perenimi_entry = ttk.Entry(add_window)
    email_label = ttk.Label(add_window, text="Email")
    email_entry = ttk.Entry(add_window)
    mark_label = ttk.Label(add_window, text="Auto mark")
    mark_entry = ttk.Entry(add_window)
    mudel_label = ttk.Label(add_window, text="Auto mudel")
    mudel_entry = ttk.Entry(add_window)
    aasta_label = ttk.Label(add_window, text="Auto aasta")
    aasta_entry = ttk.Entry(add_window)
    hind_label = ttk.Label(add_window, text="Auto hind")
    hind_entry = ttk.Entry(add_window)

    eesnimi_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    eesnimi_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    perenimi_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    perenimi_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    mark_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    mark_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    mudel_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    mudel_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
    aasta_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    aasta_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
    hind_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    hind_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w") 
    save_button = ttk.Button(add_window, text="Salvesta", command=save_data)
    save_button.grid(row=7, column=0, padx=5, pady=5, columnspan=2)
add_row_button = ttk.Button(
    my_w,
    text="Lisa uus rida",
    command=add_row,
    style="secondary.TButton",
)
add_row_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# loome funktsiooni andmete uuendamiseks
def update_table():
    cur.execute("SELECT * FROM vlootus")
    new_data = cur.fetchall()
    table.rowdata = new_data


# alustame rakendust
my_w.mainloop()

# suletakse andmebaasi ühendus
conn.close()
