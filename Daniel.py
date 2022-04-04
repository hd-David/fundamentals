from app import Nation, County, dbconnect, Town
import csv
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

def addGetNation(session, nation_name_input):
    # Try and get the Nation from the database. If error (Except) add to the database.
    try:
        nation = session.query(Nation).filter(Nation.name == nation_name_input).one()
    except NoResultFound:
        nation = Nation()
        nation.name = town_dict["nation"]
    return nation

def addGetCounty(session, county_name_input, nation_name_input):
    # Try and get the County from the database. If error (Except) add to the database.
    try:
        county = session.query(County).filter(County.name == county_name_input).one()
    except NoResultFound:
        county = County()
        county.nation = addGetNation(session, town_dict["nation"])
        county.name = town_dict["county"]
    return county


def addTown(session, town_dict):
    # Try and get the Country from the database. If error (Except) add to the database.
    town = Town()
    # Add attributes
    town.county = addGetCounty(session, town_dict["nation"], town_dict["county"])
    town.name = town_dict["name"]
    town.grid_reference = town_dict["grid_reference"]
    town.easting = town_dict["easting"]
    town.northing = town_dict["northing"]
    town.latitude = town_dict["latitude"]
    town.longitude = town_dict["longitude"]
    town.elevation = town_dict["elevation"]
    town.postcode_sector = town_dict["postcode_sector"]
    town.local_government_area = town_dict["local_government_area"]
    town.nuts_region = town_dict["nuts_region"]
    town.town_type = town_dict["town_type"]
    # add the country (parent) to the county (child)
    try: 
        session.add(town)
        session.commit()
    except IntegrityError as error:
        session.rollback()

session = dbconnect()

with open ("uk-towns-sample.csv", "r") as csvfile:
    reader =  csv.DictReader(csvfile)
    for town_dict in reader:
        addTown(session, town_dict)
