from trip import Trip

def init_trips_table(con):
    cur=con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Trips(
                trip_id VARCHAR(20) PRIMARY KEY,
                user_id VARCHAR(20) NOT NULL,
                reservation_list TEXT,
                current BOOLEAN,
                FOREIGN KEY (user_id) REFERENCES Users(user_id),
                FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
                );""")
    con.commit()

def find_past_trips(user_id, con):
    cur=con.cursor()
    cur.execute("SELECT * FROM Trips WHERE user_id = :user_id AND current = FALSE", {"user_id": user_id})
    rows = cur.fetchAll()

    past_trips = []
    
    for row in rows:
        trip = Trip(row[0], row[1], row[2], row[3])
        past_trips.append(trip)

    return past_trips

def find_current_trips(user_id, con):
    cur=con.cursor()
    cur.execute("SELECT * FROM Trips WHERE user_id = :user_id AND current = TRUE", {"user_id": user_id})
    rows = cur.fetchAll()

    current_trips = []
    
    for row in rows:
        trip = Trip(row[0], row[1], row[2], row[3])
        current_trips.append(trip)

    return current_trips

def find_trips(user_id, con):
    cur=con.cursor()
    cur.execute("SELECT * FROM Trips WHERE user_id = :user_id", {"user_id": user_id})
    rows = cur.fetchAll()

    past_trips = []
    
    for row in rows:
        trip = Trip(row[0], row[1], row[2], row[3])
        past_trips.append(trip)

    return past_trips

def insert_trip(trip, con):
    cur=con.cursor()
    cur.execute("INSERT INTO Trips(trip_id, user_id, reservation_id, reservation_list, current) VALUES (?,?,?,?,?)", 
                (trip.trip_id, trip.user_id, trip.reservation_id, trip.reservation_list, trip.current))
    con.commit()