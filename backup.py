import os
from datetime import datetime

def crear_backup():
    carpeta_origen = input("Seleccione la carpeta a respaldar:\n")

    if not os.path.exists(carpeta_origen):
        print("La carpeta no existe.")
        return

    fecha = datetime.now().strftime("%Y_%m_%d_%H_%M")
    carpeta_destino = f"Backups/Backup_{fecha}"

    print("\nCreando respaldo...\n")

    os.makedirs(carpeta_destino, exist_ok=True)

    print("Respaldo creado correctamente.")
    print(f"Ruta:\n{os.path.abspath(carpeta_destino)}")

if __name__ == "__main__":
    crear_backup()
