from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime, Numeric
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsLicenseRequest(Base):
    __tablename__ = 'license_requests'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer, default=0)
    company_name = Column(String)
    encrypt_sn = Column(Integer, default=0)
    encrypt_type = Column(String)
    service_sn = Column(Integer, default=0)
    service_name = Column(String)
    license_feature = Column(String)
    version = Column(String)
    trial_sn = Column(Integer, default=0)
    trial_type = Column(String)
    id_sn = Column(Integer, default=0)
    id_type = Column(String)
    hostid = Column(String)
    start_date = Column(String)
    expire_date = Column(String)
    connect_count = Column(Integer, default=0)
    server = Column(String)
    port = Column(String)
    license_count = Column(Integer, default=0)
    batch_license_count = Column(Integer, default=0)
    batch_update_send_mark = Column(Integer, default=0)
    batch_update_send_time = Column(DateTime, nullable=True)
    batch_update_finish_mark = Column(Integer, default=0)
    batch_update_finish_time = Column(DateTime, nullable=True)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,company_sn = 0,
                      company_name = None,
                      encrypt_sn = 0,
                      encrypt_type = None,
                      service_sn = 0,
                      service_name = None,
                      license_feature = None,
                      version = "1.0.0",
                      trial_sn = 0,
                      trial_type = None,
                      id_sn = 0,
                      id_type = None,
                      hostid = None,
                      start_date = None,
                      expire_date = None,
                      connect_count = 0,
                      server = None,
                      port = None,
                      license_count = 0,
                      batch_license_count = 0,
                      batch_update_send_mark = 0,
                      batch_update_send_time = None,
                      batch_update_finish_mark = 0,
                      batch_update_finish_time = None,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.company_sn = company_sn
        self.company_name = company_name
        self.encrypt_sn = encrypt_sn
        self.encrypt_type = encrypt_type
        self.service_sn = service_sn
        self.service_name = service_name
        self.license_feature = license_feature
        self.version = version
        self.trial_sn = trial_sn
        self.trial_type = trial_type
        self.id_sn = id_sn
        self.id_type = id_type
        self.hostid = hostid
        self.start_date = start_date
        self.expire_date = expire_date
        self.connect_count = connect_count
        self.server = server
        self.port = port
        self.license_count = license_count
        self.batch_license_count = batch_license_count
        self.batch_update_send_mark = batch_update_send_mark
        self.batch_update_send_time = batch_update_send_time
        self.batch_update_finish_mark = batch_update_finish_mark
        self.batch_update_finish_time = batch_update_finish_time
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
