from create import addTown
import csv 
from model import dbconnect


session = dbconnect()
#loading data from csv file
with open ("uk-towns-sample.csv", "r") as csvfile:
    reader =  csv.DictReader(csvfile)
    for town_dict in reader:
        addTown(session, town_dict)