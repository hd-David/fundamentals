from model import Nation, County, dbconnect, Town
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import update

""" 
    First we run querry to get the town we want to update using the town id  do commit.
    inputs:
        session - for the function to have access to the database.
        town_dict - type of (str) passing this parameter to get towns.
    outputs:
        updated town as a dictionary
"""
def update_town(session, town_dict):
    try:
        town = session.query(Town).where(Town.id == town_dict["id"] )
        #setting new values
        town.update(town_dict)     
        session.commit() 
    except NoResultFound:
        return "not results found", 404
    return "ok"
    