from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    ForeignKey,
    UniqueConstraint,
    PrimaryKeyConstraint
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

class Station(Base):
    __tablename__ = 'station'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))

class Phase(Base):
    '''
    denotes multiple phases/routes of metro
    '''
    __tablename__ = 'phase'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))

class Route(Base):
    '''
    denotes series of stations along different phases of metro.
    '''
    __tablename__ = 'route'
    id = Column(Integer, primary_key=True)
    phase_id = Column(Integer, ForeignKey('phase.id'))
    station_id = Column(Integer, ForeignKey('station.id'))
    order = Column(Integer, nullable=False, autoincrement=False)
    __table_args__ = (UniqueConstraint(phase_id, station_id, order),)


Index('my_index', MyModel.name, unique=True, mysql_length=255)


