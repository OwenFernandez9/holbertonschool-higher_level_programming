#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, password=mysql_password, database=database_name)
    cur: MySQLdb.cursors.Cursor = db.cursor()

    cur.execute("""
        SELECT MIN(id), name 
        FROM states 
        GROUP BY name 
        ORDER BY MIN(id) ASC;
    """)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
