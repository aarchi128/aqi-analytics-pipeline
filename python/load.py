import mysql.connector
import config

def get_connection():
    return mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DATABASE
    )

def insert_data(df):
    """Insert cleaned DataFrame rows into stations and readings tables."""
    conn = get_connection()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        # Check if station exists
        check_query = "SELECT station_id FROM stations WHERE station_name = %s AND city = %s"
        cursor.execute(check_query, (row["station"], row["city"]))
        result = cursor.fetchone()

        if result:
            station_id = result[0]
        else:
            insert_station_query = """
                INSERT INTO stations (station_name, city, state, country, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_station_query, (
                row["station"], row["city"], row["state"], row["country"],
                row["latitude"], row["longitude"]
            ))
            station_id = cursor.lastrowid

        insert_reading_query = """
            INSERT IGNORE INTO readings (station_id, pollutant_id, min_value, max_value, avg_value, last_update)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_reading_query, (
            station_id, row["pollutant_id"], row["min_value"], row["max_value"],
            row["avg_value"], row["last_update"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted successfully")