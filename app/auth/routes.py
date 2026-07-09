from flask import abort, flash, redirect, render_template, request, url_for
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


@bp.route("/admin/pets/new", methods=["GET", "POST"])
@login_required
@admin_required
def new_pet_page():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        species = request.form.get("species", "").strip()
        breed = request.form.get("breed", "").strip()
        age_raw = request.form.get("age", "").strip()
        is_available = "is_available" in request.form

        if not name or not species or not breed or not age_raw:
            flash("Please fill out all required fields.")
            return render_template(
                "auth/new_pet.html",
                title="Add Pet",
            )

        try:
            age = int(age_raw)
        except ValueError:
            flash("Age must be a number.")
            return render_template(
                "auth/new_pet.html",
                title="Add Pet",
            )

        existing_pet = db.session.scalar(
            db.select(Pet).filter_by(name=name)
        )

        if existing_pet:
            flash("A pet with that name already exists.")
            return render_template(
                "auth/new_pet.html",
                title="Add Pet",
            )

        pet = Pet(
            name=name,
            species=species,
            breed=breed,
            age=age,
            is_available=is_available,
        )

        db.session.add(pet)
        db.session.commit()

        flash(f"{pet.name} has been added.")
        return redirect(url_for("auth.admin_pets_page"))

    return render_template(
        "auth/new_pet.html",
        title="Add Pet",
    )

@bp.route("/admin/pets/<int:pet_id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_pet_page(pet_id):
    pet = db.get_or_404(Pet, pet_id)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        species = request.form.get("species", "").strip()
        breed = request.form.get("breed", "").strip()
        age_raw = request.form.get("age", "").strip()
        is_available = "is_available" in request.form

        if not name or not species or not breed or not age_raw:
            flash("Please fill out all required fields.")
            return render_template(
                "auth/edit_pet.html",
                title="Edit Pet",
                pet=pet,
            )

        try:
            age = int(age_raw)
        except ValueError:
            flash("Age must be a number.")
            return render_template(
                "auth/edit_pet.html",
                title="Edit Pet",
                pet=pet,
            )

        if age < 0:
            flash("Age cannot be negative.")
            return render_template(
                "auth/edit_pet.html",
                title="Edit Pet",
                pet=pet,
            )

        existing_pet = db.session.scalar(
            db.select(Pet).filter_by(name=name)
        )

        if existing_pet and existing_pet.id != pet.id:
            flash("Another pet with that name already exists.")
            return render_template(
                "auth/edit_pet.html",
                title="Edit Pet",
                pet=pet,
            )

        pet.name = name
        pet.species = species
        pet.breed = breed
        pet.age = age
        pet.is_available = is_available

        db.session.commit()

        flash(f"{pet.name} has been updated.")
        return redirect(url_for("auth.admin_pets_page"))

    return render_template(
        "auth/edit_pet.html",
        title="Edit Pet",
        pet=pet,
    )

@bp.route("/admin/pets/<int:pet_id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_pet_page(pet_id):
    pet = db.get_or_404(Pet, pet_id)
    pet_name = pet.name

    db.session.delete(pet)
    db.session.commit()

    flash(f"{pet_name} has been deleted.")
    return redirect(url_for("auth.admin_pets_page"))