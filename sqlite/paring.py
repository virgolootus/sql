import sqlite3
import csv




def connect_to_database():
    # loome ühenduse andmebaasiga
    file = 'C:/sqlite/epood_vlootus.db'
    con = sqlite3.connect(file)
    return con

def add_car():
    # funktsioon, mis võimaldab lisada andmeid vlootus tabelisse
    con = connect_to_database()
    cur = con.cursor()
    ees = input("Sisesta eesnimi: ")
    pere = input("Sisesta perenimi: ")
    email = input("Sisesta email: ")
    mark = input("Sisesta auto mark: ")
    model = input("Sisesta auto mudel: ")
    year = int(input("Sisesta auto aasta: "))
    price = int(input("Sisesta auto hind: "))
    cur.execute("INSERT INTO vlootus(ees_nimi,pere_nimi,email,car_make,car_model,car_year,car_price) VALUES (?, ?, ?, ?, ?, ?, ?)", (ees, pere, email, mark, model, year, price))
    con.commit()
    con.close()
    print("Andmed on lisatud!")

def get_older_cars():
    # funktsioon, mis tagastab vanemad autod kui 2000 aasta, sorteeritud aasta järgi tõusvas järjekorras
    con = connect_to_database()
    cur = con.cursor()
    cur.execute("SELECT * FROM vlootus WHERE car_year < 2000 ORDER BY car_year ASC LIMIT 100")
    rows = cur.fetchall()
    con.close()
    for a in rows:
        print(a)

def get_avg_year_and_max_price():
    # funktsioon, mis tagastab keskmise autode aasta ja kõige kallima hinna ühes reas
    con = connect_to_database()
    cur = con.cursor()
    cur.execute("SELECT AVG(car_year), MAX(car_price) FROM vlootus")
    row = cur.fetchone()
    con.close()
    for a in row:
        print(a)
      

def get_latest_cars():
    # funktsioon, mis tagastab 5 kõige uuemat automarki kood mudeliga
    con = connect_to_database()
    cur = con.cursor()
    cur.execute("SELECT car_make, car_model, car_year FROM vlootus ORDER BY car_year DESC LIMIT 5")
    rows = cur.fetchall()
    con.close()
    for a in rows:
        print(a)

def get_most_expensive_cars():
    # funktsioon, mis tagastab 5 kõige kallimat valitud automarki, sorteeritud perenime järgi
    markk = input("Sisesta auto mark: ")
    con = connect_to_database()
    cur = con.cursor()
    cur.execute("SELECT * FROM vlootus WHERE car_make=? ORDER BY car_price DESC, car_model ASC LIMIT 5", (markk,))
    rows = cur.fetchall()
    con.close()
    for a in rows:
        print(a)



def delete_cars():
    # funktsioon, mis võimaldab kustutada ridu, kus autode aasta jääb alla 2000 ja kindla margi järgi
    mark1 = input("Sisesta auto mark: ")
    
    con = connect_to_database()
    cur = con.cursor()
    cur.execute("DELETE FROM vlootus WHERE car_year < 2000 AND car_make=?", (mark1,))
    con.commit()
    con.close()
    print("Andmed on kustutatud!")

def export_to_csv():
    # funktsioon, mis ekspordib kõik andmed CSV faili
    con = connect_to_database

print("                                     MENU                                     ")
print("------------------------------------------------------------------------------")
print("1. Lisa andmebaasi uus auto                      5. Kuva 5 kõige kallimat autot\n2. Kuva autod mis on 20. sajandist               6. Kustuta vanu autosid\n3. Kuva keskmine autode aasta ja kalleim hind    7. Salvesta andmebaas CSV failina\n4. Kuva 5 kõige uuemat autot")
print(" ")
while True:
    valik = int(input("Vali funktsiooni number, mida soovid kasutada: "))
    if valik == 1:
        add_car()
    if valik == 2:
        get_older_cars()
    if valik == 3:
        get_avg_year_and_max_price()
    if valik == 4:
        get_latest_cars()
    if valik == 5:
        get_most_expensive_cars()
    if valik == 6:
        delete_cars()
    if valik == 7:
        export_to_csv()
    else:
        print("Vali number, mis on menüüs välja toodud!")