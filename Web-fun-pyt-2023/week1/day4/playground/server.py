from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', times=3, color='blue')

@app.route('/play/<string:times>')
def play_times(times):
    times = int(times)
    return render_template('index.html', times=times, color='blue')

@app.route('/play/<string:times>/<string:color>')
def play_times_color(times, color):
    times = int(times)
    return render_template('index.html', times=times, color=color)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
