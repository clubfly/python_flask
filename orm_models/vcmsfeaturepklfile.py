from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsFeaturePklFile(Base):
    __tablename__ = 'feature_pkl_files'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer, default=0)
    service_sn = Column(Integer, default=0)
    branch_sn = Column(Integer, default=0)
    pkl_key = Column(String)
    pkl_update_send_mark = Column(Integer, default=0)
    pkl_update_send_time = Column(DateTime, nullable=True)
    pkl_update_finish_mark = Column(Integer, default=0)
    pkl_update_finish_time = Column(DateTime, nullable=True)
    output_pkl_mark = Column(Integer, default=0)
    output_pkl_time = Column(DateTime, nullable=True)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,company_sn = 0,
                      service_sn = 0, 
                      branch_sn = 0, 
                      pkl_key = None,
                      pkl_update_send_mark = 0,
                      pkl_update_send_time = None,
                      pkl_update_finish_mark = 0,
                      pkl_update_finish_time = None,
                      output_pkl_mark = 0,
                      output_pkl_time = None,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.company_sn = company_sn
        self.service_sn = service_sn
        self.branch_sn = branch_sn 
        self.pkl_key = pkl_key
        self.pkl_update_send_mark = pkl_update_send_mark
        self.pkl_update_send_time = pkl_update_send_time
        self.pkl_update_finish_mark = pkl_update_finish_mark
        self.pkl_update_finish_time = pkl_update_finish_time
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
