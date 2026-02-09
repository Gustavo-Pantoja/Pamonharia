import shutil
from datetime import date

def fazer_backup():
	hoje = date.today().isoformat()
	origem = "banco.db"
	destino = f"backup/backup_{hoje}.db"

	try:
		shutil.copy(origem, destino)
		print("Backup realizado com sucesso")
	except FileNotFoundError:
		print("Banco de dados não encontrado")