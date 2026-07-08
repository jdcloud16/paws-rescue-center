from app.extensions import db


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    is_available = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<Pet {self.name}>"