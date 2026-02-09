import sqlite3

def conectar():
    conn = sqlite3.connect("banco.db")
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
