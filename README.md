# Django User Management Project

This is a simple Django project named **myapp** that demonstrates basic user management functionality. It includes a User model with username, email, and password fields, and provides views to display a test message and a list of users.

## Prerequisites

- Python 3.x
- Django 5.2.1 (or compatible version)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd proj2
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install django
```

4. Apply database migrations:

```bash
python manage.py migrate
```

## Running the Development Server

Start the Django development server with:

```bash
python manage.py runserver
```

By default, the server will run at `http://127.0.0.1:8000/`.

## Usage

- Access the test view at: `http://127.0.0.1:8000/test/` (displays a simple hello world message).
- Access the users list view at: `http://127.0.0.1:8000/users/` to see all users displayed using the `users.html` template.

## Project Structure

```
proj2/
│
├── config/                  # Django project configuration
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   └── ...
│
├── myapp/                   # Django app containing user management
│   ├── migrations/          # Database migrations
│   ├── static/myapp/        # Static files (CSS, JS)
│   ├── templates/           # HTML templates
│   ├── admin.py             # Admin site configuration
│   ├── models.py            # User model definition
│   ├── views.py             # View functions
│   ├── urls.py              # App URL routing
│   └── ...
│
├── db.sqlite3               # SQLite database file
├── manage.py                # Django management script
└── README.md                # This file
```

## Notes

- This project uses SQLite as the database backend.
- Static files are served from the `/static/` URL path.
- The project is configured for development use with `DEBUG=True`.

## License

This project is provided as-is without any specific license.
