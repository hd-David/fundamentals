from model import Nation, County, dbconnect, Town
import copy

""" 
    First we run querry to get the town and add the county and nation name 
    inputs:
        session - for the function to have access to the database.
        town_dict - type of (str) passing this parameter to get towns from db.
    outputs:
        strings in json format
"""
def getTown(session, town_dict):
    town = (
        session.query(Town)
        .join(Town.county)
        .join(County.nation)
        .where(County.name == town_dict["county"])
        .where(Town.name == town_dict["name"])
        ).one()
    town_county = copy.copy(town).__dict__
    del town_county["_sa_instance_state"]
    town_county["county"] = town.county.name
    town_county["nation"] = town.county.nation.name
    return town_county