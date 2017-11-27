from flask import Flask
from flask_cors import CORS

app = Flask('CVaaS')
CORS(app)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)