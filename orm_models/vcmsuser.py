from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsUser(Base):
    __tablename__ = 'users'
 
    sn = Column(Integer, primary_key=True)
    account = Column(String)
    passwords = Column(String)
    company_sn = Column(Integer, default=0)
    lock_mark = Column(Integer, default=0)
    lock_time = Column(DateTime, nullable=True)
    lock_reason = Column(String, nullable=True)
    user_rank_sn = Column(Integer, default=2)
    last_login_time = Column(DateTime, nullable=True)
    company_branch_sn = Column(Integer, default=0)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,account = None,
                      passwords = None,
                      company_sn = 0,
                      lock_mark = 0, 
                      lock_time = None, 
                      lock_reason = None,
                      user_rank_sn = 2,
                      last_login_time = None,
                      company_branch_sn = 0,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.account = account
        self.passwords = passwords
        self.company_sn = company_sn
        self.lock_mark = lock_mark
        self.lock_time = lock_time
        self.lock_reason = lock_reason
        self.user_rank_sn = user_rank_sn
        self.last_login_time = last_login_time
        self.company_branch_sn = company_branch_sn
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
