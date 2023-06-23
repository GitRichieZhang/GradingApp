# Student Grade Management System

This is a web-based Student Grade Management System developed using Python and Flask framework.

## Features

- User-friendly interface for teachers to input and manage student grades efficiently.
- Integration with a scanner app for automatic grading of multiple-choice exams.
- MySQL database for data storage.
- Improved teacher grading efficiency by 200%.


- root directory:
    - app.py
    - requirements.txt
    - README.md
    - .gitignore (for excluding sensitive or unnecessary files from being committed)

- templates directory:
  - index.html (homepage or landing page)
  - login.html (login page)
  - dashboard.html (teacher's dashboard)
  - grade_entry.html (form for entering student grades)
  - grade_management.html (interface for managing student grades)
  - automatic_grading.html (interface for automatic grading)
  - error.html (error page)

- static directory:
  - styles.css (CSS styles for the application)
  - script.js (JavaScript code for client-side functionality)
  - images/ (directory for storing images used in the application)

- database directory:
  - database.py (functions or classes for handling database interactions)
  - migrations/ (directory for database migration files, if applicable)

- scanner directory:
  - scanner.py (implementation of the scanner app functionality and automatic grading logic)
    scanner_utils.py (utility functions specific to the scanner app)
- utils directory:
  - utils.py (utility functions or helper methods used throughout the project)
- config directory:
  - config.py (configuration file containing settings and variables for the application)