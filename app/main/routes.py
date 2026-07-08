from flask import abort, render_template

from app.extensions import db
from app.main import bp
from app.models import Pet


@bp.route("/")
def homepage():
    featured_pets = db.session.scalars(
        db.select(Pet)
        .where(Pet.is_available.is_(True))
        .order_by(Pet.name)
        .limit(2)
    ).all()

    return render_template(
        "home.html",
        title="Paws Rescue Center",
        featured_pets=featured_pets,
    )


@bp.route("/pets")
def pets_page():
    pets = db.session.scalars(
        db.select(Pet)
        .where(Pet.is_available.is_(True))
        .order_by(Pet.name)
    ).all()

    return render_template(
        "pets.html",
        title="Available Pets",
        pets=pets,
    )


@bp.route("/pets/<int:pet_id>")
def pet_details_page(pet_id):
    pet = db.session.get(Pet, pet_id)

    if pet is None or not pet.is_available:
        abort(404)

    return render_template(
        "pet_details.html",
        title=pet.name,
        pet=pet,
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