from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsCompanyProductImage(Base):
    __tablename__ = 'company_product_images'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer)
    service_sn = Column(Integer)
    product_sn = Column(Integer)
    thumbnail = Column(String)
    feature_extraction_send_mark = Column(Integer, default=0)
    feature_extraction_send_time = Column(DateTime, nullable=True)
    feature_extraction_finish_mark = Column(Integer, default=0)
    feature_extraction_finish_time = Column(DateTime, nullable=True)
    bbox_totals = Column(Integer, default=0)
    detection_send_mark = Column(Integer, default=0)
    detection_send_time = Column(DateTime, nullable=True)
    detection_finish_mark = Column(Integer, default=0)
    detection_finish_time = Column(DateTime, nullable=True)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)
    image_csv_sn = Column(Integer, default=0)

    def __init__(self,company_sn = 0,
                      service_sn = 0,
                      product_sn = 0,
                      thumbnail = None,
                      feature_extraction_send_mark = 0,
                      feature_extraction_send_time = None,
                      feature_extraction_finish_mark = 0,
                      feature_extraction_finish_time = None,
                      bbox_totals = 0,
                      detection_send_mark = 0,
                      detection_send_time = None,
                      detection_finish_mark = 1,
                      detection_finish_time = None,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0,
                      image_csv_sn = 0) :
        self.company_sn = company_sn
        self.service_sn = service_sn
        self.product_sn = product_sn
        self.thumbnail = thumbnail
        self.feature_extraction_send_mark = feature_extraction_send_mark
        self.feature_extraction_send_time = feature_extraction_send_time
        self.feature_extraction_finish_mark = feature_extraction_finish_mark
        self.feature_extraction_finish_time = feature_extraction_finish_time
        self.bbox_totals = bbox_totals
        self.detection_send_mark = detection_send_mark
        self.feature_extraction_send_time = feature_extraction_send_time
        self.feature_extraction_finish_mark = feature_extraction_finish_mark
        self.feature_extraction_finish_time = feature_extraction_finish_time
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
        self.image_csv_sn = image_csv_sn
