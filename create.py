from model import Nation, County, dbconnect, Town
from flask import Flask, request
from enter import addTown
from read import getTown
from delete import delete_town
from update import update_town

app = Flask(__name__)

session = dbconnect()
# defining endpoints
@app.route('/town', methods = ['POST', 'GET', 'PATCH', 'PUT','DELETE']) 
# defining the function without pasing arguments
def town():
    if request.method == 'POST':
        addTown(session, request.json) 
        return 'ok'

    if request.method == 'GET':
        return getTown(session, request.json)

    if request.method == 'DELETE':
        return delete_town(session, request.json)
    
    if request.method == 'PUT':
        return update_town(session, request.json)
        

if __name__ == '__main__':
    app.run(debug=True)