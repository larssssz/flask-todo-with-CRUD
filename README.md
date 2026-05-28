Flask Todo Application with REST API Enhancement
Project Overview

This project is an enhancement of the original Flask Todo application created by Patrick Loeber. The original application is a simple task management system with a web interface.

In this version, a REST API has been added to provide full CRUD (Create, Read, Update, Delete) functionality. This allows the application to be used programmatically using HTTP requests and JSON data, making it suitable for integration with other systems.

Original Repository

https://github.com/patrickloeber/flask-todo

Features Implemented

The following REST API features have been implemented:

Create a new task
Retrieve all tasks
Retrieve a specific task by ID
Update an existing task
Delete a task

The API follows RESTful principles and uses standard HTTP methods.

API Endpoints
Retrieve all tasks

GET /api/tasks

Retrieve a task by ID

GET /api/tasks/

Create a new task

POST /api/tasks
Request body (JSON):
{
"title": "Task title"
}

Update an existing task

PUT /api/tasks/
Request body (JSON):
{
"title": "Updated title",
"done": true
}

Delete a task

DELETE /api/tasks/

Error Handling

The API includes proper error handling and returns appropriate HTTP status codes such as:

200 OK for successful requests
201 Created for successful resource creation
400 Bad Request for invalid input
404 Not Found for invalid task IDs
Testing

Unit tests have been implemented to verify all CRUD operations.

The tests include:

Creating a task
Retrieving tasks
Updating a task
Deleting a task
Handling invalid inputs and error cases
Running Tests

Execute the following command:

python -m unittest

Installation and Setup
Clone the repository

git clone https://github.com/larssssz/flask-todo-with-CRUD.git
cd flask-todo-with-CRUD


Install dependencies

pip install flask

Run the application

python app.py

Purpose of the Enhancement

The purpose of this enhancement is to extend the original Flask Todo application by adding backend REST API functionality. This allows the application to be used not only through a web interface but also through API calls, making it more flexible and suitable for modern application development.

