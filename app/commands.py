import click

from app.extensions import db
from app.models import Pet, User


@click.command("init-db")
def init_db_command():
    """Create database tables."""
    db.create_all()
    click.echo("Database tables created.")


@click.command("seed-db")
def seed_db_command():
    """Add starter pet records."""
    existing_pet = db.session.scalar(db.select(Pet).limit(1))

    if existing_pet is not None:
        click.echo("Database already has pet records.")
        return

    db.session.add_all([
        Pet(
            name="Luna",
            species="Dog",
            breed="Labrador Mix",
            age="2 years",
            description="Friendly, energetic, and loves outdoor walks.",
            is_available=True,
        ),
        Pet(
            name="Milo",
            species="Cat",
            breed="Domestic Shorthair",
            age="1 year",
            description="Calm, curious, and enjoys sunny windowsills.",
            is_available=True,
        ),
        Pet(
            name="Bella",
            species="Dog",
            breed="Beagle",
            age="4 years",
            description="Sweet, gentle, and great with families.",
            is_available=True,
        ),
    ])

    db.session.commit()
    click.echo("Seed pet records added.")


@click.command("create-admin")
@click.option("--name", prompt=True)
@click.option("--email", prompt=True)
@click.password_option("--password")
def create_admin_command(name, email, password):
    """Create an admin user."""
    existing_user = db.session.scalar(
        db.select(User).where(User.email == email.lower())
    )

    if existing_user is not None:
        click.echo("A user with that email already exists.")
        return

    user = User(
        name=name,
        email=email.lower(),
        is_admin=True,
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    click.echo(f"Admin user created: {email.lower()}")


def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(seed_db_command)
    app.cli.add_command(create_admin_command)