In the frontend folder:

```
npm install
npm start
```

In the backend folder:

```
pipenv shell
pip install requirements.txt
python manage.py migrate
```

in backend/app/settings.py, the default database is postgresql. Default credentials are provided, but if there is an environment variable set to DATABASE_URL, then that postgres URI will be used.

![database schema](https://i.imgur.com/9gV6sQ6.png)

https://mui.com/material-ui/getting-started/installation/



# API Routes

all urls prefixed with '/api'

## All endpoints that require authentication

All endpoints that require a current user to be logged in.

* Request: endpoints that require authentication
* Error Response: Require authentication
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "error": "Authentication credentials were not provided."
    }
    ```

## All endpoints that require proper authorization

All endpoints that require authentication and the current user does not have the
correct role(s) or permission(s).

* Request: endpoints that require proper authorization
* Error Response: Require proper authorization
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Forbidden",
      "statusCode": 401
    }
    ```

## Log In a User

Logs in a current user with valid credentials and returns the current user's
information.

* Require Authentication: false
* Request
  * Method: POST
  * URL: /user/login
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "username": "john.smith@gmail.com",
      "password": "secret password"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTU4MzIzNSwiaWF0IjoxNjc4MDQ3MjM1LCJqdGkiOiI1MTA0NDNjMjg4MGM0ZDVhOWQ5NTI0OTQzNjgyYmE5NSIsInVzZXJfaWQiOjJ9.fUYqM2Ang8nR7mKlrCOKjb8QDD__oDiGiJPDapSpE50",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5NTgzMjM1LCJpYXQiOjE2NzgwNDcyMzUsImp0aSI6ImE5ODFjNWE0NWQwNzRmMDY5ZTlhNTYzYzllOWVlNzA4IiwidXNlcl9pZCI6Mn0.XY5Ftqcft09WV7HVc_xWy4-fQRfMDdsIKlv5s0y6UOA",
        "username": "ichiroa"
    }
    ```

* Error Response: Invalid credentials
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "errors": ["No active account found with the given credentials"]
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "error": "Please provide both username/email and password"
    }
    ```

## Sign Up a User

Creates a new user, logs them in as the current user, and returns the current
user's information.

* Require Authentication: false
* Request
  * Method: POST
  * URL: /user/create
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "username": "JohnSmith",
      "email": "john.smith@gmail.com",
      "password": "secret password"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "username": "JohnSmith",
      "email": "john.smith@gmail.com",
    }
    ```

* Error response: User already exists with the specified email/password
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "errors":["User with this email or username already exists"]
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
  {
      "email": [
          "This field is required."
      ],
      "username": [
          "This field is required."
      ],
      "password": [
          "This field is required."
      ]
  }
    ```


## Get All Accounts by the Current User

Returns all the accounts owned by the user.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /accounts
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "Accounts":[
        {
          "id": 1,
          "account_number": 1234567812345678,
          "account_owner": 1,
          "current_balance": 3231.31,
        },
      ]
    }
    ```


## Create Account for the Current User

Creates and returns a new account for the user.

* Require Authentication: true
* Request
  * Method: POST
  * URL: /accounts/
  * Headers:
    * Content-Type: application/json
  * Body: None

* Successful Response
  * Status Code: 201
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "account_number": 1234567812345678,
    }
    ```

## Create a Transaction

Updates and returns an existing song.

* Require Authentication: true
* Require proper authorization: Account must belong to the current user
* Request
  * Method: POST
  * URL: /accounts/:accountId
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "account_id": 1,
      "transaction_type": "DEBIT",
      "note": "monthly job salary",
      "amount": 7750
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id" : 1,
      "account_number": "0123456701234567",
      "transaction_type": "DEBIT",
      "note": "monthly job salary",
      "amount": 7750
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "transaction_type": ["Transaction must be either DEBIT or CREDIT"],
      "note": ["Transaction note cannot be blank", "Ensure this field has no more than 50 characters."],
      "amount": ["Amount cannot be negative", "Amount cannot have more than 2 decimal places"]
    }
    ```
* Error response: Account balance is not high enough for transaction
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "error": "Insufficient funds",
    }
    ```

* Error response: Couldn't find an account with the specified id
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "error": "Account couldn't be found",
    }
    ```

## Get Balance of an Account

Returns the balance of an account by its id.

* Require Authentication: true
* Require proper authorization: Account must belong to the current user
* Request
  * Method: GET
  * URL: /accounts/:accountId
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
      {
          "id": 15,
          "account_number": "0000000000000001",
          "account_owner": 1,
          "current_balance": 0.0
      }
    ```
* Error response: Couldn't find an account with the specified id


## Get Transactions of An Account
Returns the transactions of an account by its id.

* Require Authentication: true
* Require proper authorization: Account must belong to the current user
* Request
  * Method: GET
  * URL: /accounts/:accountId/transactions
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    [
        {
            "transaction_type": "DEBIT",
            "amount": 200.23,
            "note": "1",
            "date": "2023-03-05T20:58:23.368308Z",
            "id": 2,
            "account_number": "0000000000000001"
        },
        {
            "transaction_type": "DEBIT",
            "amount": 1.11,
            "note": "41234132423",
            "date": "2023-03-05T21:09:41.555106Z",
            "id": 3,
            "account_number": "0000000000000001"
        },
    ]
    ```
* Error response: Couldn't find an account with the specified id

## Get all transactions of the user

Returns all the transactions of the user.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /transactions/all/
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
        "transactions": [
            {
                "transaction_type": "DEBIT",
                "amount": 200.23,
                "note": "1",
                "date": "2023-03-05T20:58:23.368308Z",
                "id": 2,
                "account_number": "0000000000000001"
            },
            {
                "transaction_type": "DEBIT",
                "amount": 1.11,
                "note": "41234132423",
                "date": "2023-03-05T21:09:41.555106Z",
                "id": 3,
                "account_number": "0000000000000001"
            },
        ]
    }
    ```
