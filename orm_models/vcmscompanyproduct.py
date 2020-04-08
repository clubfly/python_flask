from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsCompanyProduct(Base):
    __tablename__ = 'company_products'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer)
    service_sn = Column(Integer)
    barcode = Column(String, nullable=True)
    sku = Column(String)
    product_name = Column(String)
    abbreviation = Column(String, nullable=True)
    thumbnail = Column(String)
    image_totals = Column(Integer, default=0)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)
    product_csv_sn = Column(Integer, default=0)
    category = Column(String, nullable=True)

    def __init__(self,company_sn = 0,
                      service_sn = 0,
                      barcode = None,
                      sku = None,
                      product_name = None,
                      abbreviation = None,
                      thumbnail = None,
                      image_totals = 0,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0,
                      product_csv_sn = 0,
                      category= None) :
        self.company_sn = company_sn
        self.service_sn = service_sn
        self.barcode = barcode
        self.sku = sku
        self.product_name = product_name
        self.abbreviation = abbreviation
        self.thumbnail = thumbnail
        self.image_totals = image_totals
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn        
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
        self.product_csv_sn = product_csv_sn
        self.category = category
