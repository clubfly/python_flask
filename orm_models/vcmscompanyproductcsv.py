from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsCompanyProductCsv(Base):
    __tablename__ = 'company_product_csv'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer, default=0)
    user_file_name = Column(String)
    sys_file_name = Column(String)
    file_manage_mark = Column(Integer, default=0)
    file_manage_time = Column(DateTime, nullable=True)
    service_sn = Column(Integer, default=0)
    data_total = Column(Integer, default=0)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,company_sn = 0,
                      user_file_name = None,
                      sys_file_name = None,
                      file_manage_mark = 0,
                      file_manage_time = None,
                      service_sn = 0,
                      data_total = 0,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.company_sn = company_sn
        self.user_file_name = user_file_name
        self.sys_file_name = sys_file_name
        self.file_manage_mark = file_manage_mark
        self.file_manage_time = file_manage_time
        self.service_sn = service_sn
        self.data_total = data_total
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
