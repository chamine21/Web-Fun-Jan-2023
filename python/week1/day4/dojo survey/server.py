from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session["name"] = request.form["name"]
    session["Dojo_Location"] = request.form["Dojo_Location"]
    session["Favorite_language"] = request.form["Favorite_language"]
    session["comment"] = request.form["comment"]
    return redirect('/result')

@app.route('/result')
def result():
    name = session.get('name')
    Dojo_Location = session.get('Dojo_Location')
    Favorite_language = session.get('Favorite_language')
    comment = session.get('comment')
    return render_template('result.html')
 
    

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8000)
