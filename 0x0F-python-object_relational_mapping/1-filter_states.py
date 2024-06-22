#!/usr/bin/python3

"""lsfjglaerjsglasglnvlsrnljeargsV"""


from sys import argv
import MySQLdb as mdb

if __name__ == "__main__":
    curr = mdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3], charset="utf8")

    cur = curr.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \"N%\" ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)

    cur.close()
    curr.close()
