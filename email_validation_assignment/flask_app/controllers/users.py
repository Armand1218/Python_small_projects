from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template("index.html", person = users)

@app.route('/new/user')
def new_user():
    return render_template("add_user.html")

@app.route('/add', methods = ['POST'])
def add():
    user_info = request.form
    if User.valid_user(user_info):
        User.save_db(user_info)
        print("PASS")
        return redirect('/')
    print("FAIL")
    return redirect('/new/user')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/')