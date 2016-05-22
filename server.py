from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/yolo/yoloname')
def yolo(yoloname):
    return 'Yolo name %s' % yoloname

if __name__ == '__main__':
    app.run()