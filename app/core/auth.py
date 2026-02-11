import getpass

SENHA_ADMIN = "1234"  # depois você troca


def pedir_senha():
    tentativa = getpass.getpass("\n🔐 Senha do administrador: ")

    if tentativa == SENHA_ADMIN:
        print("✅ Acesso autorizado.")
        return True
    else:
        print("❌ Senha incorreta.")
        return False
