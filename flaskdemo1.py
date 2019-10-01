
from flask import Flask,render_template,request,redirect

app = Flask(__name__)
app.debug = True
@app.route('/index',methods=["GET"])
def index():
    return render_template('index.html',user_dict=user_dict)
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method==["GET"]:
        return render_template('login.html',logintext=logintext)
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'user' and pwd == 'pwd':
            return redirect('index.html')
    return render_template('login.html',error='用户名密码错误')
@app.route('/info/<int:uid>',methods=['GET'])
def info(uid):
    user=user_dict.get(uid).get('name')
    pwd=user_dict.get(uid).get('pwd')
    return render_template('info.html',user=user,pwd=pwd)
@app.route('/dropdown',methods=["GET"])
def dropdown():
    return render_template('dropdown.html',user_dict=user_dict)
if __name__ == '__main__':
    user_dict={
        1:{'name':"user1",'pwd':"pwd1"},
        2:{'name':"user2",'pwd':"pwd2"},
        3:{'name':"user3",'pwd':"pwd3"}
    }
    app.run()


import os
print(os.__file__)
