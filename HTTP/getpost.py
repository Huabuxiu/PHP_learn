from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/register',methods=['POST'])
def resgister():
    print(request.headers)
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    return request.form.get('name')+',Welcome'

if __name__ == '__main__':
    app.run(debug=True)