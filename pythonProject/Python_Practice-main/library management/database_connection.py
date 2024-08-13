import mysql.connector
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aravi@123*",
            database="library"
        )
        if connection.is_connected():
            return connection
    except Exception as e:
        print(f"Error in connecting: {e}")
        return None
