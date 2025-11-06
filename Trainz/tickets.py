#TICKETS.PY IS FOR THE DATABASE
#FOR CODE, SEE TICKET.PY

#following tutorial mentioned in iteration3
import sqlite3
con = sqlite3.connect("trainz.db") #creates our trainz db
c = con.cursor()

#Create
c.execute("""
CREATE TABLE IF NOT EXISTS Tickets(
          ticket_id TEXT PRIMARY KEY,
          user_id TEXT NOT NULL,
          reservation_id TEXT NOT NULL,)
          """)


con.commit()

res = c.execute("" \
"SELECT name FROM sql WHERE name='Tickets': ")
print("Table- this is a test- table exists", res.fetchone())

def insert_ticket(ticket_id, user_id, reservation_id)
    con = sqlite3.connect("trainz.db")
    c=con.cursor()
    cur.execute("""
        INSERT INTO Tickets VALUES (?, ?, ?)
    """, (ticket_id, user_id, reservation_id))
    con.commit()
    con.close())