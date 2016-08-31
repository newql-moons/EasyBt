import sqlite3


DB_PATH = '/media/moons/文档/SQLite/easybt/magnet.db'

class MagnetTab(object):

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)

    def insert(self, dic):
        hash_code = dic['hash']
        day = dic['day']
        hits = dic['hits']
        size = dic['size']
        title = dic['title']

        if self.select_by_hash(hash_code) is None:
            sql = 'INSERT INTO magnet VALUES (?,?,?,?,?)'
            self.conn.execute(sql, (hash_code, day, hits, size, title,))
            self.conn.commit()

    def select_by_hash(self, hash_code):
        sql = 'SELECT * FROM magnet WHERE hash = ?'
        cs = self.conn.execute(sql, (hash_code,))
        lines = cs.fetchall()

        if len(lines) == 0:
            return None
        else:
            return lines[0]

    def close(self):
        self.conn.close()
