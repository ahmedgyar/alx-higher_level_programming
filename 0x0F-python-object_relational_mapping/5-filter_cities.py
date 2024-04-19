#!/usr/bin/python3
''' script for task 2
    script should take 4 arguments: mysql username,
    mysql password, database name and state name searched
'''

import sys
import MySQLdb


def anything():
    ''' displays all values in the states table in hbtn db where name
        matches the argument passed to the script
    '''
    username = sys.argv[1]
    password = 'ahmedyasser'
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = 3306
    
    con = MySQLdb.connect(user=username, passwd=password,
                        db=db_name, host=host, port=port)
    cur = con.cursor()
    cur.execute('SELECT c.name FROM cities c INNER JOIN states s ' +
                'ON s.id = c.state_id WHERE ' +
                'BINARY s.name = %s ' +
                'ORDER BY c.id ASC;', [state_name])
    results = cur.fetchall()
    cur.close()
    con.close()

    for result in results:
        print(result)


if __name__ == '__main__':
    anything()
