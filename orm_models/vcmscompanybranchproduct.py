from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsCompanyBranchProduct(Base):
    __tablename__ = 'company_branch_products'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer)
    service_sn = Column(Integer)
    branch_sn = Column(Integer)
    product_sn = Column(Integer)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,company_sn = 0,
                      service_sn = 0,
                      branch_sn = 0,
                      product_sn = 0,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.company_sn = company_sn
        self.service_sn = service_sn
        self.branch_sn = branch_sn
        self.product_sn = product_sn
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn        
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
