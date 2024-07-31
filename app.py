from flask import Flask

app = Flask(__main__)

@app.route("/")
def home():
    return "hello this is the main page <HELLO<h1>"

@app.route("/<name>")
def user(name):
    retu

if __name__ == "__main__":
   app.run()