
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.routes.main import main
from app import db
from app.models.user import User
from app.models.post import Post

@main.route("/")
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("index.html", posts=posts)

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("main.index"))
        flash("Invalid credentials")
    return render_template("login.html")

@main.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Account created. Please log in.")
        return redirect(url_for("main.login"))
    return render_template("signup.html")

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@main.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        post = Post(title=title, body=body, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("new_post.html")
