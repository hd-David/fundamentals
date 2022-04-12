from model import Nation, County, dbconnect, Town
from flask import Flask, request
from create import addTown
from read import getTown
from delete import delete_town
from update import update_town
from jsonschema import validate

app = Flask(__name__)

schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "grid_reference": { "type": "string" },
    "latitude":{"type": "number"},
    "longitude":{"type":"number"},
    "elevation":{"type": "integer"},
    "postcode_sector": {"type" : "string"}
  }
  
}



session = dbconnect()

# defining endpoints
@app.route('/town', methods = ['POST', 'GET', 'PATCH', 'PUT','DELETE']) 
def town():

    validate( instance=request.json, schema=schema, )
    
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