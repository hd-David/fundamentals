from model import Nation, County, dbconnect, Town
from flask import Flask, request, jsonify
from create import addTown
from read import getTown
from delete import delete_town
from update import update_town
from jsonschema import validate
from jsonschema import ValidationError
import json

app = Flask(__name__)

schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "grid_reference": { "type": "string" },
    "latitude": {"type": "number"},
    "longitude": {"type" :"number"},
    "elevation": {"type": "integer"},
    "postcode_sector": {"type" : "string"},
    "nuts_region": {"type": "string"},
    "northing": {"type": "integer"},
    "easting" : {"type": "integer"},
    "town_type": {"type": "string"},
    "local_government_area": {"type ": "string"}
  }
  
}

session = dbconnect()

# defining endpoints
@app.route('/town', methods = ['POST', 'GET', 'PATCH', 'PUT','DELETE']) 
def town():
    if request.method == 'GET':
        town_dict = {
            "county": request.args.get('county'),
            "name": request.args.get('name')
        }
        return getTown(session, town_dict)
        
    try:
        validate(instance=request.json, schema=schema)
    except ValidationError as error:
        print(error)
        error_message = {
                        "message": error.message,
                        "path" : list(error.path),
                        "validator" : error.validator,
                        "validator_value": error.validator_value,
                        }
        
        return jsonify(error_message)

    if request.method == 'POST': 
        addTown(session, request.json) 
        return 'Ok'
        
    if request.method == 'DELETE':
        return delete_town(session, request.json)
    
    if request.method == 'PATCH':
        return update_town(session, request.json)
        

if __name__ == '__main__':
    app.run(debug=True)