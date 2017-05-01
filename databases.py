#!/usr/bin/python


def mysql():
    import MySQLdb # apt install python-mysqldb

    # connect
    db = MySQLdb.connect(host="localhost", user="username", passwd="password",db="database_name")

    cursor = db.cursor()

    # execute SQL select statement
    cursor.execute("SELECT * FROM users")

    # get the number of rows in the resultset
    numrows = int(cursor.rowcount)
    ret = cursor.fetchall()

    for row in ret:
        print(row[4])


def mongodb():
    from pymongo import MongoClient
    client = MongoClient("mongodb://mongodb0.example.net:27017")
    db = client["test"] # test is a collection
    
    # insert
    a_dict = dict()
    result = db["restaurants"].insert_one(a_dict)
    
    # query
    cursor = db["restaurants"].find()
    for doc in cursor:
        print(doc)


def sqlite():
    import sqlite3
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
