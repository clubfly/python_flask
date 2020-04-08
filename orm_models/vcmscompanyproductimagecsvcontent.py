from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsCompanyProductImageCsvContent(Base):
    __tablename__ = 'company_product_image_csv_contents'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer, default=0)
    product_image_csv_sn = Column(Integer, default=0)
    sku = Column(String)
    product_name = Column(String)
    ori_file_path = Column(String, nullable=True)
    sys_file_path = Column(String, nullable=True)
    url = Column(String, nullable=True)
    image_created_mark = Column(Integer, default=0)
    image_created_time = Column(DateTime, nullable=True)
    service_sn = Column(Integer, default=0)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)
    barcode = Column(String, nullable=True)

    def __init__(self,company_sn = 0,
                      product_image_csv_sn = 0,
                      sku = None,
                      product_name = None,
                      ori_file_path = None,
                      sys_file_path = None,
                      url = None,
                      image_created_mark = 0,
                      image_created_time = None,
                      service_sn = 0,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0,
                      barcode=None) :
        self.company_sn = company_sn 
        self.product_image_csv_sn = product_image_csv_sn
        self.sku = sku
        self.product_name = product_name
        self.ori_file_path = ori_file_path
        self.sys_file_path = sys_file_path
        self.url = url
        self.image_created_mark = image_created_mark
        self.image_created_time = image_created_time
        self.service_sn = service_sn
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
        self.barcode = barcode
