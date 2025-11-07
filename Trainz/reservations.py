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


def insert_reservation(reservation_id, lname, fname, age, selected_option, con):
    cur=con.cursor()
    cur.execute("INSERT INTO Reservations(user_id, lname, fname, age, selected_option) VALUES (?,?,?,?,?)", 
                (reservation_id, lname, fname, age, selected_option))
    con.commit()