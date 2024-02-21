# Script para criar o banco de dados
from FakePinterest import database, app
from FakePinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()