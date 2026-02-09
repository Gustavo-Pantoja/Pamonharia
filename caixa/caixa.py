from utils.db import conectar
from datetime import date

def registrar_venda():
	try:
		valor = float(input("Valor da venda: R$ "))
	except ValueError:
		print("Valor inválido")
		return

	hoje = date.today().isoformat()
	conn = conectar()
	cursor = conn.cursor()

	cursor.execute(
	"INSERT INTO vendas (valor) VALUES (?)",
	(valor,)
	)

	cursor.execute(
	"UPDATE caixa_diario SET total_vendas = total_vendas + ? WHERE data = ?",
	(valor, hoje)
	)

	conn.commit()
	conn.close()

	print("Venda registrada e caixa atualizado")


registrar_venda()