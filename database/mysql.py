import MySQLdb # apt install python-mysqldb
def mysql():

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