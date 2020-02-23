import flask
import flask_cors


app = flask.Flask(__name__)
flask_cors.CORS(app)

scores = {}

@app.route('/savescore')
def saveScore():
    correct = flask.request.values.get('correct')
    incorrect = flask.request.values.get('incorrect')
    if correct == None and incorrect == None:
        return {
            'code':-1,
            'msg':'Invalid Request'
        }
    correct = int(correct)
    incorrect = int(incorrect)

    scores[flask.request.remote_addr] = {
        'correct':correct,
        'incorrect':incorrect
    }
    return {
        'code':0
    }

@app.route('/retrieve')
def retrieveScore():
    return {
        'code':0,
        'correct':scores[flask.request.remote_addr]['correct'],
        'incorrect':scores[flask.request.remote_addr]['incorrect']
    }
