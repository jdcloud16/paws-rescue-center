# Paws Rescue Center

Paws Rescue Center is a Flask web application for a fictional animal rescue organization. The app allows visitors to view adoptable pets and allows admin users to manage pet listings through a protected admin area.

## Project Purpose

This project was built as a portfolio-ready Flask application to demonstrate:

- Flask application structure
- Routing and templates
- User authentication
- Admin-only authorization
- Database models with SQLAlchemy
- CRUD operations
- Form handling
- Flash messages
- Manual QA documentation
- Git-based development workflow

## Features

### Public Features

- Home page
- Available pets page
- About page
- Contact page
- Responsive navigation
- Shared base layout using Jinja template inheritance

### Authentication Features

- User registration
- User login
- User logout
- Protected user dashboard
- Flash messages for user feedback

### Admin Features

- Admin-only dashboard
- View all pets
- Add new pets
- Edit existing pets
- Delete pets
- Prevent duplicate pet names
- Validate required pet form fields
- Validate pet age values

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite
- Jinja2
- HTML
- CSS
- Git and GitHub

## Project Structure

```text
paws-rescue-center/
├── app/
│   ├── auth/
│   │   └── routes.py
│   ├── main/
│   │   └── routes.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── auth/
│   │   ├── main/
│   │   └── base.html
│   ├── __init__.py
│   └── models.py
├── instance/
├── QA.md
├── README.md
└── requirements.txt