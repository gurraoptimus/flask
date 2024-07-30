from flask import Flask

app = Flask(__main__)

def home():
    return "hello this is the main page<HELLO"

if __name__ == "__main__":
   app.run()