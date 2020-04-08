from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime, Float, ARRAY
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsFeaturePklContent(Base):
    __tablename__ = 'feature_pkl_contents'
 
    sn = Column(Integer, primary_key=True)
    feature_pkl_sn = Column(Integer, default=0)
    company_sn = Column(Integer, default=0)
    service_sn = Column(Integer, default=0)
    branch_sn = Column(Integer, default=0)
    pkl_key = Column(String)
    image_sn = Column(Integer, default=0)
    sku = Column(String)
    feature_sn = Column(Integer, default=0)
    product_sn = Column(Integer, default=0)
    product_name = Column(String)
    barcode = Column(String,nullable=True)
    feature = Column(ARRAY(Float), nullable=True)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,feature_pkl_sn = 0,
                      company_sn = 0,
                      service_sn = 0, 
                      branch_sn = 0, 
                      pkl_key = None,
                      image_sn = 0,
                      sku = None,
                      feature_sn = 0,
                      product_sn = 0,
                      product_name = None,
                      barcode = None,
                      feature = None,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.feature_pkl_sn = feature_pkl_sn
        self.company_sn = company_sn
        self.service_sn = service_sn
        self.branch_sn = branch_sn 
        self.pkl_key = pkl_key
        self.image_sn = image_sn
        self.sku = sku
        self.feature_sn = feature_sn
        self.product_sn = product_sn
        self.product_name = product_name
        self.barcode = barcode
        self.feature = feature
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
