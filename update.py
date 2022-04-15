from model import Nation, County, dbconnect, Town
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import update
import json, copy
from flask import jsonify

""" 
    First we run querry to get the town we want to update using the town id  do commit.
    inputs:
        session - for the function to have access to the database.
        town_dict - type of (str) passing this parameter to get towns.
    outputs:
        updated town as a dictionary
"""
def update_town(session, town_dict):
    # checking if the row exist
    query = session.query(Town).filter(Town.id == town_dict["id"] )
    query_check = copy.copy(query) # making a copy of the query
    try:
        query_check.one() 
        query_check.update(town_dict)  
        session.commit() 
    except NoResultFound:
        return jsonify({'message':"not results found"}), 404
    return jsonify({'message' : 'town update succesfully!'})
    