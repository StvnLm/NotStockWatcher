import sqlite3

try:
    sqliteConnection = sqlite3.connect('../db.sqlite3')
    sqlite_create_table_query = '''CREATE TABLE StockTable (
                                id INTEGER PRIMARY KEY,
                                ticker TEXT,
                                asset_description TEXT,
                                asset_type TEXT,
                                amount TEXT,
                                type TEXT,
                                transaction_date DATETIME,
                                senator TEXT);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")