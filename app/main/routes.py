from flask import abort, render_template

from app.main import bp
from app.main.data import PETS


@bp.route("/")
def homepage():
    return render_template(
        "home.html",
        title="Paws Rescue Center",
        featured_pets=PETS[:2],
    )


@bp.route("/pets")
def pets_page():
    return render_template(
        "pets.html",
        title="Available Pets",
        pets=PETS,
    )


@bp.route("/pets/<int:pet_id>")
def pet_details_page(pet_id):
    pet = None

    for current_pet in PETS:
        if current_pet["id"] == pet_id:
            pet = current_pet
            break

    if pet is None:
        abort(404)

    return render_template(
        "pet_details.html",
        title=pet["name"],
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
