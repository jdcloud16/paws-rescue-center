from datetime import datetime, timezone

from app.extensions import db


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    is_available = db.Column(db.Boolean, default=True, nullable=False)

    applications = db.relationship(
        "AdoptionApplication",
        backref="pet",
        lazy=True,
    )

    def __repr__(self):
        return f"<Pet {self.name}>"


class AdoptionApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey("pet.id"), nullable=False)
    applicant_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30), nullable=True)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), default="submitted", nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    def __repr__(self):
        return f"<AdoptionApplication {self.applicant_name} for pet_id={self.pet_id}>"