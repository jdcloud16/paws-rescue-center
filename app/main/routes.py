from flask import abort, flash, redirect, render_template, url_for

from app.extensions import db
from app.main import bp
from app.forms import AdoptionApplicationForm, ContactForm
from app.models import AdoptionApplication, ContactMessage, Pet


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


@bp.route("/pets/<int:pet_id>/adopt", methods=["GET", "POST"])
def adoption_application_page(pet_id):
    pet = db.session.get(Pet, pet_id)

    if pet is None or not pet.is_available:
        abort(404)

    form = AdoptionApplicationForm()

    if form.validate_on_submit():
        application = AdoptionApplication(
            pet_id=pet.id,
            applicant_name=form.applicant_name.data,
            email=form.email.data,
            phone=form.phone.data,
            message=form.message.data,
        )

        db.session.add(application)
        db.session.commit()

        flash(
            f"Your adoption application for {pet.name} has been submitted.",
            "success",
        )

        return redirect(url_for("main.pet_details_page", pet_id=pet.id))

    return render_template(
        "adoption_application.html",
        title=f"Adopt {pet.name}",
        pet=pet,
        form=form,
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


@bp.route("/contact", methods=["GET", "POST"])
def contact_page():
    form = ContactForm()

    if form.validate_on_submit():
        contact_message = ContactMessage(
            sender_name=form.sender_name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data,
        )

        db.session.add(contact_message)
        db.session.commit()

        flash(
            "Your message has been sent. Our team will follow up soon.",
            "success",
        )

        return redirect(url_for("main.contact_page"))

    return render_template(
        "contact.html",
        title="Contact Us",
        form=form,
    )