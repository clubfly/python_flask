from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsCompany(Base):
    __tablename__ = 'companies'
 
    sn = Column(Integer, primary_key=True)
    company_name = Column(String, nullable=True)
    max_admin_cnt = Column(Integer, default=5)
    max_branch_user_cnt = Column(Integer, default=5)
    max_branch_cnt = Column(Integer, default=5)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)    
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,company_name = None,
                      max_admin_cnt = 5,
                      max_branch_user_cnt = 5,
                      max_branch_cnt = 5,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.company_name = company_name
        self.max_admin_cnt = max_admin_cnt
        self.max_branch_user_cnt = max_branch_user_cnt
        self.max_branch_cnt = max_branch_cnt
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
