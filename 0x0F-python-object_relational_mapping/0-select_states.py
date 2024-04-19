#!/usr/bin/python3
import sys
import MySQLdb

def anything():
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <db_name>")
        sys.exit(1)

    # Extracting command line arguments
    username = sys.argv[1]
    password = 'ahmedyasser'
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    # Connecting to the MySQL database
    try:
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

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

if __name__ == '__main__':
    anything()
