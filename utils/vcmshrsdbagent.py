import os,sys,traceback
import datetime,time
import collections
from flask import session
from utils.pgconnector import PgConnector
from orm_models.vcmscompany import VcmsCompany
from orm_models.vcmsrecognitionservice import VcmsRecognitionService
from orm_models.vcmscompanyservice import VcmsCompanyService
from orm_models.vcmscompanyproduct import VcmsCompanyProduct
from orm_models.vcmscompanyproductimage import VcmsCompanyProductImage

class VcmsHrsDbAgent : 

    service = "app"

    def __init__(self) :
        pass

    def _get_all_company_data(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompany). \
                                  filter(VcmsCompany.deprecated==0). \
                                  order_by(VcmsCompany.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "company_name" : row.company_name,
                                   "service_list" : self._get_company_service_data(int(row.sn)),
                                   "enabled" : row.enabled
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_system_service_data(self) :
        return_data = collections.OrderedDict()
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsRecognitionService). \
                                  filter(VcmsRecognitionService.enabled==1). \
                                  filter(VcmsRecognitionService.deprecated==0). \
                                  order_by(VcmsRecognitionService.sn)
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "service_name" : row.service_name,
                                   "service_type" : row.service_type,
                                   "feature_extraction_mark" : row.feature_extraction_mark,
                                   "enabled" : row.enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_service_data(self,company_sn) :
        return_data = collections.OrderedDict()
        if company_sn > 0 :
            system_service = self._get_system_service_data()
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsCompanyService). \
                                      filter(VcmsCompanyService.company_sn==company_sn). \
                                      order_by(VcmsCompanyService.sn.desc())
            for row in db_result :
                return_data[row.sn] = {
                                       "sn" : row.sn,
                                       "company_service_sn" : row.sn,
                                       "company_sn" : row.company_sn,
                                       "service_sn" : row.service_sn,
                                       "service_name" : system_service[row.service_sn]["service_name"],
                                       "service_type" : system_service[row.service_sn]["service_type"],
                                       "enabled" : row.enabled
                                      }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_service_product_cnt(self,service_sn,search_key) :
        sql_connector = PgConnector(self.service)
        if search_key is None or search_key == "" :
            db_data_cnt = sql_connector.query(VcmsCompanyProduct). \
                                        filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                        filter(VcmsCompanyProduct.deprecated==0).count()
        else :
            db_data_cnt = sql_connector.query(VcmsCompanyProduct). \
                                        filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                        filter(VcmsCompanyProduct.product_name==str(search_key)). \
                                        filter(VcmsCompanyProduct.deprecated==0).count()
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _get_company_service_product_data(self,service_sn,search_key,limit,offset) :
        sql_connector = PgConnector(self.service)
        if search_key is None or search_key == "" :
            db_result = sql_connector.query(VcmsCompanyProduct). \
                                      filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                      filter(VcmsCompanyProduct.deprecated==0). \
                                      order_by(VcmsCompanyProduct.sn.desc()). \
                                      limit(limit).offset(offset)
        else :
            db_result = sql_connector.query(VcmsCompanyProduct). \
                                      filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                      filter(VcmsCompanyProduct.product_name==str(search_key)). \
                                      filter(VcmsCompanyProduct.deprecated==0). \
                                      order_by(VcmsCompanyProduct.sn.desc()). \
                                      limit(limit).offset(offset)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "barcode" : row.barcode,
                                   "sku" : row.sku,
                                   "product_name" : row.product_name,
                                   "abbreviation" : row.abbreviation,
                                   "thumbnail" : row.thumbnail,
                                   "image_totals" : row.image_totals,
                                   "ct_user_sn" : row.ct_user_sn,
                                   "ut_user_sn" : row.ut_user_sn,
                                   "enabled" : row.enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data
