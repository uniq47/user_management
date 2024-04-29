### User Management

#

```
This Django application that provies a simple user management with CURD where we can see list of all the existing users, Creat user, Update user and Delete user
```

### Installation

```
pip install -r requirements.txt

```

### Now you can run the project with this command

```
python manage.py runserver
```

### API Endpoints

```
to access the swagger documentation

http://127.0.0.1:8000/swagger/


Create User

_______________________________________________________
POST /users/
Body:
{
    "user_id": 1,
    "user_name": "usapkota",
    "first_name": "uniq",
    "last_name": "sapkota",
    "email": "usap@example.com",
    "user_status": "I",
    "department": "string"
  }



Read Users
_______________________________________________________
GET /users
Response: Returns a list of all users


Update User
_______________________________________________________
PUT /users/{user_id}
Body:

  {
    "user_name": "shantisapkota",
    "first_name": "shanti",
    "last_name": "sapkota",
    "email": "shantisapkota@example.com",
    "user_status": "I",
    "department": "string"
  }



Delete User
_______________________________________________________
DELETE /users/{user_id}


```
