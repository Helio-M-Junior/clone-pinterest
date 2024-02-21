# Script para gerar a chave secreta para o banco de dados
import secrets

print(secrets.token_hex(16))