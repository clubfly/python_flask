from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsUserRank(Base):
    __tablename__ = 'system_user_ranks'
 
    sn = Column(Integer, primary_key=True)
    rank_name = Column(String)
    rank_function = Column(String)
    rank_js = Column(String)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,rank_name = None,
                      rank_function = None,
                      rank_js = None,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.rank_name = rank_name
        self.rank_function = rank_function
        self.rank_js = rank_js
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
