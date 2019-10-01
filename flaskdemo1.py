
from flask import Flask,render_template,request,redirect
from datetime import timedelta
app = Flask(__name__)
app.debug = True
app.send_file_max_age_default = timedelta(seconds=1)
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
    return render_template('dropdown.html',user_dict=user_dict,asdf=dropdownTemplate()%'qwe')
def dropdownTemplate():
    template = """
    <div class="dropdown">
          <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
            %s
            <span class="caret"></span>
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenu">
              <li class="dropdown-submenu">
                  <a class="dropdown-toggle" tabindex="-1" href="#">停电影响用户</a>
                    <ul class="dropdown-menu" aria-labelledby="dropdownMenu">
                          <li class="dropdown-submenu">
                              <a class="dropdown-toggle" tabindex="-1" href="#">1</a>
                                <ul class="dropdown-menu" aria-labelledby="dropdownMenu">
                                    <li><a tabindex="-1" href="#">高低压接线图</a></li>
                                    <li><a tabindex="-1" href="#">定值单</a></li>
                                    <li><a tabindex="-1" href="#">自备电源情况</a></li>
                                    <li><a tabindex="-1" href="#">调度协议</a></li>
                                    <li><a tabindex="-1" href="#">现场规程</a></li>
                                    <li><a tabindex="-1" href="#">批准书</a></li>
                                </ul>
                          </li>
                        <li><a tabindex="-1" href="#">2</a></li>
                        <li><a tabindex="-1" href="#">3</a></li>
                    </ul>
              </li>
              <li class="dropdown-submenu">
                  <a class="dropdown-toggle" tabindex="-1" href="#">设备参数</a>
                    <ul class="dropdown-menu" aria-labelledby="dropdownMenu">
                        <li><a tabindex="-1" href="#">一次参数</a></li>
                        <li><a tabindex="-1" href="#">额定载流</a></li>
                    </ul>
              </li>
            <li role="separator" class="divider"></li>
            <li><a href="#">设备故障预案</a></li>
            <li><a href="#">相关定值单</a></li>
          </ul>
        </div>
    """
    return template



if __name__ == '__main__':
    user_dict={
        1:{'name':"user1",'pwd':"pwd1"},
        2:{'name':"user2",'pwd':"pwd2"},
        3:{'name':"user3",'pwd':"pwd3"}
    }
    asdf=list()
    app.run()


import os
print(os.__file__)
