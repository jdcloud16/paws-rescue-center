from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional
from wtforms.validators import EqualTo

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


class RegistrationForm(FlaskForm):
    name = StringField(
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

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, max=128),
        ],
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )

    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=120),
        ],
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )

    remember_me = BooleanField("Remember Me")

    submit = SubmitField("Log In")