from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['get'])
def api():
    #get arguments from request
    return "Invalid event type"

if __name__ == '__main__':
    app.run(debug=True)
