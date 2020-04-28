from flask import Flask

app = Flask(__name__)
@app.route('/')
def score_server():
    try:
        file = open("Scores.txt", "r")
        score = file.readline()
        file.close()
        return """<html>
                       <head>
                         <title>Scores Game</title>
                       </head>
                       <body>
                         <h1>The score is <div id="score">{%s}</div></h1> 
                       </body>
                 </html>""" % score

    except IOError:
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
