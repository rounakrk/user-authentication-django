# User Authentication System

In this we are making a web app using django as the backend server and using it authentication system for user sign up and sign in functionality in any kind of system.

## Tech Stack

**FrontEnd:** HTML, CSS, Bootstrap CDN

**BackEnd:** Django(Python)

## Run Locally

Create your virtual environment

```bash
  python -m venv env
```

Activate your virtual environment

```bash
  cd env\Scripts
  activate
```

Clone the project

```bash
  git clone https://github.com/rounakrk/user-authentication-django.git
```

Go to the project directory

```bash
  cd user-authentication-django
```

Install dependencies using requirements.txt

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

If there are some migrations needed

```bash
  python manage.py makemigrations
  python manage.py migrate
```
Then re-run the server.

