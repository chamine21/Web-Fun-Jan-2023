from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    visit_count = session.get('visit_count', 0)
    visit_count += 1
    session['visit_count'] = visit_count
    return render_template('index.html', visit_count=visit_count)

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8000)
