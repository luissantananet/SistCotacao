import sqlite3

class Database:
    def __init__(self, name = 'database.db') -> None:
        self.nome = name
    
    def connect(self):
        self.conn = sqlite3.connect(self.nome)
        self.cursor = self.conn.cursor()
    def cursor(self):
        return self.conn.cursor()
    
    def disconnect(self):
        try:
            self.conn.close()
        except AttributeError:
            pass
    
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarifas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                frete_peso decimal(7,2),
                ad_valoren decimal(7,4),
                gris decimal(7,4),
                taxa decimal(7,2),
                icms decimal(7,2)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarifas_minimas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao varchar(50),
                tarifa_base decimal(7,2),
                tarifa_litoral decimal(7,2),
                ad_Gris decimal(7,4),
                pedagio decimal(7,2),
                pedlitoral decimal(7,2)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cotacao(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                emit_cnpj varchar(14),
                emit_nome varchar(100),
                dest_cnpj varchar(14),
                dest_nome  varchar(100),
                cidade_origem varchar(100),
                estado_origem varchar(100),
                cidade_destino varchar(100),
                estado_destino varchar(100),    
                tipo varchar(3),
                valor_merc decimal(10,2),
                peso decimal(10,3),
                volume int,
                tipo_merc varchar(100),
                peso_cubo_total decimal(10,3),
                m3_total decimal(10,3),
                data_cotacao date,
                fretetotal varchar(10),
                fretetotal_litotal varchar(10)
            );
        """)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cubagem(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dim1 decimal(5,2),
                dim2 decimal(5,2),
                dim3 decimal(5,2),
                volume decimal,
                m3 decimal(6,3)
            );
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cnpj varchar(14),
                nome varchar(100),
                endereco varchar(100),
                cidade varchar(100),
                estado varchar(100),
                cep varchar(10),
                telefone varchar(20),
                email varchar(100)
            );   
        ''')
        self.conn.commit()
    
    def selects_all(self,table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()
    
    def select_cubagem(self,id):
        self.cursor.execute(f"SELECT * FROM cubagem WHERE id = '{id}';")
        for linha in self.cursor.fetchall():
            return linha
    
    def TRUNCATE_TABLE(self,table):
        self.cursor.execute(f"DROP TABLE '{table}';")
        self.conn.commit()
    
    def inserts_all(self, table, values):
        columns = ", ".join(values.keys())
        placeholders = ", ".join(["?" for _ in values])
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(sql, list(values.values()))
        self.conn.commit()

    def updeate_all(self, table, values):
        set_clause = ", ".join([f"{col} = ?" for col in values.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE descricao = ?"
        self.cursor.execute(sql, list(values.values()) + [values['descricao']])
        self.conn.commit()
    
    def delete_all(self, table, values):
        sql = f"DELETE FROM {table} WHERE descricao = ?"
        self.cursor.execute(sql, [values['descricao']])
        self.conn.commit()

    def insert_tarifas(self):
        self.cursor.execute("INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 01 até 20Kg',00.00,00.00,00.00,00.00,00.00);")
        self.cursor.execute("INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 21 até 50Kg',00.00,00.00,00.00,00.00,00.00);")
        self.cursor.execute("INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 51 até 100Kg',00.00,00.00,00.00,00.00,00.00);")
        self.cursor.execute("INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 101 até 150Kg',00.00,00.00,00.00,00.00,00.00);")
        self.cursor.execute("INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 151 até 200Kg',00.00,00.00,00.00,00.00,00.00);")
        self.cursor.execute("INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 201 até 250Kg',00.00,00.00,00.00,00.00,00.00);")
        self.cursor.execute("INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 251 até 300Kg',00.00,00.00,00.00,00.00,00.00);")
        self.cursor.execute("INSERT INTO tarifas(descricao,frete_peso,ad_valoren,gris,taxa,icms) VALUES('TB',00.00,00.00,00.00,00.00,00.00);")
        self.cursor.execute("INSERT INTO tarifas(descricao,frete_peso,ad_valoren,gris,taxa,icms) VALUES('TBL',00.00,00.00,00.00,00.00,00.00);")
        self.conn.commit()

if __name__ == '__main__':
    db = Database()
    db.connect()
    db.create_tables()
    db.insert_tarifas()
    if db.conn:
        print('Conectado')
    db.disconnect()