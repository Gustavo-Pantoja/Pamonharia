import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "banco.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def conectar():
    conn = sqlite3.connect(DB_PATH)
    criar_tabelas(conn)
    return conn


def criar_tabelas(conn):
    cursor = conn.cursor()

    # Tabela de vendas (NÃO APAGAR)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor REAL NOT NULL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Tabela de caixa diário (NOVA)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS caixa_diario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT UNIQUE,
            total_vendas REAL DEFAULT 0
        )
    """)

    conn.commit()
