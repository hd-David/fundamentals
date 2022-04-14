## GLOBAL STATISTICS
install the following to run the application

*Python3
*Sqlalchemy
*Sqlite3
*Flask
*Postman on your machine

`The application is about how can we use CRUD in an API. 
In the model.py,we are defining our class intances and database connection
`

`In api.py is where the application is running from and the Endpoint for the application.
Since we defined our route in this app, all the requests are done in this app.
`
`In update.py the user run a query to check if the row they want to update does exist. In our API we check the data recieved if exist on our database, if does not exist , we send feedback results not find .
`
`In delete.py the user run a query to check if the row they want to delete is on the database. It is adviceble to use an id becuase when the name is used multiple rows will be deleted that matchs the user's request.
`
`To create an entry or add some data to our database, create.py does populate our dabase with data, when the user do a post the addTown function is called in our application.
`