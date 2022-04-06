from model import Nation, County, dbconnect, Town
from sqlalchemy import delete, update
from flask import Flask, jsonify

session = dbconnect()

""" 
    First we run querry to get the town we want to delete using the town id and do commit.
    inputs:
        session - for the function to have access to the database.
        town_dict - type of (str) passing this parameter to get towns from db.
    outputs:
        strings in json format
"""
def delete_town(session, town_dict):
    town = session.query(Town).where(Town.id == 1 ).one()
    session.delete(town)
    session.commit()
    town_county = town.__dict__
    del town_county["_sa_instance_state"]
    return jsonify(town_county)
