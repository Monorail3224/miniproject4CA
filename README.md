# Polling App with Django

Welcome to the Polling App, a web application built with Django that allows users to create and participate in polls.

## Table of Contents

- [Overview](#overview)
- [Features](#key-key-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Overview

The Polling App is a web-based platform that enables users to create, manage, and participate in polls. It provides an interactive and user-friendly interface for both poll creators and voters.

### Key Features

- User registration and authentication.
- Creating and managing polls with custom questions and choices.
- Voting on polls.
- Viewing poll results in real-time.
- Admin panel for managing polls and user accounts.
- Responsive design with Bootstrap for a visually appealing user experience.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.11.1
- Django 4.2.6
- SQLite (or your preferred database)
- Additional dependencies (listed in [requirements.txt](requirements.txt))

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Monorail3224/miniproject4CA.git
   cd miniproject4CA

2. Create a Virtual Environment:

    ```shell
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Project Dependencies:
    ```shell
    pip install -r requirements.txt


4. Perform database migrations:
    ```shell
    python manage.py makemigrations
    python manage.py migrate

5. Create a SuperUser for the Admin Panel:
    ```shell
    python manage.py createsuperuser

6. Start the Development Server:
    ```shell
    python manage.py runserver


## Usage

    1. Register or log in to your account.

    2. Create a new poll with your custom questions and choices.

    3. Share the poll link with others to collect votes.

    4. View real-time poll results on the results page.

    5. Manage your polls and view user responses in the admin panel.