import sqlite3
import os


class GestorTabelas:
    def __init__(self, nome_db):
        self.nome_db = f"{nome_db}.db"

    def conectar(self):
        return sqlite3.connect(self.nome_db)

    def criar_tabela(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS cartas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, ident TEXT NOT NULL) """)
        conn.commit()
        conn.close()

    def verificar_existencia(self):
        return os.path.exists(self.nome_db)

    def eliminar_tabela(self):
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS cartas")
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"O erro foi: {e}") 
            return False


    def eliminar_ficheiro_lista(self):
        if os.path.exists(self.nome_db):
            os.remove(self.nome_db)
            return True
        return False


    def adicionar_carta(self, nome, ident):
        self.criar_tabela()
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cartas (nome, ident) VALUES (?, ?)", (nome, ident))
        conn.commit()
        conn.close()
        return "Gravado na Base de Dados!"

    def ler_tudo(self):
        print(f"DEBUG: A ler do ficheiro {self.nome_db}")
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, ident FROM cartas")
        linhas = cursor.fetchall()
        conn.close()
        if not linhas:
            return "Lista vazia."
        resultado = ""
        for nome, ident in linhas:
            resultado += f"- {nome}: {ident}\n"
        return resultado
    
    def remover_carta(self, n, i):
        c = self.conectar()
        cur = c.cursor()
        cur.execute("DELETE FROM cartas WHERE nome = ? AND ident = ?", (n, i))
        apagados = cur.rowcount 
        c.commit()
        c.close()
        if apagados > 0:
            return f"Foram apagadas {apagados} cartas"
        else:
            return f"Nenhuma carta removida!"