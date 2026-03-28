# Script de respaldo de Tommy0950
import os

def check_status():
    print("\n--- Verificador de Estado de Red ---")
    site = input("Escribe una URL (ej: google.com): ")
    # Ejecutamos un ping para ver si responde
    response = os.system("ping -c 1 " + site)

    if response == 0:
        print(f"\n[+] El sitio {site} esta ACTIVO")
    else:
        print(f"\n[-] El sitio {site} no responde")

if __name__ == "__main__":
    check_status()
  
