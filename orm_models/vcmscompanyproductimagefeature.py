from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime, Float, ARRAY
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsCompanyProductImageFeature(Base):
    __tablename__ = 'company_product_image_features'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer)
    service_sn = Column(Integer)
    product_sn = Column(Integer)
    image_sn = Column(Integer)
    x = Column(Float, default=0)
    y = Column(Float, default=0)
    w = Column(Float, default=0)
    h = Column(Float, default=0)
    feature = Column(ARRAY(Float), nullable=True)
    contour = Column(ARRAY(Float), nullable=True)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)

    def __init__(self,company_sn = 0,
                      service_sn = 0,
                      product_sn = 0,
                      image_sn = 0,
                      x = 0,
                      y = 0,
                      w = 0,
                      h = 0,
                      feature = None,
                      contour = None,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0) :
        self.company_sn = company_sn
        self.service_sn = service_sn
        self.product_sn = product_sn
        self.image_sn = image_sn
        self.x = x,
        self.y = y
        self.w = w
        self.h = h
        self.feature = feature
        self.contour = contour
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn        
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
