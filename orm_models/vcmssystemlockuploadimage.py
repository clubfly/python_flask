from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsSystemLockUploadImage(Base):
    __tablename__ = 'system_lock_upload_images'
 
    sn = Column(Integer, primary_key=True)
    lock_token = Column(String)
    lock_mark = Column(Integer, default=0)
    lock_time = Column(DateTime, nullable=True)
    unlock_time = Column(DateTime, nullable=True)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)    
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,lock_token = None,
                      lock_mark = 0,
                      lock_time = None,
                      unlock_time = None,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.lock_token = lock_token
        self.lock_mark = lock_mark
        self.lock_time = lock_time
        self.unlock_time = unlock_time
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
