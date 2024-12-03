# Financial Assistance Scheme Management System

This is a backend solution for managing financial assistance schemes for needy individuals and families. It provides the necessary REST API for any frontend to fulfil the objectives below, showcasing the backend logic and design, and database design.

## Objectives

This system will:

- allow the management of a fictitious set of financial assistance schemes;
- manage accounts of administrators in charge of management of schemes;
- save and update records of applicants who applied for schemes;
- advise users of schemes that each applicant can apply for;
- save the outcome of granting of schemes to applicants.

## Requirements

The language, framework and libraries used are as follow:

- [Python](https://www.python.org/) 3.10 and above
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/)

## Installation

1. Create and activate a virtual environment.
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```
2. Install FastAPI and SQLModel.
```
$ pip install "fastapi[standard]"
$ pip install "passlib[bcrypt]"
$ pip install sqlmodel
```

3. Run the server with:
```
$ fastapi dev app/main.py
```

4. Open your browser at http://127.0.0.1:8000/docs to view and test the API available.

## Usage

The following details the list of functions and their respective REST URLs provided by the system.

- Login/logout as applicant or administrator.
    - A root admin is created by default. User to replace password in `main.py` with your own hashed one.
    - *Feature to be implemented. See Todo[1].*
- List all administrators.
    - GET http://127.0.0.1:8000/admin/
    - Returns a list of administrators.
- Retrieve a single administrator.
    - GET http://127.0.0.1:8000/admin/{admin_id}
    - Returns an administrator or 404 if administrator not found.
- Create a new administrator.
    - POST http://127.0.0.1:8000/admin/
    - Provides username and password in request body.
    - *Password validation to be implemented. See Todo[2]*
- Update an administrator's details.
    - PATCH http://127.0.0.1:8000/admin/{admin_id}
    - Provides username or password in request body.
    - Returns an administrator or 404 if administrator not found.
    - *Password validation to be implemented. See Todo[2]*
- Delete an administrator.
    - DELETE http://127.0.0.1:8000/admin/{admin_id}
    - Returns an ok is true or 404 if administrator not found.
- List all applicants.
    - GET http://127.0.0.1:8000/applicants/
    - Returns a list of applicants.
- Retrieve a single applicant.
    - GET http://127.0.0.1:8000/applicants/{applicant_id}
    - Returns an applicant or 404 if applicant not found.
- Create a new applicant.
    - POST http://127.0.0.1:8000/applicant/
    - Provides username and password in request body.
    - *Password validation to be implemented. See Todo[2]*
- Update an applicant's details.
    - PATCH http://127.0.0.1:8000/applicants/{applicant_id}
    - Provides username or password in request body.
    - Returns an applicant or 404 if applicant not found.
    - *Password validation to be implemented. See Todo[2]*
- Delete an applicant.
    - DELETE http://127.0.0.1:8000/applicants/{applicant_id}
    - Returns an okay is true or 404 if applicant not found.
- Retrieve an applicant's profile.
    - GET http://127.0.0.1:8000/applicants/{applicant_id}/profile
    - Returns an applicant's profile or 404 if applicant or profile not found.
- Create an applicant's profile.
    - POST http://127.0.0.1:8000/applicants/{applicant_id}/profile
    - Provides age, gender, and salary in request body.
    - Returns the applicant's profile or 404 if applicant not found or 400 if profile already exist.
- Update an applicant's profile.
    - PATCH http://127.0.0.1:8000/applicants/{applicant_id}/profile
    - Provides age, gender, or salary in request body.
    - Returns an applicant's profile or 404 if applicant or profile not found.
- Remove an applicant's profile.
    - DELETE http://127.0.0.1:8000/applicants/{applicant_id}/profile
    - Returns an ok is true or 404 if applicant or profile not found.
- List all financial assistance schemes.
    - GET http://127.0.0.1:8000/schemes/
    - Returns a list of schemes.
- Retrieve a single scheme
    - GET http://127.0.0.1:8000/schemes/{scheme_id}
    - Returns a scheme or 404 if scheme not found.
- Create a new scheme.
    - POST http://127.0.0.1:8000/schemes/
    - Provides name, description, minimum_age, and maximum salary. 
- Update a scheme's details.
    - PATCH http://127.0.0.1:8000/schemes/{scheme_id}
    - Provides name, description, minimum_age, or maximum salary. 
    - Returns a scheme or 404 if scheme not found.
- Delete a scheme.
    - DELETE http://127.0.0.1:8000/schemes/{scheme_id}
    - Returns an okay is true or 404 if scheme not found.
- List all applications.
    - GET http://127.0.0.1:8000/applications/
    - Returns a list of applications.
- Retrieve a single application.
    - GET http://127.0.0.1:8000/applications/{application_id}
    - Returns an application or 404 if application not found.
- List all application by an applicant.
    - GET http://127.0.0.1:8000/applications/?applicant_id={applicant_id}
    - Returns a list of applications submitted by a single applicant.
- Create a new application.
    - POST http://127.0.0.1:8000/applications/
    - Provides applicant's id and scheme's id in request body.
- Approve or reject an application.
    - PATCH http://127.0.0.1:8000/applications/{application_id}/status/approved
    - PATCH http://127.0.0.1:8000/applications/{application_id}/status/rejected
    - Returns an application or 404 if application not found.
- Delete an application.
    - DELETE http://127.0.0.1:8000/applications/{application_id}
    - Returns an okay is true or 404 if application not found.

## Todo

1. Implementing [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/) for login and permission to functions based on user role.
2. Implementing password validation in terms of length and strength before hashing.
