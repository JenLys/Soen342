#TICKETS.PY IS FOR THE DATABASE
#FOR CODE, SEE TICKET.PY

#following tutorial mentioned in iteration3
import sqlite3
from user import User

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

def insert_ticket(ticket, con):
    cur=con.cursor()
    #cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("""INSERT INTO Tickets(ticket_id, user_id, reservation_id)
                VALUES (?,?,?)""", (ticket.ticket_id, ticket.user_id, ticket.reservation_id))
    con.commit()

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
