from reservation import Reservation

def init_reservations_table(con):
    cur=con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Reservations(
                reservation_id VARCHAR(20) PRIMARY KEY,
                lname VARCHAR(20) NOT NULL,
                fname VARCHAR(20) NOT NULL,
                age int NOT NULL,
                selected_option VARCHAR(10) NOT NULL,
                date VARCHAR(10) NOT NULL
                );""")
    con.commit()

def insert_reservation(res: Reservation, con):
    cur=con.cursor()
    cur.execute("INSERT INTO Reservations(reservation_id, lname, fname, age, selected_option, date) VALUES (?,?,?,?,?,?)", 
                (res.reservation_id, res.lname, res.fname, res.age, res.selected, res.date))
    con.commit()

def show_all_reservations(con):
    cur = con.cursor()

    cur.execute("SELECT * FROM Reservations")
    rows = cur.fetchall()

    if len(rows) == 0:
        print("Reservations table is empty.")
        return
    
    reservation_list = []

    for row in rows:
        reservation = Reservation(row[1], row[2], row[3], row[4], row[5])
        reservation.reservation_id = row[0]
        reservation_list.append(Reservation(row[1], row[2], row[3], row[4], row[5]))

    for reservation in reservation_list:
        print(reservation)