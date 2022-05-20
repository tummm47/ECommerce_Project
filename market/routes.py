from market import app
from flask import render_template, redirect, url_for, request, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm
from market import db


@app.route("/")
def base_page():
    return render_template("base.html")


@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("market_page"))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}')
    return render_template("register.html", form=form)
