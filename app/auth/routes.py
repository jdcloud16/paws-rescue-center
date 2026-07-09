from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app.auth import bp
from app.extensions import db
from app.forms import LoginForm, RegistrationForm
from app.models import Pet, User
from functools import wraps


def admin_required(view_function):
    @wraps(view_function)
    def wrapped_view(**kwargs):
        if not current_user.is_authenticated:
            return login_required(view_function)(**kwargs)

        if not current_user.is_admin:
            abort(403)

        return view_function(**kwargs)

    return wrapped_view


@bp.route("/register", methods=["GET", "POST"])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for("main.homepage"))

    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user = db.session.scalar(
            db.select(User).where(User.email == form.email.data.lower())
        )

        if existing_user is not None:
            flash("An account with that email already exists.", "error")
            return redirect(url_for("auth.register_page"))

        user = User(
            name=form.name.data,
            email=form.email.data.lower(),
        )
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Your account has been created. You can now log in.", "success")
        return redirect(url_for("auth.login_page"))

    return render_template(
        "auth/register.html",
        title="Create Account",
        form=form,
    )


@bp.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("main.homepage"))

    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.scalar(
            db.select(User).where(User.email == form.email.data.lower())
        )

        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password.", "error")
            return redirect(url_for("auth.login_page"))

        login_user(user, remember=form.remember_me.data)

        flash("You are now logged in.", "success")
        return redirect(url_for("main.homepage"))

    return render_template(
        "auth/login.html",
        title="Log In",
        form=form,
    )


@bp.route("/logout")
@login_required
def logout_page():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.homepage"))


@bp.route("/dashboard")
@login_required
def dashboard_page():
    return render_template(
        "auth/dashboard.html",
        title="Dashboard",
    )

@bp.route("/admin")
@login_required
@admin_required
def admin_page():
    return render_template(
        "auth/admin.html",
        title="Admin",
    )


@bp.route("/admin/pets")
@login_required
@admin_required
def admin_pets_page():
    pets = db.session.scalars(
        db.select(Pet).order_by(Pet.name)
    ).all()

    return render_template(
        "auth/admin_pets.html",
        title="Manage Pets",
        pets=pets,
    )