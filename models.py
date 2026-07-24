# models.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    rol = db.Column(db.String(50), nullable=False)  # admin, analista, supervisor, promotor, ejecutivo, gerente

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Usuario {self.email} ({self.rol})>"


class PDV(db.Model):
    __tablename__ = 'pdvs'
    
    id = db.Column(db.Integer, primary_key=True)
    codigo_pdv = db.Column(db.String(100), unique=True, nullable=True)
    nombre = db.Column(db.String(200), nullable=False)
    empresa = db.Column(db.String(200))
    canal = db.Column(db.String(100))
    zona = db.Column(db.String(100))
    distrito = db.Column(db.String(150))
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    direccion = db.Column(db.String(300))
    prioridad = db.Column(db.String(50), default='media')  # alta, media, baja
    activo = db.Column(db.Boolean, default=True)  # Para cierres temporales

    def __repr__(self):
        return f"<PDV {self.nombre}>"


class Promotor(db.Model):
    __tablename__ = 'promotores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)
    zona = db.Column(db.String(100))
    cuenta = db.Column(db.String(100), default='Pernod Ricard')
    capacidad_diaria = db.Column(db.Integer, default=5)
    activo = db.Column(db.Boolean, default=True)

    # Relación de conveniencia
    usuario = db.relationship('Usuario', backref=db.backref('promotor_perfil', uselist=False))

    def __repr__(self):
        return f"<Promotor {self.nombre}>"


class Ausencia(db.Model):
    __tablename__ = 'ausencias'
    
    id = db.Column(db.Integer, primary_key=True)
    promotor_id = db.Column(db.Integer, db.ForeignKey('promotores.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    semana = db.Column(db.Integer, nullable=True)
    dia = db.Column(db.String(20), nullable=True)
    motivo = db.Column(db.String(300))

    promotor = db.relationship('Promotor', backref=db.backref('ausencias', lazy=True))

    def __repr__(self):
        return f"<Ausencia Promotor {self.promotor_id} en {self.fecha}>"


class RutaPlanificada(db.Model):
    __tablename__ = 'rutas_planificadas'
    
    id = db.Column(db.Integer, primary_key=True)
    promotor_id = db.Column(db.Integer, db.ForeignKey('promotores.id'), nullable=False)
    pdv_id = db.Column(db.Integer, db.ForeignKey('pdvs.id'), nullable=False)
    semana = db.Column(db.Integer, nullable=False)
    dia = db.Column(db.String(20), nullable=False)  # Lunes, Martes, Miércoles, etc.
    orden = db.Column(db.Integer, nullable=False)

    promotor = db.relationship('Promotor', backref=db.backref('rutas', lazy=True))
    pdv = db.relationship('PDV', backref=db.backref('asignado_en_rutas', lazy=True))

    def __repr__(self):
        return f"<Ruta Promotor {self.promotor_id} - {self.dia} (Semana {self.semana})>"
