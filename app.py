from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/favicon.ico')
def logo():
    f = open('static/img/logo.ico','rb')
    image = f.read()
    # print('image:%s'%image)
    resp = Response(image, mimetype="image/jpeg")
    return resp

@app.route('/aa')
def hello_world():
    return render_template('my_collect.html')

@app.route('/login')
def login():
    return render_template('a01.html')

@app.route('/')
def index():
    # return redirect(my_collect.html)
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run()