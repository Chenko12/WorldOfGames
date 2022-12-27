from flask import Flask

def score_server():
    scoreserver = Flask(__name__)
    @scoreserver.route("/")
    def showscore():
        scores = open('Scores.txt', 'r')
        SCORE  = scores.readline()
        return (f'''<html>
                    <head>
                    <title>Scores Game</title>
                    </head>
                    <body>
                    <h1>The score is <div id="score" style="color:green">{SCORE}</div></h1>
                    </body>
                    </html>'''), 200

    @scoreserver.route("/")
    def error():
        ERROR = "Can't show scores"
        return (f'''<html>
                    <head>
                    <title>Scores Game</title>
                    </head>
                    <body>
                    <body>
                    <h1><div id="score" style="color:red">{ERROR}</div></h1>
                    </body>
                    </html>'''),201


    if "__main__" == __name__:
        scoreserver.run('0.0.0.0', debug=True, port=30000)
