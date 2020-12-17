from app import app
from app.forms import LoginForm
from flask import render_template,flash,redirect,url_for

@app.route('/')

@app.route('/index')
def index():
    user = {
            'username':'dzp'
           }

    
    posts = [
        {
            'author':{'username': 'py'},
            'body':'hello'
        },
        
        {
            'author':{'username': 'thon'},
            'body':'world'  
        }
    ]
    return render_template('index.html', posts=posts,user=user)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        flash('用户登录的名户名是:{} , 是否记住我:{}'.format(
            form.username.data,form.remember_me.data))
        
        return redirect('/index')
    
    return render_template('login.html',title='登录',form=form)