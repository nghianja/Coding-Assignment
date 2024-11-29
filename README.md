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
    - A root admin is created by default. User to replace password in `main.py` with a hashed one.
    - *Feature to be implemented. See Todo[1].*
- List all administrators.
- Create a new administrator.
- Update an administrator's details.
- Delete an administrator.
- List all applicants.
- Create a new applicant.
- Update an applicant's details.
- Delete an applicant.
- List all financial assistance schemes.
- Create a new scheme.
- Update a scheme's details.
- Delete a scheme.
- List all applications.
- Create a new application.
- Update an application's details.
- Delete an application.

## Todo

1. Implementing [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/) for login and permission to functions based on user role.
