# Load Database Pkg
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()


# Fxn
# track_utils.py

import sqlite3

def get_connection():
    connection = sqlite3.connect('your_database.db')
    return connection

def create_page_visited_table():
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS page_visited (pagename TEXT, time_of_visit TIMESTAMP)')
        connection.commit()

def add_page_visited_details(pagename, time_of_visit):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO page_visited (pagename, time_of_visit) VALUES (?, ?)', (pagename, time_of_visit))
        connection.commit()

def view_all_page_visited_details():
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM page_visited')
        return cursor.fetchall()

def create_emotionclf_table():
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS emotion_prediction (raw_text TEXT, prediction TEXT, probability REAL, time_of_visit TIMESTAMP)')
        connection.commit()

def add_prediction_details(raw_text, prediction, probability, time_of_visit):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO emotion_prediction (raw_text, prediction, probability, time_of_visit) VALUES (?, ?, ?, ?)', (raw_text, prediction, probability, time_of_visit))
        connection.commit()

def view_all_prediction_details():
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM emotion_prediction')
        return cursor.fetchall()
import sqlite3
from datetime import datetime

import sqlite3

def create_stress_level_table():
    conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with the name of your SQLite database file
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stressLevelTable (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT,
                    stress_level INTEGER,
                    timestamp DATETIME)''')
    conn.commit()
    conn.close()

def add_stress_level_details(text, stress_level, timestamp):
    conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with the name of your SQLite database file
    c = conn.cursor()
    c.execute("INSERT INTO stressLevelTable (text, stress_level, timestamp) VALUES (?, ?, ?)", (text, stress_level, timestamp))
    conn.commit()
    conn.close()
