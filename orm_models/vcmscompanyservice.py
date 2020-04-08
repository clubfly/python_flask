from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class VcmsCompanyService(Base):
    __tablename__ = 'company_services'
 
    sn = Column(Integer, primary_key=True)
    company_sn = Column(Integer, default=0)
    per_product_image_cnt = Column(Integer, default=30)
    service_sn = Column(Integer, default=0)
    recognition_model_name = Column(String, nullable=True)
    recognition_model_version = Column(String, nullable=True)
    deploy_apply_mark = Column(Integer, default=0)
    deploy_apply_time = Column(DateTime, nullable=True)
    deploy_accept_mark = Column(Integer, default=0)
    deploy_accept_time = Column(DateTime, nullable=True)
    system_deploy_mark = Column(Integer, default=0)
    system_deploy_time = Column(DateTime, nullable=True)
    max_product_cnt = Column(Integer, default=1000)
    min_training_cnt = Column(Integer, default=300)
    ct_user_sn = Column(Integer, default=0)
    ut_user_sn = Column(Integer, default=0)
    enabled = Column(Integer, default=1)
    ct = Column(DateTime, default=func.now())
    ut = Column(DateTime, nullable=True, onupdate=func.now())
    deprecated = Column(Integer, default=0)
    detection_api = Column(String, nullable=True)
    feature_api = Column(String, nullable=True)
    self_test_api = Column(String, nullable=True)
    pkl_update_api = Column(String, nullable=True)

    def __init__(self,company_sn = 0,
                      per_product_image_cnt = 30,
                      service_sn = 0,
                      recognition_model_name = None,
                      recognition_model_version = None,
                      deploy_apply_mark = 0,
                      deploy_apply_time = None,
                      deploy_accept_mark = 0,
                      deploy_accept_time = None,
                      system_deploy_mark = 0,
                      system_deploy_time = None,
                      max_product_cnt = 1000,
                      min_training_cnt = 300,
                      ct_user_sn = 0,
                      ut_user_sn = 0,
                      enabled = 1,
                      ct = None,
                      ut = None,
                      deprecated = 0,
                      detection_api = None,
                      feature_api = None,
                      self_test_api = None,
                      pkl_update_api = None) :
        self.company_sn = company_sn
        self.per_product_image_cnt = per_product_image_cnt
        self.service_sn = service_sn
        self.recognition_model_name = recognition_model_name
        self.recognition_model_version = recognition_model_version
        self.deploy_apply_mark = deploy_apply_mark
        self.deploy_apply_time = deploy_apply_time
        self.deploy_accept_mark = deploy_accept_mark
        self.deploy_accept_time = deploy_accept_time
        self.system_deploy_mark = system_deploy_mark
        self.system_deploy_time = system_deploy_time
        self.max_product_cnt = max_product_cnt
        self.min_training_cnt = min_training_cnt
        self.ct_user_sn = ct_user_sn
        self.ut_user_sn = ut_user_sn
        self.enabled = enabled 
        self.ct = ct
        self.ut = ut
        self.deprecated = deprecated
        self.detection_api = detection_api
        self.feature_api = feature_api
        self.self_test_api = self_test_api
        self.pkl_update_api = pkl_update_api
