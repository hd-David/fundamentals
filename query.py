from model import Nation, County, dbconnect, Town
from flask import Flask, jsonify
from sqlalchemy import select, join
import copy

app = Flask(__name__)
session = dbconnect()


# input - county
# output - list of dictionary
@app.route('/query/<county>')
def query_data(county):
    output_counties = []
    towns = (
        session.query(Town)
        .join(Town.county)
        .join(County.nation)
        .where(County.name == county)
        ).all()
    for town in towns:
        
        _town = copy.copy(town).__dict__
        del _town['_sa_instance_state']
        _town['county_name'] = town.county.name
        _town['nation_name'] = town.county.nation.name
        output_counties.append(_town)
    return jsonify(output_counties)


@app.route('/get-nation/<nation>')
def get_nation(nation):
    nations_output = []
    nations = (session.query(Nation).join(Nation.county).where(Nation.name == nation)).all()
    for nation in nations:
        _nation = nation.__dict__
        del _nation['_sa_instance_state']
        nations_output.append(_nation)
        print(_nation)
    return jsonify(nations_output)


@app.route('/update-nation/<nation>/<Newnation>')
def update_nation(nation, Newnation):
    
if __name__ == '__main__':
    app.run(debug=True)