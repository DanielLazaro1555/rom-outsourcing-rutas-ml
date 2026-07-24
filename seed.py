# seed.py
import pandas as pd
from app import app
from models import db, Usuario, PDV, Promotor
from pdv_importer import import_pdv_dataframe, load_pdv_dataframe

def seed_database():
    print("[*] Iniciando el sembrado de la base de datos...")
    
    # 1. Crear usuarios por defecto
    roles = ['admin', 'analista', 'supervisor', 'promotor', 'ejecutivo', 'gerente']
    usuarios_creados = {}
    
    for rol in roles:
        email = f"{rol}@rom.com"
        # Verificar si ya existe
        usuario = Usuario.query.filter_by(email=email).first()
        if not usuario:
            usuario = Usuario(email=email, rol=rol)
            usuario.set_password("password")  # Contraseña para login: password
            db.session.add(usuario)
            print(f"[+] Usuario creado: {email}")
        else:
            # Actualizar contraseña si ya existe
            usuario.set_password("password")
            print(f"[~] Usuario actualizado: {email}")
        usuarios_creados[rol] = usuario
    
    db.session.commit()
    
    # 2. Crear promotores de prueba (asociados a los usuarios de tipo promotor)
    # Crearemos 5 promotores para los clusters por defecto
    for i in range(5):
        email_prom = f"promotor{i}@rom.com"
        usuario_prom = Usuario.query.filter_by(email=email_prom).first()
        if not usuario_prom:
            usuario_prom = Usuario(email=email_prom, rol='promotor')
            usuario_prom.set_password("password")  # Contraseña para login: password
            db.session.add(usuario_prom)
            db.session.commit()
        else:
            usuario_prom.set_password("password")
        
        promotor = Promotor.query.filter_by(nombre=f"Promotor {i}").first()
        if not promotor:
            promotor = Promotor(
                nombre=f"Promotor {i}",
                usuario_id=usuario_prom.id,
                zona="LIMA",
                cuenta="Pernod Ricard",
                capacidad_diaria=5
            )
            db.session.add(promotor)
            print(f"[+] Promotor creado: Promotor {i}")
        else:
            print(f"[-] Promotor ya existe: Promotor {i}")
            
    db.session.commit()
    
    # 3. Sembrar puntos de venta (PDVs) desde el CSV
    if PDV.query.count() == 0:
        print("[*] Cargando PDVs desde data/pdv.csv...")
        try:
            df = load_pdv_dataframe("data/pdv.csv", filename="data/pdv.csv")
            stats = import_pdv_dataframe(df)
            db.session.commit()
            print(
                "[+] Sembrado exitoso: "
                f"{stats['imported']} PDVs importados, "
                f"{stats['inactive_fuera_de_ruta']} fuera de ruta inactivos, "
                f"{stats['duplicates_in_file']} duplicados en archivo, "
                f"{stats['duplicates_in_db']} duplicados en BD, "
                f"{stats['invalid_rows']} filas inválidas."
            )
        except Exception as e:
            db.session.rollback()
            print(f"[-] Error cargando el CSV: {str(e)}")
    else:
        print(f"[-] Los PDVs ya están sembrados ({PDV.query.count()} registros en BD).")

    print("[*] Sembrado de base de datos finalizado.")

if __name__ == "__main__":
    with app.app_context():
        seed_database()
