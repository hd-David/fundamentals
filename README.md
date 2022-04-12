## GLOBAL STATISTICS
install the following to run the application

*Python3
*Sqlalchemy
*Sqlite3
*Flask
*Postman on your machine

The application is about how can we use CRUD in an API. 
In the model.py,we are defining our class intances and database connection

In api.py is where the application is running from and the Endpoint for the application.
Since we defined our route in this app, all the requests are done in this app.

When the wrong data is entered and we realise that, we define the update.py. In this application, we send what we want to update as the request to the api. In our API we check the data recieved if exist on our database, if does not exist , we give our user data sent is invalid.

If we want to get ride of an entry, in our API, the delete.py handles that for us. The user send an id of the row the want to delete as the request. It is adviceble to user and id becuase when the name is used multiple rows will be deleted that match the the user's request.

To create an entry or add some data to our database, create.py does populate our dabase with data, when the user do a post the addTown function is called in our application.