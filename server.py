
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'
app.message = 0
gold = 0
count = 15


@app.route('/')
def index():
    print(session['count'])
    session['message'] += ''
    session['gold'] += 0
    session['win'] = ''
    session['count'] -= 1

    if session['count'] == 0 and session['gold'] >= 50:
        session['win'] = 'Win'
        session['gold'] = 0
        session['count'] = 0
        # session['message'] = ''

    elif session['count'] <= 0 and session['gold'] < 50:
        session['win'] = 'Lose - Play Again'
        session['gold'] = 0
        session['count'] = 0
        session['message'] = ''

        session['message'] = ''

    return render_template("index.html", win=session['win'], count=session['count'], message=session['message'], gold=session['gold'])


@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm' and session['count'] > 0:
        session['gold'] += 15
        session['message'] += '<li style=\"color: green\">Earn 15 golds from the farm!</li>'

    elif request.form['building'] == 'cave' and session['count'] > 0:
        session['gold'] += 7
        session['message'] += '<li style=\"color: green\">Earn 7 golds from the cave!</li>'

    elif request.form['building'] == 'house' and session['count'] > 0:
        session['gold'] += 4
        session['message'] += '<li style=\"color: green\">Earn 4 golds from the House!</li>'

    elif request.form['building'] == 'casino' and session['count'] > 0:
        session['gold'] -= 10
        if session['gold'] > 0:
            session['message'] += '<li style=\"color: green\">Earn 30 golds from the Casino!</li>'
        else:
            session['message'] += '<li style=\"color: red\">Earn -1 golds from the Casino!</li>'

    # else:
    #     session['count'] = 1
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    session['gold'] = 0
    session['count'] = 8
    session['message'] = ''

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
