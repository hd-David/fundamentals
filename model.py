from sqlalchemy import Table, Column,Integer, String, ForeignKey,Numeric, MetaData,Float, inspect
from sqlalchemy import create_engine, insert, update, delete, select, UniqueConstraint,DateTime, join
from sqlalchemy.orm import sessionmaker,relation
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


Base  = declarative_base()

# Country is currently the "parent" of everything. It is the "root".
class Nation(Base):
    __tablename__ = 'nation'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))


class County(Base):
    __tablename__ = 'county'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    # We define the relationship between Country and County here.
    nation = relation("Nation", backref="county")
    nation_id = Column(Integer, ForeignKey('nation.id'))


# County is a child of Country
class Town(Base):
    __tablename__ = 'town'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    grid_reference = Column(String(64))
    easting = Column(Integer)
    northing = Column(Integer)
    latitude = Column(Float) 
    longitude = Column(Float)
    elevation = Column(Integer)
    postcode_sector = Column(String(64))
    local_government_area = Column(String(64))
    nuts_region = Column(String(64))
    town_type = Column(String(64))
    # We define the relationship between town and County here.
    county = relation("County", backref="town")
    county_id = Column(Integer, ForeignKey('county.id'))
    UniqueConstraint(grid_reference, name='uix_1')

class TownSchema(SQLAlchemyAutoSchema):
    class meta:
        fields = ('id', 'name', 'grid_reference', 'easting', 'northing', 'latitude',
         'longitude', 'elevation', 'postcode_sector', 'local_government_area', 'nuts_region', 'town_type')

    
# database connection
def dbconnect():
    engine = create_engine("sqlite:///my.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
