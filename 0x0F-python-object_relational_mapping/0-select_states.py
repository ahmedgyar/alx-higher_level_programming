#!/usr/bin/python3
import sys
import MySQLdb


def anything():
    '''List all states in the database.'''
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <db_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = 'ahmedyasser'
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    con = MySQLdb.connect(user=username, passwd=password, db=db_name, host=host, port=port)
    cur = con.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    results = cur.fetchall()

    cur.close()
    con.close()

    for result in results:
        print(result)


if __name__ == '__main__':
    anything()
