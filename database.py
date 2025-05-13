import sqlite3

def conectar():
    return sqlite3.connect('clientes.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sexo TEXT,
        email TEXT,
        data_nascimento TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()

def inserir_cliente(nome, sexo, email, data_nascimento, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO cliente (nome, sexo, email, data_nascimento, status)
    VALUES (?, ?, ?, ?, ?)
    """, (nome, sexo, email, data_nascimento, status))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def atualizar_cliente(id, nome, sexo, email, data_nascimento, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE cliente SET nome=?, sexo=?, email=?, data_nascimento=?, status=? WHERE id=?
    """, (nome, sexo, email, data_nascimento, status, id))
    conn.commit()
    conn.close()

def deletar_cliente(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cliente WHERE id=?", (id,))
    conn.commit()
    conn.close()
