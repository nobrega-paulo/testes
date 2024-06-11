import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Teste 2', 'teste2@gmail.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)', (2, 'Teste 3', 'teste3@gmail.com'))
    conexao.commit()
except Exception as exc:
    print(f"Ops! bla bla bla {exc}")
    conexao.rollback()