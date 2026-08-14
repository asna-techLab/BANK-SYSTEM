
import psycopg

def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="bank_system",
        user="postgres",
        password="12345678",
        port=5432
    )