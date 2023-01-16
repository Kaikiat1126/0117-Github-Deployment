##动态加载html文件
from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/html', methods=['get'])
def getData():
    #get arguments from request
    return '<h1>hello world</h1><script></script>'  #template flask JInjia2

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1' , port=81)
