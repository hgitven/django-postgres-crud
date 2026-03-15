import os
import django
from django.db import connections
from django.db.utils import OperationalError

# CONFIGURACIÓN CRÍTICA:
# Asegúrate de que 'pythonV' sea el nombre exacto de la carpeta 
# que contiene tu archivo settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pythonV.settings') 

try:
    django.setup()
except Exception as e:
    print(f"Error configurando Django: {e}")
    exit()

def check_django_connection():
    print("--- Verificando Conexión desde el corazón de Django ---")
    db_conn = connections['default']
    try:
        db_conn.cursor()
        print("¡ÉXITO! Django puede conectarse a PostgreSQL sin problemas.")
        print(f"Base de datos: {db_conn.settings_dict['NAME']}")
        print(f"Host: {db_conn.settings_dict['HOST']}")
    except OperationalError as e:
        print("\n[ERROR DE DJANGO]")
        print(f"Django no pudo conectar. El error técnico es:\n{e}")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

if __name__ == "__main__":
    check_django_connection()