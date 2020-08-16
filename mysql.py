import MySQLdb

# 接続する
conn = MySQLdb.connect(
 user='root',
 passwd='root',
 host='localhost',
 db='mydb')

# カーソルを取得する
cur = conn.cursor()

# SQL（データベースを操作するコマンド）を実行する
# userテーブルから、HostとUser列を取り出す
sql = "select * from error"
cur.execute(sql)

# 実行結果を取得する
rows = cur.fetchall()

# 一行ずつ表示する
for row in rows:
 print(row)

cur.close
conn.close
