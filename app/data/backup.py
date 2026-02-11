from pathlib import Path
import shutil
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "banco.db"


def fazer_backup():
    if not DB_PATH.exists():
        print("Banco de dados não encontrado.")
        return

    backup_dir = BASE_DIR / "backups"
    backup_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_dir / f"banco_backup_{timestamp}.db"

    shutil.copy(DB_PATH, backup_file)

    print(f"Backup criado em: {backup_file}")
