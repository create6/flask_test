from flask import Flask, redirect, render_template, Response

app = Flask(__name__)





@app.route('/favicon.ico')
def logo():
    f = open('log.ico','rb')
    image = f.read()
    print('image:%s'%image)
    resp = Response(image, mimetype="image/jpeg")
    return resp

@app.route('/aa')
def hello_world():
    return 'Hello Python !'

@app.route('/login')
def login():
    return 'Login!'

@app.route('/')
def market():
    # return redirect(my_collect.html)
    return render_template('my_collect.html')


if __name__ == '__main__':
    # app.run(debug = True)
    app.run()