import sqlite3
import psycopg2d

def create_table():
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("CREATE TABLE if NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

insert("coffee cup",10,6)

def view():
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM store")
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("DELETE FROM store where item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

delete("wine glass")

print(view())
