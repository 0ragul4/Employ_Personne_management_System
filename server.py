from flask import Flask,render_template, url_for


app = Flask(__name__)

@app.route('/login')
def log():
    return render_template('login.html')

@app.route('/home')
def home1():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
