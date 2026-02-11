from app.data.db import conectar
from datetime import date
from app.core.auth import pedir_senha


def iniciar_caixa_diario():
    hoje = date.today().isoformat()
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM caixa_diario WHERE data = ?",
        (hoje,)
    )

    if cursor.fetchone():
        print("Caixa de hoje já está aberto")
    else:
        cursor.execute(
            "INSERT INTO caixa_diario (data) VALUES (?)",
            (hoje,)
        )
        conn.commit()
        print("Caixa diário iniciado com sucesso")
    conn.close()