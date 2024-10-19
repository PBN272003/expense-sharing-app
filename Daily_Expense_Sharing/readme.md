1. Project Overview

# Daily Expense Sharing Application

This is a backend implementation of a Daily Expense Sharing Application, where users can create expenses and share them with other participants. The app supports splitting expenses equally, by exact amounts, or by percentages. The users can also download a balance sheet of their expenses in an Excel format.

## Features
- User registration and authentication using JWT (JSON Web Tokens)
- Expense creation with optional fields like `date` and `description`
- Expense splitting among participants (Equal, Exact, Percentage)
- Generation of a downloadable balance sheet in Excel

2. Project Structure

## Project Structure

expense_sharing_app/
│
├── manage.py
├── requirements.txt
├── expense_sharing_app/   # Main project settings and configurations
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/                 # User management (registration, authentication)
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
└── expenses/              # Expense management (create, split, balance sheet)
    ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── utils.py

3. Setup Instructions

## Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL (or SQLite for simpler setup)
- `pip` for Python package management
- Git

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PBN272003/expense-sharing-app.git
   cd expense-sharing-app

4. Set up a virtual environment:

python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

5. Install the required dependencies:

pip install -r requirements.txt

6. Setting Up the Database:

If you're using SQLite (default Django setting), no additional configuration is needed.

For PostgreSQL, update the DATABASES setting in settings.py with your PostgreSQL credentials.

Example:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'expense_sharing_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

7. Apply migrations to set up the database schema:

python manage.py makemigrations
python manage.py migrate

8. Create a superuser for admin access (optional but recommended):

python manage.py createsuperuser

9. Run the development server:

python manage.py runserver

Access the API and admin panel:

API: http://127.0.0.1:8000/api/users/register/
Admin panel: http://127.0.0.1:8000/admin/

### **API Endpoints**
Document the main API endpoints for users and expenses:

```markdown
## API Endpoints

### User Endpoints

- **Register** (POST): `/api/users/register/`
  - Request Body:
    ```json
    {
      "username": "newuser",
      "email": "newuser@example.com",
      "password": "yourpassword",
      "mobile_number": "1234567890"
    }
    ```

- **Login** (POST): `/api/users/token/`
  - Request Body:
    ```json
    {
      "username": "newuser",
      "password": "yourpassword"
    }
    ```

- **Get Profile** (GET): `/api/users/profile/` (Authenticated)

### Expense Endpoints

- **Create Expense** (POST): `/api/expenses/`
  - Request Body:
    ```json
    {
      "amount": 500,
      "split_type": "EQUAL",
      "description": "Dinner at restaurant",
      "date": "2024-10-19",
      "participants": [
        {
          "user": 1,
          "amount_owed": 250
        },
        {
          "user": 2,
          "amount_owed": 250
        }
      ]
    }
    ```
- **Viewing Balances** (GET): `/api/expenses/balances/` (Authenticated)

- **List Expenses** (GET): `/api/expenses/` (Authenticated)

- **Download Balance Sheet** (GET): `/api/expenses/download_balance_sheet/` (Authenticated)

- **Postman** for API testing (optional)

## Technologies Used

- **Django**: Backend web framework
- **Django REST Framework**: For building the REST APIs
- **PostgreSQL**: (Optional) For database management
- **SQLite**: Default database used for quick setup
- **JWT**: JSON Web Token for user authentication
- **OpenPyXL**: For generating downloadable Excel balance sheets
- **Python 3.10+**: Language used for backend logic
- **Postman API**: For API testing

######Using Postman to Test the API##############
Setting up Postman
Postman is a tool you can use to test API endpoints. You can download it from Postman’s official website.

Once installed, you can use Postman to:

Test User Authentication (register, login, get profile).
Create Expenses and split them among participants.
Download Balance Sheets in Excel format.

Testing the Endpoints
1. Register a New User
Method: POST
URL: http://127.0.0.1:8000/api/users/register/
Body: (raw JSON)
json
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "password123",
    "mobile_number": "1234567890"
}
2. Login to Obtain JWT Token
Method: POST

URL: http://127.0.0.1:8000/api/users/token/

Body: (raw JSON)

json
{
    "username": "testuser",
    "password": "password123"
}
The response will include:

json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
3. Make Authenticated Requests Using JWT
Create Expense Example:
Method: POST
URL: http://127.0.0.1:8000/api/expenses/
Headers: Add Authorization: Bearer <access_token> in the headers (replace <access_token> with the token you got from the login).
Body: (raw JSON)
json
{
    "amount": 500,
    "split_type": "EQUAL",
    "description": "Dinner at restaurant",
    "date": "2024-10-19",
    "participants": [
        {
            "user": 1,
            "amount_owed": 250
        },
        {
            "user": 2,
            "amount_owed": 250
        }
    ]
}
4. Download Balance Sheet
Method: GET
URL: http://127.0.0.1:8000/api/expenses/download_balance_sheet/
Headers: Add Authorization: Bearer <access_token>
The response will return an Excel file with the balance sheet.


## Testing the Project

1. **Using Django Admin**:
   You can manage users, expenses, and participants via the Django admin panel at `http://127.0.0.1:8000/admin/` after creating a superuser.

2. **Using Postman**:
   You can test the API endpoints using Postman or any API testing tool by making requests to the endpoints documented above. For endpoints requiring authentication, use the JWT token obtained from the login endpoint in the Authorization header.

3. **Run Automated Tests**:
   (If you have implemented tests)
   ```bash
   python manage.py test

