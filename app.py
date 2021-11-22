from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/account")
def account():
    return render_template('signIn.html')

if __name__ == '__main__':
    app.run(debug=True)