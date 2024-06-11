from pathlib import Path

try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError:
    print("Arquivo não encontrado")


ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except IsADirectoryError as exc:
    print("Não foi possivel abrir o aquivo.")