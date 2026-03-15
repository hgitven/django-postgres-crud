import psycopg2
import sys

def diagnostico():
    print("--- Iniciando Diagnóstico de PostgreSQL ---")
    
    config = {
        "dbname": "pv",
        "user": "postgres",
        "password": "postgre1.",
        "host": "127.0.0.1",
        "port": "5432"
    }

    try:
        print(f"Intentando conectar a {config['dbname']} en {config['host']}...")
        conn = psycopg2.connect(**config)
        print("¡CONEXIÓN EXITOSA!")
        
        cur = conn.cursor()
        cur.execute("SELECT version();")
        record = cur.fetchone()
        print(f"Estás conectado a: {record}")
        
        cur.close()
        conn.close()

    except Exception as error:
        print("\n[ERROR DETECTADO]")
        print(f"Tipo de error: {type(error).__name__}")
        print(f"Mensaje del error: {error}")
        
        if "authentication failed" in str(error):
            print("\nSugerencia: La contraseña 'postgre1.' no es correcta para el usuario 'postgres'.")
        elif "does not exist" in str(error):
            print("\nSugerencia: La base de datos 'pv' no existe. Créala con: CREATE DATABASE pv;")
        elif "connection refused" in str(error):
            print("\nSugerencia: El servicio de PostgreSQL no está corriendo o el puerto 5432 está bloqueado.")

if __name__ == "__main__":
    diagnostico()