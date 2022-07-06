import pyodbc


class counters():
    def __init__(self, id, name, number):
        self.id = id
        self.name = name
        self.number = number


def read_Access(TableName):
    conn = pyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\B\Desktop\back\OnlineShop.accdb;")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + str(TableName))
    rows = cursor.fetchall()
    json = []
    if str(TableName) == '''counters''':
        for row in rows:
            obj = counters(row[0], row[1], row[2])
            json.append(obj)
    return json
