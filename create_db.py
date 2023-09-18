import sqlite3

conn = sqlite3.connect('bike_rental.db')
cursor = conn.cursor()

# Create a table to store bike information along with user names and zone information
cursor.execute('''
CREATE TABLE bikes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    bike_name TEXT,
    city TEXT,
    zone TEXT,
    status TEXT
)
''')

# Insert sample data for each city and zone combination
cities = ['City1', 'City2', 'City3']  # Add your cities here
zones = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']

for city in cities:
    for zone in zones:
        for i in range(1, 11):
            cursor.execute("INSERT INTO bikes (name, bike_name, city, zone, status) VALUES (?, ?, ?, ?, ?)",
                           (None, f'Bike{i}', city, zone, 'available'))

conn.commit()
conn.close()
