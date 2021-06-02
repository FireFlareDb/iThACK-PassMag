import sqlite3
import os

def create_dbtables():
    conn = sqlite3.connect(r"Password_Manager/User/leveldb/user.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS UserDataBase
         (ID                INTEGER          PRIMARY KEY,
         Website            CHAR(50)         Null,
         URL                TEXT(500)        NOT NULL,
         Username           CHAR(50)         NULL,
         Email              CHAR(50)         NOT NULL,
         Password           TEXT(200)        NOT NULL,
         Description        TEXT(5000));''')


    cur.execute('''CREATE TABLE IF NOT EXISTS UserDataBase_Encryption
         (Identification    INTEGER          Not Null,
          Encryption        CHAR(5000)       Not Null);''')

    conn.commit()
    conn.close()

def create_database():
    if os.path.exists("Password_Manager/User/leveldb"):
        if not os.path.exists("Password_Manager/User/leveldb/user.db"):
            sqlite3.connect(r"Password_Manager/User/leveldb/user.db")
            create_dbtables()
    else:
        os.mkdir("Password_Manager/User/leveldb")
        sqlite3.connect(r"Password_Manager/User/leveldb/user.db")
        create_dbtables()

def connect_database():
    connection = sqlite3.connect(r"Password_Manager/User/leveldb/user.db")
    return connection

if __name__ == '__main__':
    create_database()