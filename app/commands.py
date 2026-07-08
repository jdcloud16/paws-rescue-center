import click

from app.extensions import db
from app.models import Pet


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


def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(seed_db_command)