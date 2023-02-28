So, the stack that I'm expected to build this with is:

Python
React.js
Django REST framework
Docker
Go

This is the database schema:

![database schema](https://i.imgur.com/9gV6sQ6.png)

First name, last name, additional user information is intentionally left out for this demo.

https://mui.com/material-ui/getting-started/installation/

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
      "message": "Authentication required",
      "statusCode": 401
    }
    ```

## All endpoints that require proper authorization

All endpoints that require authentication and the current user does not have the
correct role(s) or permission(s).

* Request: endpoints that require proper authorization
* Error Response: Require proper authorization
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Forbidden",
      "statusCode": 403
    }
    ```

## Get the Current User

Returns the information about the current user that is logged in.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /users/current
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "email": "john.smith@gmail.com",
      "username": "JohnSmith",
    }
    ```

## Log In a User

Logs in a current user with valid credentials and returns the current user's
information.

* Require Authentication: false
* Request
  * Method: POST
  * URL: /session
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "credential": "john.smith@gmail.com",
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
      "id": 1,
      "firstName": "John",
      "lastName": "Smith",
      "email": "john.smith@gmail.com",
      "username": "JohnSmith",
      "previewImage": "url"
    }
    ```

* Error Response: Invalid credentials
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Invalid credentials",
      "statusCode": 401
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "email": "Email is required",
        "password": "Password is required"
      }
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


## Create an Account for the Current User

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
        "id": 1,
        "account_number": 1234567812345678,
        "account_owner": 1,
        "current_balance": 3231.31,
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
      "account_id": 1234567812345678,
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
      "message": "Account couldn't be found",
      "statusCode": 404
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
        "account_number" : 1234567812345678,
        "current_balance" : 400
    }
    ```
* Error response: Couldn't find an account with the specified id
