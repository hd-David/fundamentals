from app import Nation, County, dbconnect, Town
from flask import Flask, jsonify
from sqlalchemy import select, join

app = Flask(__name__)
session = dbconnect()


# input - county
# output - list of dictionary
@app.route('/query/<county>')
def query_data(county):
    output_counties = []
    counties = (
        session.query(Town)
        .join(Town.county)
        .where(County.name == "Essex")
        ).all()
    for county in counties:
        _county = county.__dict__
        del _county['_sa_instance_state']
        output_counties.append(_county)

    print(output_counties)
    return jsonify(output_counties)



if __name__ == '__main__':
    app.run(debug=True)