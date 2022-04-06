from model import Nation, County, dbconnect, Town
from sqlalchemy import update

""" 
    First we run querry to get the town we want to update using the town id and reference new values we want 
    to change and do commit.
    inputs:
        session - for the function to have access to the database.
        town_dict - type of (str) passing this parameter to get towns from db.
    outputs:
        updated town as a dictionary
"""
def update_town(session, town_dict):
    town = session.query(Town).where(Town.id == 2 ).one()
    #setting new values
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

    session.commit()

    return 'ok'