from app import Nation, County, dbconnect
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length

class Createform(FlaskForm):
    name = StringField('name', validators= [ DataRequired(), Length(min=3 , max=15)])
    grid_reference = StringField('grid reference', validators= [ DataRequired() ])
    easting = IntegerField('easting', validators= [ DataRequired() ])
    northing = IntegerField('northing', validators= [ DataRequired()])
    latitude = FloatField(' latitude', validators= [DataRequired()])
    longitude = FloatField(' longitude', validators= [ DataRequired()])
    elevation = IntegerField(' elevation', validators= [ DataRequired()])
    postcode_sector = StringField(' postcode-sector', validators= [DataRequired()])
    local_government_area = StringField(' local goverment area', validators= [ DataRequired()])
    nuts_region = StringField(' nuts region', validators= [ DataRequired()])
    town_type = StringField(' town type', validators=[ DataRequired()])  

    submit = SubmitField('submit')