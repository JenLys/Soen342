#TICKETS.PY IS FOR THE DATABASE
#FOR CODE, SEE TICKET.PY

#following tutorial mentioned in iteration3
import sqlite3

def init_tickets_table(): #if not created, init
    con = sqlite3.connect("trainz.db")#creates our trainz db
    cur=con.cursor()
    #cur.execute("PRAGMA foreign_keys = ON;")
    #Create ***UPDATE FOREIGN ONCE USER AND RESERVATION TABLES CREATED
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
    #cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("""INSERT INTO Tickets(ticket_id, user_id, reservation_id)
                VALUES (?,?,?)""", (ticket_id, user_id, reservation_id))
    con.commit()
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
