# Simple python CRUD API

This repository serves as an example architecture of simple Python CRUD application. The application is used as a phone book where user can search for people's phone numbers and insert new ones.

## Tasks:
 - Create Python application that exposes API over HTTP protocol
 - Create application routes that allows user to interact with data
 - Application supports basic CRUD operation
   - Create
   - Read
   - Update
   - Delete
 - Application uses any kind of database backend
   - it is up to developer what kind of database is used
   - the simplest variant is `sqlite`
 - The phone book application stores following information
   - ID (unique, autogenerated)
   - Name
   - Surname
   - Phone
   - Address
 - Document your code
 - Create a documentation on how the application works
 - Split your git commits into logical pieces
 - Submit a pull-request to this repository with the solution

### Optional
 - Run application inside of container
   - Create a Dockerfile
   - Provide example command how the application can be executed

## Acceptance criteria
 - As an application user I can insert new person into phone book by providing required values into URL arguments
 - As an application user I can view all contacts in phone book
 - As an application user I can update name and phone of any contact by providing person's ID and new name and phone
 - As an application user I can delete contact by calling API route with person's ID


There are no limitations in terms of what libraries can be used. There are several examples on the internet how such an application can be created. I do recommend to search on the internet, but the final solution can't be just simple copy/paste from a tutorial.

The application doesn't need to have any UI. The output can just simple text printed on a screen.

In case you need any help, contact me at araszka@redhat.com.

Good luck!