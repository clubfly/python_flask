from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsSystemAnnouncement(Base):
    __tablename__ = 'system_announcement'
 
    sn = Column(Integer, primary_key=True)
    board_hash = Column(String)
    publish_mark = Column(Integer, default=0)
    publish_time = Column(DateTime, nullable=True)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)    
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,board_hash = None,
                      publish_mark = 0,
                      publish_time = None,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.board_hash = board_hash
        self.publish_mark = publish_mark
        self.publish_time = publish_time
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
