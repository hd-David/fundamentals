from app import dbconnect, Town, County, Nation
import csv
from sqlalchemy.orm.exc import NoResultFound

# SQL Errors
from sqlalchemy.orm.exc import NoResultFound


def addGetNation(session, nation_name_input):
    
    try:    # checking if nation exist in the database
        nation = session.query(Nation).filter(Nation.name == nation_name_input).one()
    except NoResultFound: # if it does not exist, create one
        nation = Nation()
        nation.name = nation_name_input
    return nation

def addGetCounty(session, county_name_input, nation_name_input):
    
    try:     # checking if county exist in the database
        county = session.query(County).filter(County.name == county_name_input).one()
    except NoResultFound:  # if it does not exist, create one
        county = County()
        county.nation = addGetNation(session, nation_name_input)
        county.name = county_name_input
    return county
    
def addTown(session, town_input):
    # Try and get the Country from the database. If error (Except) add to the database.
    town = Town()
    # Add attributes
    town.county = addGetCounty(session, town_input["county"], town_input["nation"])
    town.name = town_input["name"]
    town.grid_reference = town_input["grid_reference"]
    town.easting = town_input["easting"]
    town.northing = town_input["northing"]
    town.latitude = town_input["latitude"]
    town.longitude = town_input["longitude"]
    town.elevation = town_input["elevation"]
    town.postcode_sector = town_input["postcode_sector"]
    town.local_government_area = town_input["local_government_area"]
    town.nuts_region = town_input["nuts_region"]
    town.town_type = town_input["town_type"]