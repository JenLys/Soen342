#TICKETS.PY IS FOR THE DATABASE
#FOR CODE, SEE TICKET.PY

#following tutorial mentioned in iteration3
import sqlite3
from user import User

def init_tables(con):
    init_users_table(con)
    init_reservations_table(con)
    init_trips_table(con)
    init_tickets_table(con)

def init_users_table(con):
    cur=con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Users(
                user_id VARCHAR(20) PRIMARY KEY,
                lname VARCHAR(20) NOT NULL,
                fname VARCHAR(20) NOT NULL,
                age int NOT NULL
                );""")
    con.commit()

def init_reservations_table(con):
    cur=con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Reservations(
                reservation_id VARCHAR(20) PRIMARY KEY,
                lname VARCHAR(20) NOT NULL,
                fname VARCHAR(20) NOT NULL,
                age int NOT NULL,
                selected_option VARCHAR(10) NOT NULL
                );""")
    con.commit()
    
def init_trips_table(con):
    cur=con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Trips(
                trip_id VARCHAR(20) PRIMARY KEY,
                user_id VARCHAR(20) NOT NULL,
                reservation_id VARCHAR(20) NOT NULL,
                reservation_list TEXT,
                FOREIGN KEY (user_id) REFERENCES Users(user_id),
                FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
                );""")
    con.commit()

def init_tickets_table(con):
    cur=con.cursor()
    #cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Tickets(
        ticket_id VARCHAR(20) PRIMARY KEY,
        user_id VARCHAR(20) NOT NULL,
        reservation_id VARCHAR(20) NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
    );""")
    con.commit()

def init_connections_table(con):
    cur=con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Connections(
        route_id VARCHAR(6) PRIMARY KEY,
        dep_city VARCHAR(20),
        arr_city VARCHAR(20),
        dep_time VARCHAR(20),
        arr_time VARCHAR(20),
        train_type VARCHAR(20),
        days_of_op VARCHAR(20),
        fclass_rate FLOAT,
        sclass_rate FLOAT   
                );""")
    con.commit()

def insert_user(user_id, lname, fname, age, con):
    cur=con.cursor()
    cur.execute("INSERT INTO Users(user_id, lname, fname, age) VALUES (?,?,?,?)", (user_id, lname, fname, age))
    con.commit()

def insert_reservation(reservation_id, lname, fname, age, selected_option, con):
    cur=con.cursor()
    cur.execute("INSERT INTO Reservations(user_id, lname, fname, age, selected_option) VALUES (?,?,?,?,?)", 
                (reservation_id, lname, fname, age, selected_option))
    con.commit() 

def insert_trip(trip_id, user_id, reservation_id, reservation_list, con):
    cur=con.cursor()
    cur.execute("INSERT INTO Trips(trip_id, user_id, reservation_id, reservation_list) VALUES (?,?,?,?)", 
                (trip_id, user_id, reservation_id, reservation_list))
    con.commit()

def insert_ticket(ticket_id, user_id, reservation_id, con):
    cur=con.cursor()
    #cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("""INSERT INTO Tickets(ticket_id, user_id, reservation_id)
                VALUES (?,?,?)""", (ticket_id, user_id, reservation_id))
    con.commit()

def find_user(user_id, con):
    cur = con.cursor()
    cur.execute("SELECT * FROM Users WHERE user_id = :user_id", {"user_id": user_id})

    user_data = cur.fetchone()

    if user_data == None:
        return None

    return User(user_data[1], user_data[2], user_data[0], user_data[3])

def show_all_users(con):
    cur = con.cursor()

    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()

    if len(rows) == 0:
        print("Users table is empty.")
        return
    
    user_list = []

    for row in rows:
        user_list.append(User(row[1], row[2], row[0],row[3]))

    for user in user_list:
        print(user)

    con.close()

#to test out if the table got created properly. Add show_after_insert=False parameter in insert_ticket(...), set it to True in bookingDB.py
def show_all_tickets():
    import sqlite3
    con = sqlite3.connect("trainz.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM Tickets")
    rows = cur.fetchall()

    if rows:
        print("All tickets in the database:")
        for row in rows:
            print(row)
    else:
        print("Tickets table is empty.")

    con.close()
