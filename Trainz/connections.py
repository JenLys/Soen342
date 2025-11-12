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