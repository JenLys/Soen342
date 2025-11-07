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

def insert_trip(trip_id, user_id, reservation_id, reservation_list, con):
    cur=con.cursor()
    cur.execute("INSERT INTO Trips(trip_id, user_id, reservation_id, reservation_list) VALUES (?,?,?,?)", 
                (trip_id, user_id, reservation_id, reservation_list))
    con.commit()