from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsRecognitionService(Base):
    __tablename__ = 'system_recognition_services'
 
    sn = Column(Integer, primary_key=True)
    service_name = Column(String)
    service_type = Column(String)
    feature_extraction_mark = Column(Integer, default=1)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,service_name = None,
                      service_type = None,
                      feature_extraction_mark = 1,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.service_name = service_name
        self.service_type = service_type
        self.feature_extraction_mark = feature_extraction_mark
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
