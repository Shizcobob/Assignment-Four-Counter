from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    
app.secret_key = 'Shizcobob'

@app.route('/')     
def counting():

    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0

    counterhtml=session['counter']

    if 'actual_counter' in session:
        session['actual_counter'] += 1
    else:
        session['actual_counter'] = 0

    actual_counter=session['actual_counter']

    return render_template('index.html', counterhtml=counterhtml, actual_counter=actual_counter)
        

@app.route('/double_down')
def double_down():
    if 'counter' in session:
        session['counter'] += 1
    return redirect('/')

@app.route('/input_amount', methods=['post'])
def input_amount():
    session['counter'] += int(request.form['selected'])
    return redirect('/')
    


@app.route('/destroy_session')
def resetter():
    session.pop('counter')
    session.pop('actual_counter')
    return redirect('/')


if __name__=="__main__":     
    app.run(debug=True)    
