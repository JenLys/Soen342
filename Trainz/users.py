from user import User

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

def insert_user(user_id, lname, fname, age, con):
    cur=con.cursor()
    cur.execute("INSERT INTO Users(user_id, lname, fname, age) VALUES (?,?,?,?)", (user_id, lname, fname, age))
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