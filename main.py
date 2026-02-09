from menu.menu_principal import menu_principal
from utils.seguranca import verificar_banco


def main():
    menu_principal()


if __name__ == "__main__":
    main()

if not verificar_banco():
    input("\nSistema não pode iniciar. ENTER para sair.")
    exit()
