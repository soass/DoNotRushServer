# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response
from flask_cors import CORS
# import json
import MySQLdb

api = Flask(__name__)
CORS(api)

@api.route('/api/getError/<int:userId>', methods=['GET'])
def get_data(userId):
 try:
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
     sql = "select * from error where isread = 0 and userid = " + str(userId)
     cur.execute(sql)

     # 実行結果を取得する
     rows = cur.fetchall()
     print(rows)
     for row in rows:
         num = row[0]
         sql = "update error set isread = 1 where id =" + str(num)
         cur.execute(sql)
         conn.commit()
         print(sql)

     cur.close
     conn.close

 except Exception as e:
     print(e)
     abort(404)

 result = {
     "result":True,
     "data":{
         "num":len(rows),
         }
     }


 return make_response(jsonify(result))
@api.route('/api/insertData/<int:userId>/<error>', methods=['POST'])
def insert_data(userId, error):
  try:
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


      sql = "INSERT INTO error (userid,errormessage) VALUES (" + str(userId) +",\"" + error + "\")"
      print(sql)
      cur.execute(sql)


      # 実行結果を取得する


      cur.close()
      conn.commit()
      conn.close()
  except Exception as e:
      print(e)
      abort(404)

  return make_response()


@api.errorhandler(404)
def not_found(error):
 return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
 api.run(host='0.0.0.0', port=3000)
