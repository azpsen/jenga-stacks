from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/test')
def test_route():
    return {
        'name': 'Hello, World!',
        'key': 'value',
        'date': datetime.datetime.now()
    }

if __name__ == '__main__':
    app.run(debug=True)
