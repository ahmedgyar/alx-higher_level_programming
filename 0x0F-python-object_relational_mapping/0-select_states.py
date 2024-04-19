#!/usr/bin/python3
import sys
import MySQLdb

def anything():
    '''list all states in db'''
    username = sys.argv[1]
    password = 'ahmedyasser'
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    con = MySQLdb.connect(user=username, passwd=password, db=db_name, host=host, port=port)
    cur = con.cursor()

    # Executing the SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetching results
    results = cur.fetchall()

    # Closing cursor and connection
    cur.close()
    con.close()

    # Printing results
    for result in results:
        print(result)


if __name__ == '__main__':
    anything()
