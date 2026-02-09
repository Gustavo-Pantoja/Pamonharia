from caixa.caixa import registrar_venda
from backup.backup import fazer_backup
from caixa.reset_diario import iniciar_caixa_diario
from caixa.reset import resetar_caixa
from utils.auth import pedir_senha


def menu_principal():
    iniciar_caixa_diario()

    while True:
        print("\n=== PAMONHARIA ===")
        print("1 - Registrar venda")
        print("2 - Fazer backup")
        print("4 - 🔄 Resetar caixa (admin)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_venda()

        elif opcao == "2":
            fazer_backup()

        elif opcao == "4":
            if pedir_senha():
                resetar_caixa()
                input("\nENTER para continuar...")

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida")
