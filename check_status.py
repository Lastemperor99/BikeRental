import sqlite3

def check_rental_status():
    conn = sqlite3.connect('bike_rental.db')
    cursor = conn.cursor()

    # Query to retrieve user names, bike names, and statuses
    cursor.execute("SELECT zone, name, bike_name, status FROM bikes WHERE status='rented'")
    rented_bikes = cursor.fetchall()

    conn.close()

    if not rented_bikes:
        print("No bikes are currently rented.")
    else:
        print("Rental Status by Zone:")
        zone_status = {}  # To store status by zone
        for zone, user, bike, status in rented_bikes:
            if zone not in zone_status:
                zone_status[zone] = []
            zone_status[zone].append(f"User: {user}, Bike: {bike}, Status: {status}")

        for zone, status_list in zone_status.items():
            print(f"Zone {zone}:")
            for status in status_list:
                print(status)

if __name__ == "__main__":
    check_rental_status()

