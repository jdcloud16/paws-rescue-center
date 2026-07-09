# Paws Rescue Center QA Checklist

## Public Pages

- [ ] Home page loads
- [ ] Available Pets page loads
- [ ] About page loads
- [ ] Contact page loads
- [ ] Navbar links work
- [ ] Footer appears on all pages

## Authentication

- [ ] Register page loads
- [ ] Login page loads
- [ ] Invalid login shows a useful message
- [ ] Valid login redirects to dashboard
- [ ] Logout works

## Authorization

- [ ] Logged-out users cannot access dashboard
- [ ] Logged-out users cannot access admin area
- [ ] Non-admin users cannot access admin area
- [ ] Admin users can access admin area

## Admin Pet CRUD

- [ ] Admin can view all pets
- [ ] Admin can add a pet
- [ ] Admin can edit a pet
- [ ] Admin can delete a pet
- [ ] Duplicate pet names are blocked
- [ ] Invalid age values are blocked
- [ ] Flash messages appear after actions

## Visual Check

- [ ] Layout looks consistent
- [ ] Buttons are readable
- [ ] Tables are readable
- [ ] Forms are easy to use