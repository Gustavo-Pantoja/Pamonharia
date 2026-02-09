import sqlite3
import os


def resetar_caixa():
    if os.path.exists("banco.db"):
        os.remove("banco.db")
        print("\n✅ Caixa resetado com sucesso.")
    else:
        print("\n⚠ Banco já não existe.")
