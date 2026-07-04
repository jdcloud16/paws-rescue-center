from flask import render_template

from app.main import bp


@bp.route("/")
def homepage():
    return render_template("home.html")


@bp.route("/pets")
def pets_page():
    return render_template(
        "pets.html",
        title="Available Pets",
    )


@bp.route("/about")
def about_page():
    return render_template(
        "about.html",
        title="About Us",
        description=(
            "We are a nonprofit organization dedicated to rescuing animals."
        ),
    )


@bp.route("/contact")
def contact_page():
    return render_template(
        "contact.html",
        title="Contact Us",
    )