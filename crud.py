import sqlite3 as sql

class crud:
    def __init__(self, database):
        self.conn = sql.connect(database)
        self.cursor = self.conn.cursor()
        
    def CREATE_TABLE(self, table_name, fields):
        fields_to_query = []
        query = 'CREATE TABLE ' + table_name + '(' + fields + ')'

        self.cursor.execute(query)
        self.conn.commit()

    def INSERT_INTO(self, table, values):
        quant_i = []
        if len(values) >= 2:
            for i in range(len(values) - 1):
                quant_i.append(', ?')
            query = 'INSERT INTO ' + table +  ' VALUES(?' + ''.join(quant_i) + ')'
        else:
            query = 'INSERT INTO ' + table +  ' VALUES(?)'

        self.cursor.execute(query, values)
        self.conn.commit()

    def DELETE(self, table, where=False):
        query = 'DELETE FROM ' + table
        if where:
            query = query + ' WHERE ' + where['coluna'] + where['oper'] + '?'
            self.cursor.execute(query,[ where['valor']])
        else:
            self.cursor.execute(query)

        self.conn.commit()

    def DROP_TABLE(self, table):
        query = 'DROP TABLE ' + table

        self.cursor.execute(query)
        self.conn.commit()

    def UPDATE(self, table_name, _set, where):
        query = 'UPDATE ' + table_name + ' SET ' + _set['coluna'] + _set['oper'] + '? ' + ' WHERE ' + where['coluna'] + where['oper'] + '?'

        self.cursor.execute(query, [_set['valor'], where['valor']])
        self.conn.commit()


    def SELECT(self, table, quant, where=False):
        query = 'SELECT ' + quant + ' FROM ' + table
        if where:
            query = query + ' WHERE ' + where['coluna'] + where['oper'] + '?'
            self.cursor.execute(query, [where['valor']])
        else:
            self.cursor.execute(query)
        
        return self.cursor.fetchall()