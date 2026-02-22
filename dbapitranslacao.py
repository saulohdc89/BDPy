import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect( ROOT_PATH / 'clientes.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row
try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES(?, ?)', ('TESTE 6', 'teste6@gmail.com'))    
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES(?, ?, ?)', (2,'TESTE 7', 'teste7@gmail.com'))
    cursor.execute("DELETE FROM clientes WHERE id= 16;")
    conexao.commit()
except Exception as exc:
    print(f'OPS! Um erro ocorreu! {exc}' )
    conexao.rollback
