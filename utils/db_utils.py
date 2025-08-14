import sqlite3
import pandas as pd

DB_PATH = "db/restaurant.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT,
            category TEXT,
            price REAL,
            gst REAL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            mode TEXT,
            payment_method TEXT,
            subtotal REAL,
            gst REAL,
            discount REAL,
            total REAL,
            date_time TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            item_name TEXT,
            quantity INTEGER,
            price REAL
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_menu_from_csv(file_path="data/menu.csv"):
    df = pd.read_csv(file_path)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("menu", conn, if_exists="replace", index=False)
    conn.close()

def get_menu():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT item_name, price, gst FROM menu")
    rows = cursor.fetchall()
    conn.close()
    return rows
