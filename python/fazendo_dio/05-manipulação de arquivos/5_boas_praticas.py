from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
    1 / 0

print(arquivo.read())
 
