import sqlite3
import tkinter as tk
from tkinter import ttk

def rent_bike():
    # Retrieve user input
    user_name = name_entry.get()
    selected_area = area_combobox.get()

    # Query the database for available bikes in the selected zone
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()
    cursor.execute("SELECT bike_name FROM bikes WHERE zone=? AND status='available'", (selected_area,))
    available_bikes = cursor.fetchall()

    if not available_bikes:
        message_label.config(text="No bikes available in this zone.")
    else:
        selected_bike = available_bikes[0][0]  # Assuming the user selects the first available bike
        message_label.config(text=f"Hi {user_name}, you've rented {selected_bike}. Enjoy your ride!")

        # Update the bike status to 'rented' and store the user's name
        cursor.execute("UPDATE bikes SET status='rented', name=? WHERE bike_name=?", (user_name, selected_bike))
        conn.commit()

    conn.close()


# Create the main window
window = tk.Tk()
window.title("Bike Rental App")

# Create and pack widgets
name_label = tk.Label(window, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

area_label = tk.Label(window, text="Select area:")
area_label.pack()

areas = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']
area_combobox = ttk.Combobox(window, values=areas)
area_combobox.pack()

rent_button = tk.Button(window, text="Rent Bike", command=rent_bike)
rent_button.pack()

message_label = tk.Label(window, text="")
message_label.pack()

window.mainloop()
