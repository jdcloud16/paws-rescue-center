from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional


class AdoptionApplicationForm(FlaskForm):
    applicant_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(max=120),
        ],
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=120),
        ],
    )

    phone = StringField(
        "Phone",
        validators=[
            Optional(),
            Length(max=30),
        ],
    )

    message = TextAreaField(
        "Why would you be a good fit for this pet?",
        validators=[
            DataRequired(),
            Length(min=20, max=1000),
        ],
    )

    submit = SubmitField("Submit Application")

class ContactForm(FlaskForm):
    sender_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(max=120),
        ],
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=120),
        ],
    )

    subject = StringField(
        "Subject",
        validators=[
            DataRequired(),
            Length(max=150),
        ],
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(),
            Length(min=10, max=1000),
        ],
    )

    submit = SubmitField("Send Message")