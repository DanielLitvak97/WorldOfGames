from flask import Flask
from pymysql import connect

app = Flask(__name__)
@app.route('/')
def score_server():
    try:
        conn = connect(host='db', port=3306, user='root', passwd='Password123', db='games', autocommit=True)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users_scores")
        record = cursor.fetchone()
        score = int(record[0])

        return """<html>
                       <head>
                         <title>Scores Game</title>
                       </head>
                       <body>
                         <h1>The score is <div id="score">{%s}</div></h1> 
                       </body>
                 </html>""" % score

    except:
        return """<html>
                       <head>
                         <title>Scores Game</title>
                       </head>
                       <body>
                       <body>
                         <hi><div id="score" style="color:red">{ERROR}</div></h1>
                       </body>
                 </html>"""


app.run(host="0.0.0.0", port=8777, debug=True)
