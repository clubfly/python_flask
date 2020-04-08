from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime, Numeric
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsLicense(Base):
    __tablename__ = 'licenses'
 
    sn = Column(Integer, primary_key=True)
    license_key = Column(String)
    generate_type = Column(String)
    request_sn = Column(Integer, default=0)
    company_sn = Column(Integer, default=0)
    company_name = Column(String)
    encrypt_type = Column(String)
    license_feature = Column(String)
    version = Column(String)
    trial_type = Column(String)
    id_type = Column(String)
    hostid = Column(String)
    start_date = Column(String)
    expire_date = Column(String)
    connect_count = Column(Integer, default=0)
    server = Column(String)
    port = Column(String)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,license_key = None,
                      generate_type = None,
                      request_sn = 0,
                      company_sn = 0,
                      company_name = None,
                      encrypt_type = None,
                      license_feature = None,
                      version = "1.0.0",
                      trial_type = None,
                      id_type = None,
                      hostid = None,
                      start_date = None,
                      expire_date = None,
                      connect_count = 0,
                      server = None,
                      port = None,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.license_key = license_key
        self.generate_type = generate_type
        self.request_sn = request_sn
        self.company_sn = company_sn
        self.company_name = company_name
        self.encrypt_type = encrypt_type
        self.license_feature = license_feature
        self.version = version
        self.trial_type = trial_type
        self.id_type = id_type
        self.hostid = hostid
        self.start_date = start_date
        self.expire_date = expire_date
        self.connect_count = connect_count
        self.server = server
        self.port = port
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
