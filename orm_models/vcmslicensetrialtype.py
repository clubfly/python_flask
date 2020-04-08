from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsLicenseTrialType(Base):
    __tablename__ = 'license_trial_types'
 
    sn = Column(Integer, primary_key=True)
    trial_type = Column(String)
    trial_name = Column(String)
    trial_days = Column(Integer, default=0)
    default_select = Column(Integer, default=0)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,trial_type = None,
                      trial_name = None,
                      trial_days = 0,
                      default_select = 0,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.trial_type = trial_type
        self.trial_name = trial_name
        self.trial_days = trial_days
        self.default_select = default_select
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
