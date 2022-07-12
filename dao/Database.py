import pyodbc


class counters():
    def __init__(self, id, name, number):
        self.id = id
        self.name = name
        self.number = number


class sqlbase():
    def getConnection(self):
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=46.34.161.23,13433;DATABASE=Bigdeli;UID=sa;PWD=111@a')
        cursor = connection.cursor()
        return connection, cursor


def ReadDB():
        sqlBase = sqlbase()
        connection, cursor = sqlBase.getConnection()
        cursor.execute("set nocount on; select * from counters")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        li = []
        for row in rows:
            obj = counters(row[0], row[1], row[2])
            li.append(obj)
        return li