from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsCompanyProfile(Base):
    __tablename__ = 'company_profiles'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer)
    company_name = Column(String, nullable=True)
    company_no = Column(String, nullable=True)
    company_address = Column(String, nullable=True)
    company_tel = Column(String, nullable=True)
    company_contact = Column(String, nullable=True)
    company_contact_tel = Column(String, nullable=True)
    company_contact_email = Column(String, nullable=True)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,company_sn = 0,
                      company_name = None,
                      company_no = None,
                      company_address = None,
                      company_tel = None,
                      company_contact = None,
                      company_contact_tel = None,
                      company_contact_email = None,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.company_sn = company_sn
        self.company_name = company_name
        self.company_no = company_no
        self.company_address = company_address
        self.company_tel = company_tel
        self.company_contact = company_contact
        self.company_contact_tel = company_contact_tel
        self.company_contact_email = company_contact_email
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn        
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
