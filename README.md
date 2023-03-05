So, the stack that I'm expected to build this with is:

- Python
- React.js
- Django REST framework
- Docker
- Go

This is the database schema:

![database schema](https://i.imgur.com/9gV6sQ6.png)

https://mui.com/material-ui/getting-started/installation/

Notes:

Because user authentication is not a core part of this assessment,

# API Routes

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
      "account_id": 1234567812345678,
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
      "message": "Validation Error",
      "statusCode": 400,
      "errors": {
        "account_id": "Account id is required.",
        "transaction_type": "Transaction must be either DEBIT or CREDIT",
        "note": "Transaction Note cannot be empty",
        "amount": "amount must be greater than 0"
      }
    }
    ```
* Error response: Account balance is not high enough for transaction
  * Status Code: 406
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Account balance too low",
      "statusCode": 406
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
