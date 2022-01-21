# Phone book API
This application serves the purpose as a phone book database. The user can perform basic CRUD operations, such as:
- read the entire phonebook database
- add new contacts
- update existing contacts
- delete the contacts

Application exposes API over HTTP protocol and the user can manipulate and read the data by calling respective route or input the data into URL arguments.
- Application can be also run inside of a container. Example command once the container is built: `docker run app_name -d -p 80:80` if we want to run it in detached mode. It will listen on port 80, so we do not have to include it once the container was initiated.
 
## Functions of the application:
### READ function:
- user can read the database of all contacts by calling the `/contacts` route or via `Contacts` button from the main page
### Create function:
- user can add new contact to the database by providing the required values as URL arguments
	- example: `/add?name=foo&surname=bar&phone=123&address=baz_1` 
- once the entry is created phone book database is called
### Update function:
- user can update name, surname and phone number of existing entry by providing a contact ID and new name, surname and phone into URL arguments
  - example: `/update?id=1&name=foo&surname=bar&phone=123`
- once the contact is updated phone book database is called
### Delete function:
- user can delete the contact from the database by calling the person's ID as URL argument
  - example: `/delete?id=1`
- once the contact is deleted phone book database is called