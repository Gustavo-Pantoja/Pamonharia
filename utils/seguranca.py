import os
import shutil
from datetime import datetime

BANCO = "banco.db"
PASTA_BACKUP = "backup"


def verificar_banco():
    # banco existe?
    if os.path.exists(BANCO):
        return True

    print("\n⚠ BANCO DE DADOS NÃO ENCONTRADO!")

    if not os.path.exists(PASTA_BACKUP):
        print("❌ Pasta de backup inexistente.")
        return False

    backups = [
        f for f in os.listdir(PASTA_BACKUP)
        if f.endswith(".db")
    ]

    if not backups:
        print("❌ Nenhum backup encontrado.")
        return False

    ultimo = max(backups)

    origem = os.path.join(PASTA_BACKUP, ultimo)
    destino = BANCO

    shutil.copy(origem, destino)

    print(f"✅ Banco restaurado automaticamente: {ultimo}")

    return True
