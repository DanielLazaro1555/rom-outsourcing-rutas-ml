#!/bin/sh

# Crear carpeta de logs si no existe
mkdir -p logs

# Log de inicio
echo "[$(date '+%Y-%m-%d %H:%M:%S')] --- Iniciando arranque del contenedor ---" >> logs/startup.log

# Esperar a que la base de datos esté lista
echo "Esperando a que la base de datos PostgreSQL inicie..." | tee -a logs/startup.log
python -c '
import socket
import time
import os
import urllib.parse

db_url = os.environ.get("DATABASE_URL", "")
if db_url:
    url = urllib.parse.urlparse(db_url)
    host = url.hostname
    port = url.port or 5432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((host, port))
            s.close()
            print("PostgreSQL está listo!")
            break
        except socket.error:
            print("Base de datos no disponible aún. Reintentando en 1s...")
            time.sleep(1)
' 2>&1 | tee -a logs/startup.log

# Ejecutar el sembrado de la base de datos
echo "Ejecutando sembrado de la base de datos..." | tee -a logs/startup.log
python seed.py 2>&1 | tee -a logs/startup.log

# Iniciar la aplicación Flask
echo "Iniciando Flask..." | tee -a logs/startup.log
exec python app.py
