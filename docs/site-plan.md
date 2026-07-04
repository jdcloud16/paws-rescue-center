# Paws Rescue Center Site Plan

## Product Purpose

Paws Rescue Center will help visitors discover adoptable animals and submit adoption applications. Rescue staff will use protected administrative pages to manage animals and review applications.

## User Roles

### Visitor

A visitor is not signed in.

Visitors can:

- View the homepage
- Browse adoptable pets
- View an individual pet profile
- Read about the rescue center
- Create an account
- Log in

### Registered User

A registered user is signed in.

Registered users can:

- Access all public pages
- Submit an adoption application
- View their submitted applications
- Log out

### Administrator

An administrator is an authorized staff member.

Administrators can:

- Access the administrative dashboard
- Add pets
- Edit pet information
- Change adoption status
- Remove pet records safely
- Review adoption applications
- Update application statuses

## Public Pages

### Home

Planned URL:

```text
/
```

Purpose:

- Introduce the rescue center
- Explain its mission
- Display featured pets
- Explain the adoption process
- Direct visitors to available pets

### Adoptable Pets

Planned URL:

```text
/pets
```

Purpose:

- Display available animals in a responsive card layout
- Show basic information for each pet
- Link to individual pet profiles

Navigation label:

```text
Adopt
```

### Pet Details

Planned URL:

```text
/pets/<pet_id>
```

Purpose:

- Display a pet’s complete profile
- Show adoption availability
- Provide an application call to action

### About

Planned URL:

```text
/about
```

Purpose:

- Explain the organization’s mission
- Describe the rescue and adoption process
- Provide general contact information

### Register

Planned URL:

```text
/register
```

Purpose:

- Allow visitors to create an account

### Login

Planned URL:

```text
/login
```

Purpose:

- Allow existing users to access their accounts

## Registered User Pages

### Submit Adoption Application

Planned URL:

```text
/pets/<pet_id>/apply
```

Purpose:

- Allow a signed-in user to apply for a specific pet
- Validate and save the application

### My Applications

Planned URL:

```text
/my-applications
```

Purpose:

- Display the user’s submitted applications
- Show the status of each application

## Administrator Pages

### Admin Dashboard

Planned URL:

```text
/admin
```

Purpose:

- Summarize pets and adoption applications
- Provide links to administrative actions

### Manage Pets

Planned URL:

```text
/admin/pets
```

Purpose:

- List all pet records
- Provide add, edit, and status-management actions

### Add Pet

Planned URL:

```text
/admin/pets/new
```

Purpose:

- Allow administrators to create a new pet record

### Edit Pet

Planned URL:

```text
/admin/pets/<pet_id>/edit
```

Purpose:

- Allow administrators to update an existing pet record

### Review Applications

Planned URL:

```text
/admin/applications
```

Purpose:

- View submitted adoption applications
- Update application statuses

## Navigation States

### Visitor Navigation

```text
Home | Adopt | About | Log In | Create Account
```

### Registered User Navigation

```text
Home | Adopt | About | My Applications | Log Out
```

### Administrator Navigation

```text
Home | Adopt | About | Admin Dashboard | Log Out
```

## Initial MVP Scope

The first working version will focus on:

- A reusable site layout
- Public informational pages
- Pet listings
- Individual pet profiles
- User registration and login
- Adoption applications
- Basic administrator management

Features such as email notifications, payments, live chat, and external shelter integrations are outside the initial scope.