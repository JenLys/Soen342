#TICKETS.PY IS FOR THE DATABASE
#FOR CODE, SEE TICKET.PY

#following tutorial mentioned in iteration3
import sqlite3
con = sqlite3.connect("trainz.db") #creates our trainz db
cur = con.cursor()

#Create ***UPDATE FOREIGN ONCE USER AND RESERVATION TABLES CREATED
# cur.execute("PRAGMA foreign_keys = ON;") #sets foreign key
cur.execute("""
CREATE TABLE IF NOT EXISTS Tickets(
          ticket_id TEXT PRIMARY KEY,
          user_id TEXT NOT NULL,
          reservation_id TEXT NOT NULL)
          """) #USER ID AND RESERVATION ID MUST BE CREATED AS TABLES ALREADY--- THEY ARE FOREIGN KEYS. CAN'T CALL THEM FOREIGN KEYS IF TABLES AREN'T CREATED YET

#updated code with foreign:
'''CREATE TABLE IF NOT EXISTS Tickets(
    ticket_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    reservation_id TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
)'''


con.commit()
con.close()

def insert_ticket(ticket_id, user_id, reservation_id):
    con=sqlite3.connect("trainz.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO Tickets(ticket_id, user_id, reservation_id)
                VALUES (?,?,?)""", (ticket_id, user_id, reservation_id))
    con.commit()
    con.close()


def insert_ticket(ticket_id, user_id, reservation_id):
    con = sqlite3.connect("trainz.db")
    c=con.cursor()
    cur.execute("""
        INSERT INTO Tickets VALUES (?, ?, ?)
    """, (ticket_id, user_id, reservation_id))
    con.commit()
    con.close()

