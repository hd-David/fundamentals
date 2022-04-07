from model import Nation, County, dbconnect, Town
from sqlalchemy import delete
from flask import Flask, jsonify
from sqlalchemy.orm.exc import NoResultFound

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
    try:
        town = session.query(Town).where(Town.id == town_dict['id']).one()
        session.delete(town)
        session.commit()
    except NoResultFound:
        return jsonify({"Not found" : "Invalid requuest"})
