import pymysql

DB_CONFIG = dict(
    host="localhost",
    user="root",
    password="1234",
    database="gimbap_store",
    charset="utf8"
)

class DB:
    def __init__(self, **config):
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)
    
    def fetch_items(self):
        sql = "SELECT * FROM gimbaps ORDER BY ID"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
    
    def insert_items(self, Name, price, inventory) :
        sql = "INSERT INTO gimbaps (Name, price, inventory) VALUES (%s,%s,%s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (Name, price, inventory))
                conn.commit()
                return True
            except Exception as e:
                print(e)
                conn.rollback()
                return False
    
    def update_items(self, ID, Name, price, inventory):
        sql = "UPDATE gimbaps SET Name=%s, price=%s, inventory=%s WHERE ID=%s"
        with self.connet() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql,(Name,price,inventory,ID))
                conn.commit()
                return True
            except Exception as e:
                print(e)
                conn.rollback()
                return False
            
    def delete_items(self,ID):
        sql="DELETE FROM gimbaps WHERE ID=%s"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql,(ID,))
                conn.commit()
                return True
            except Exception as e:
                print(e)
                conn.rollback()
                return False
