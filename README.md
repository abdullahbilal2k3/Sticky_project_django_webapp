## Sticky Notes Web Application
### Project Overview
I have developed this personal Sticky Notes web application using the Django framework as part of my Web Engineering assignment. The application allows users to securely register, log in, and manage their own private collection of notes. Each user has a protected workspace where they can create, view, edit, and delete their sticky notes.

### Key Features
Secure Authentication: Built-in Django system for user registration, login, and logout.

Private CRUD Operations: Users can Create, Read, Update, and Delete only their own notes.

Dynamic Visuals: Each note card displays a user-defined background color, mimicking physical sticky notes.

Search Functionality: Users can filter through their notes using a search bar (Bonus Feature).

Pinning System: Important notes can be pinned to the top of the collection (Bonus Feature).

Delete Confirmation: A dedicated safety page to confirm before a note is permanently removed.

Technologies Used
Backend: Django (Python)

Database: SQLite

Frontend: HTML5, CSS3 (Template Inheritance)

Forms: Django ModelForms

Setup & Execution Instructions
1. Install Dependencies
Ensure you have Python and Django installed on your system.

2. Database Migrations
To set up the database schema, run the following commands in your terminal:

Bash
python manage.py makemigrations
python manage.py migrate
3. Create Administrator (Optional)
To access the admin dashboard, create a superuser:

Bash
python manage.py createsuperuser
4. Run the Application
Start the development server:

Bash
python manage.py runserver
Once the server is running, access the app at http://127.0.0.1:8000/