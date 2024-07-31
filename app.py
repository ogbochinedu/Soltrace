from flask import Flask
from automate.automate import Automate

app = Flask(__name__)

@app.route('/')
def home():
    auto = Automate()
    auto.start()
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
