import os,sys,traceback
import datetime,time
import collections
from flask import session
from utils.pgconnector import PgConnector
from orm_models.vcmscompany import VcmsCompany
from orm_models.vcmsrecognitionservice import VcmsRecognitionService
from orm_models.vcmscompanyprofile import VcmsCompanyProfile
from orm_models.vcmscompanyservice import VcmsCompanyService
from orm_models.vcmsuser import VcmsUser
from orm_models.vcmsuserrank import VcmsUserRank
from orm_models.vcmsuserservicepermission import VcmsUserServicePermission
from orm_models.vcmscompanybranch import VcmsCompanyBranch
from orm_models.vcmscompanyproduct import VcmsCompanyProduct
from orm_models.vcmscompanybranchproduct import VcmsCompanyBranchProduct
from orm_models.vcmscompanyproductimage import VcmsCompanyProductImage
from orm_models.vcmscompanyproductimagefeature import VcmsCompanyProductImageFeature
from orm_models.vcmsfeaturepklfile import VcmsFeaturePklFile
from orm_models.vcmsfeaturepklcontent import VcmsFeaturePklContent
from orm_models.vcmssystemlockuploadimage import VcmsSystemLockUploadImage

class VcmsFeatureDbAgent : 

    service = "app"
    limitation = 50

    def __init__(self) :
        pass

    def _get_image_for_detections(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImage). \
                                  filter(VcmsCompanyProductImage.detection_send_time==None). \
                                  filter(VcmsCompanyProductImage.detection_finish_mark==0). \
                                  filter(VcmsCompanyProductImage.enabled==1). \
                                  filter(VcmsCompanyProductImage.deprecated==0). \
                                  order_by(VcmsCompanyProductImage.sn).limit(self.limitation)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "thumbnail" : row.thumbnail,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "product_sn" : row.product_sn
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_processing_time_for_detections(self,image_sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImage). \
                           filter(VcmsCompanyProductImage.sn==int(image_sn)). \
                           update({
                                   "detection_send_time" : ut,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_finish_time_for_detections(self,image_sn,bbox_totals) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImage). \
                           filter(VcmsCompanyProductImage.sn==int(image_sn)). \
                           update({
                                   "bbox_totals" : bbox_totals,
                                   "detection_send_mark" : 1,
                                   "detection_finish_mark" : 1,
                                   "detection_finish_time" : ut,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs 

    def _reset_result_for_detections(self,image_sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImageFeature). \
                           filter(VcmsCompanyProductImageFeature.image_sn==int(image_sn)). \
                           update({
                                   "enabled" : 0,
                                   "deprecated" : 1,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_result_for_detections(self,company_sn,service_sn,product_sn,image_sn,x,y,w,h,contour):
        sql_connector = PgConnector(self.service)
        detections = VcmsCompanyProductImageFeature(
                                                    company_sn=company_sn,
                                                    service_sn=service_sn,
                                                    product_sn=product_sn,
                                                    image_sn=image_sn,
                                                    x=x,
                                                    y=y,
                                                    w=w,
                                                    h=h,
                                                    contour=contour
                                                   )
        sql_connector.get_session().add(detections)
        sql_connector.get_session().commit()
        detections = detections.sn
        sql_connector.get_session().get_bind().close()
        return detections

    def _get_image_for_features(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImage). \
                                  filter(VcmsCompanyProductImage.bbox_totals>0). \
                                  filter(VcmsCompanyProductImage.detection_finish_mark==1). \
                                  filter(VcmsCompanyProductImage.feature_extraction_send_time==None). \
                                  filter(VcmsCompanyProductImage.feature_extraction_finish_mark==0). \
                                  filter(VcmsCompanyProductImage.enabled==1). \
                                  filter(VcmsCompanyProductImage.deprecated==0). \
                                  order_by(VcmsCompanyProductImage.sn).limit(self.limitation)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "thumbnail" : row.thumbnail,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "product_sn" : row.product_sn,
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_image_detection_for_feature(self,image_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImageFeature). \
                                  filter(VcmsCompanyProductImageFeature.image_sn==int(image_sn)). \
                                  filter(VcmsCompanyProductImageFeature.deprecated==0). \
                                  order_by(VcmsCompanyProductImageFeature.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn, 
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "product_sn" : row.product_sn,
                                   "image_sn" : row.image_sn,
                                   "x" : row.x,
                                   "y" : row.y,
                                   "w" : row.w,
                                   "h" : row.h,
                                   "feature" : row.feature,
                                   "contour" : row.contour
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_processing_time_for_features(self,image_sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImage). \
                           filter(VcmsCompanyProductImage.sn==int(image_sn)). \
                           update({
                                   "feature_extraction_send_time" : ut,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_finish_time_for_features(self,image_sn) : 
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImage). \
                           filter(VcmsCompanyProductImage.sn==int(image_sn)). \
                           update({
                                   "feature_extraction_send_mark" : 1,
                                   "feature_extraction_finish_mark" : 1,
                                   "feature_extraction_finish_time" : ut,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_result_for_features(self,sn,feature):
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImageFeature). \
                           filter(VcmsCompanyProductImageFeature.sn==int(sn)). \
                           update({
                                   "feature" : feature,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _add_company_service_pkl_data(self,company_sn,service_sn,branch_sn,pkl_key) :
        sql_connector = PgConnector(self.service)
        pkl = VcmsFeaturePklFile(
                                 company_sn=company_sn,
                                 service_sn=service_sn,
                                 branch_sn=branch_sn,
                                 pkl_key=pkl_key
                                )
        sql_connector.get_session().add(pkl)
        sql_connector.get_session().commit()
        pkl = pkl.sn
        sql_connector.get_session().get_bind().close()
        return pkl

    def _del_company_service_pkl_data(self,company_sn,service_sn,branch_sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsFeaturePklFile). \
                           filter(VcmsFeaturePklFile.company_sn==int(company_sn)). \
                           filter(VcmsFeaturePklFile.service_sn==int(service_sn)). \
                           filter(VcmsFeaturePklFile.branch_sn==int(branch_sn)). \
                           update({
                                   "enabled" : 0,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _add_company_service_pkl_content_data(self,feature_pkl_sn,company_sn,service_sn,branch_sn,pkl_key,
                                              image_sn,sku,feature_sn,product_sn,product_name,barcode,feature) :
        sql_connector = PgConnector(self.service)
        pkl = VcmsFeaturePklContent(
                                    feature_pkl_sn=feature_pkl_sn,
                                    company_sn=company_sn,
                                    service_sn=service_sn,
                                    branch_sn=branch_sn,
                                    pkl_key=pkl_key,
                                    image_sn=image_sn,
                                    sku=sku,
                                    feature_sn=feature_sn,
                                    product_sn=product_sn,
                                    product_name=product_name,
                                    barcode=barcode,
                                    feature=feature
                                   )
        sql_connector.get_session().add(pkl)
        sql_connector.get_session().commit()
        pkl = pkl.sn
        sql_connector.get_session().get_bind().close()
        return pkl

    def _get_company_service_product_enabled_status_data(self,company_sn,service_sn,enabled) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProduct.enabled==int(enabled)). \
                                  filter(VcmsCompanyProduct.deprecated==0). \
                                  order_by(VcmsCompanyProduct.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "product_sn" : row.sn,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "barcode" : row.barcode,
                                   "sku" : row.sku,
                                   "product_name" : row.product_name,
                                   "enabled" : row.enabled,
                                   "category" : row.category
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_service_product_image_enabled_status_data(self,company_sn,service_sn,enabled) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImage). \
                                  filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProductImage.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProductImage.bbox_totals>0). \
                                  filter(VcmsCompanyProductImage.enabled==int(enabled)). \
                                  filter(VcmsCompanyProductImage.deprecated==0). \
                                  order_by(VcmsCompanyProductImage.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "image_sn" : row.sn,
                                   "product_sn" : row.product_sn,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "enabled" : row.enabled
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_service_product_features(self,company_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImageFeature.sn,
                                        VcmsCompanyProductImageFeature.company_sn,
                                        VcmsCompanyProductImageFeature.service_sn,
                                        VcmsCompanyProductImageFeature.product_sn,
                                        VcmsCompanyProductImageFeature.image_sn,
                                        VcmsCompanyProductImageFeature.x,
                                        VcmsCompanyProductImageFeature.y,
                                        VcmsCompanyProductImageFeature.w,
                                        VcmsCompanyProductImageFeature.h,
                                        VcmsCompanyProductImageFeature.contour,
                                        VcmsCompanyProductImageFeature.feature). \
                                  filter(VcmsCompanyProductImageFeature.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProductImageFeature.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProductImageFeature.feature!=None). \
                                  filter(VcmsCompanyProductImageFeature.enabled==1). \
                                  filter(VcmsCompanyProductImageFeature.deprecated==0). \
                                  order_by(VcmsCompanyProductImageFeature.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "instance_sn" : row.sn,
                                   "image_sn" : row.image_sn,
                                   "product_sn" : row.product_sn,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "x" : row.x,
                                   "y" : row.y,
                                   "w" : row.w,
                                   "h" : row.h,
                                   "contour" : row.contour,
                                   "feature" : row.feature
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_service_branch_product_enabled_status_data(self,company_sn,service_sn,branch_sn,enabled) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyBranchProduct). \
                                  filter(VcmsCompanyBranchProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyBranchProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyBranchProduct.branch_sn==int(branch_sn)). \
                                  filter(VcmsCompanyBranchProduct.enabled==enabled). \
                                  filter(VcmsCompanyBranchProduct.deprecated==0). \
                                  order_by(VcmsCompanyBranchProduct.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.product_sn] = row.product_sn
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_output_pkl_file_data(self,pkl_key) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsFeaturePklFile). \
                                  filter(VcmsFeaturePklFile.pkl_key==pkl_key). \
                                  filter(VcmsFeaturePklFile.output_pkl_mark==0). \
                                  filter(VcmsFeaturePklFile.enabled==1). \
                                  filter(VcmsFeaturePklFile.deprecated==0). \
                                  order_by(VcmsFeaturePklFile.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "feature_pkl_sn" : row.sn,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "branch_sn" : row.branch_sn,
                                   "pkl_key" : row.pkl_key
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_output_mark_for_pkl_file(self,pkl_key) :
        output_pkl_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsFeaturePklFile). \
                           filter(VcmsFeaturePklFile.pkl_key==pkl_key). \
                           filter(VcmsFeaturePklFile.output_pkl_mark==0). \
                           update({
                                   "output_pkl_mark" : 1,
                                   "output_pkl_time" : output_pkl_time
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_pkl_file_content_data(self,feature_pkl_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsFeaturePklContent). \
                                  filter(VcmsFeaturePklContent.feature_pkl_sn==feature_pkl_sn). \
                                  filter(VcmsFeaturePklContent.enabled==1). \
                                  filter(VcmsFeaturePklContent.deprecated==0). \
                                  order_by(VcmsFeaturePklContent.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            barcode = None
            if row.barcode is not None :
                barcode = row.barcode
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "feature_pkl_sn" : row.sn,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "branch_sn" : row.branch_sn,
                                   "pkl_key" : row.pkl_key,
                                   "image_sn" : row.image_sn,
                                   "sku" : row.sku,
                                   "feature_sn" : row.feature_sn,
                                   "product_sn" : row.product_sn,
                                   "product_name" : row.product_name,
                                   "barcode" : barcode,
                                   "feature" : row.feature
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def set_pkl_upd_send_mark_to_test_server(self,pkl_key) :
        pkl_update_send_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsFeaturePklFile). \
                           filter(VcmsFeaturePklFile.pkl_key==pkl_key). \
                           filter(VcmsFeaturePklFile.pkl_update_send_mark==0). \
                           update({
                                   "pkl_update_send_mark" : 1,
                                   "pkl_update_send_time" : pkl_update_send_time
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def set_pkl_upd_finish_mark_to_test_server(self,pkl_key) :
        pkl_update_finish_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsFeaturePklFile). \
                           filter(VcmsFeaturePklFile.pkl_key==pkl_key). \
                           filter(VcmsFeaturePklFile.pkl_update_finish_mark==0). \
                           update({
                                   "pkl_update_finish_mark" : 1,
                                   "pkl_update_finish_time" : pkl_update_finish_time
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _reset_feature_enabled_by_product_status(self,company_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        sql = """
              update company_product_image_features
              set enabled = 1
              where product_sn in (SELECT sn FROM company_products where enabled = 1 and company_sn = %s and service_sn = %s) and 
                    company_sn = %s and service_sn = %s;
              update company_product_image_features
              set enabled = 1
              where image_sn in (SELECT sn FROM company_product_images where enabled = 1 and company_sn = %s and service_sn = %s) and 
                    company_sn = %s and service_sn = %s;
              update company_product_image_features 
              set enabled = 0 
              where product_sn in (SELECT sn FROM company_products where enabled = 0 and company_sn = %s and service_sn = %s) and 
                    company_sn = %s and service_sn = %s;
              update company_product_image_features 
              set enabled = 0 
              where image_sn in (SELECT sn FROM company_product_images where enabled = 0 and company_sn = %s and service_sn = %s) and 
                    company_sn = %s and service_sn = %s;""" % (company_sn,service_sn,company_sn,service_sn,
                                                               company_sn,service_sn,company_sn,service_sn,
                                                               company_sn,service_sn,company_sn,service_sn,
                                                               company_sn,service_sn,company_sn,service_sn)
        sql_connector.execute_raw_sql(sql)
        sql_connector.get_session().commit()        
        sql_connector.get_session().get_bind().close()
        return 0

    def _get_company_all_api_settings(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyService). \
                                  filter(VcmsCompanyService.enabled==1). \
                                  filter(VcmsCompanyService.deprecated==0). \
                                  order_by(VcmsCompanyService.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            if int(row.company_sn) not in return_data :
                return_data[row.company_sn] = {}
            return_data[row.company_sn][row.sn] = {
                                                   "company_sn" : row.company_sn,
                                                   "detection_api" : row.detection_api,
                                                   "feature_api" : row.feature_api,
                                                   "self_test_api" : row.self_test_api,
                                                   "pkl_update_api" : row.pkl_update_api
                                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _reset_image_for_detections(self,image_sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImage). \
                           filter(VcmsCompanyProductImage.sn==int(image_sn)). \
                           update({
                                   "bbox_totals" : 0,
                                   "detection_send_mark" : 0,
                                   "detection_send_time" : None,
                                   "detection_finish_mark" : 0,
                                   "detection_finish_time" : None
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_search_product_by_binding_feature(self,company_sn,service_sn,feature_data) :
        sql_connector = PgConnector(self.service)
        sql = "with"
        i = 1
        for row in feature_data :
            sql += """
                   "%s" as (select company_product_image_features.product_sn as "b_%s"
                            from company_product_image_features
                            left join company_products on company_products.sn = company_product_image_features.product_sn 
                            where company_product_image_features.company_sn = %s and
                                  company_product_image_features.service_sn = %s and
                                  company_product_image_features.enabled = 1 and
                                  company_product_image_features.deprecated = 0 and 
                                  company_products.enabled = 1
                            order by cube(company_product_image_features.feature) <-> cube(array%s) limit 1),""" % (i,i,company_sn,service_sn,row["feature"])
            i += 1
        str = ""
        for j in range(1,i) :
            str += """ "%s",""" % (j)
        final_sql = sql[:-1] + """
        select * from %s""" % (str[:-1])
        rs = sql_connector.execute_raw_sql(final_sql)
        return_data = collections.OrderedDict()
        for row in rs :
            for j in range((i-1)) :
                rs2 = self._get_product_data(company_sn,row[j])
                if "product_name" in rs2 :
                    return_data[(j+1)] = {
                                          "product_sn" : row[j],
                                          "product_name" : rs2["product_name"],
                                          "name" : rs2["product_name"],
                                          "sku" : rs2["sku"],
                                          "barcode" : rs2["barcode"]
                                         }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_product_data(self,company_sn,product_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.sn==int(product_sn)). \
                                  filter(VcmsCompanyProduct.enabled==1). \
                                  filter(VcmsCompanyProduct.deprecated==0). \
                                  order_by(VcmsCompanyProduct.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data = {
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
                           "ct" : str(row.ct),
                           "deprecated" : row.deprecated 
                          }
        sql_connector.get_session().get_bind().close()
        return return_data

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
                                   "max_admin_cnt" : row.max_admin_cnt,
                                   "max_branch_cnt" : row.max_branch_cnt,
                                   "max_branch_user_cnt" : row.max_branch_user_cnt,
                                   "ct_user_sn" : row.ct_user_sn,
                                   "ut_user_sn" : row.ut_user_sn,
                                   "enabled" : row.enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_service_data(self,company_sn) :
        return_data = collections.OrderedDict()
        if company_sn > 0 :
            company_list = self._get_all_company_data()
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsCompanyService). \
                                      filter(VcmsCompanyService.company_sn==company_sn). \
                                      order_by(VcmsCompanyService.sn.desc())
            for row in db_result :
                return_data[row.sn] = {
                                       "sn" : row.sn,
                                       "company_service_sn" : row.sn,
                                       "company_sn" : row.company_sn,
                                       "company_name" : company_list[row.company_sn]["company_name"],
                                       "system_service_sn" : row.service_sn,
                                       "per_product_image_cnt" : row.per_product_image_cnt,
                                       "service_sn" : row.service_sn,
                                       "max_product_cnt" : row.max_product_cnt,
                                       "min_training_cnt" : row.min_training_cnt,
                                       "ct_user_sn" : row.ct_user_sn,
                                       "ut_user_sn" : row.ut_user_sn,
                                       "enabled" : row.enabled,
                                       "ct" : str(row.ct),
                                       "deprecated" : row.deprecated
                                      }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _get_system_lock_for_uploading_images(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsSystemLockUploadImage). \
                                  filter(VcmsSystemLockUploadImage.enabled==1). \
                                  filter(VcmsSystemLockUploadImage.deprecated==0). \
                                  order_by(VcmsSystemLockUploadImage.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            lock_time = "N/A"
            if row.lock_time is not None and row.lock_time != "" :
                lock_time = str(row.lock_time)
            unlock_time = "N/A"
            if row.unlock_time is not None and row.unlock_time != "" :
                unlock_time = str(row.unlock_time)
            return_data = {
                           "sn" : row.sn,
                           "lock_token" : row.lock_token,
                           "lock_mark" : row.lock_mark,
                           "lock_time" : lock_time,
                           "unlock_time" : unlock_time
                          }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _reset_all_detection_feature_data(self) :
        sql_connector = PgConnector(self.service)
        sql = """
              TRUNCATE TABLE public.company_product_image_features;
              ALTER SEQUENCE public.company_product_image_features_sn_seq RESTART 1;
              UPDATE public.company_product_images
              set bbox_totals = 0,
                  detection_send_mark = 0,
	          detection_send_time = null,
	          detection_finish_mark = 0,
	          detection_finish_time = null,
                  feature_extraction_send_mark = 0,
	          feature_extraction_send_time = null,
	          feature_extraction_finish_mark = 0,
	          feature_extraction_finish_time = null;
              """
        sql_connector.execute_raw_sql(sql)
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 0

    def _get_company_service_image_for_detections(self,company_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImage). \
                                  filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProductImage.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProductImage.detection_send_time==None). \
                                  filter(VcmsCompanyProductImage.detection_finish_mark==0). \
                                  filter(VcmsCompanyProductImage.deprecated==0). \
                                  order_by(VcmsCompanyProductImage.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "thumbnail" : row.thumbnail,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "product_sn" : row.product_sn
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_service_image_for_features(self,company_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImage). \
                                  filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProductImage.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProductImage.bbox_totals>0). \
                                  filter(VcmsCompanyProductImage.detection_finish_mark==1). \
                                  filter(VcmsCompanyProductImage.feature_extraction_send_time==None). \
                                  filter(VcmsCompanyProductImage.feature_extraction_finish_mark==0). \
                                  filter(VcmsCompanyProductImage.deprecated==0). \
                                  order_by(VcmsCompanyProductImage.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "thumbnail" : row.thumbnail,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "product_sn" : row.product_sn,
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _reset_feature_by_product_status(self,company_sn,service_sn,product_sn,enabled) :
        sql_connector = PgConnector(self.service)
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rs = sql_connector.query(VcmsCompanyProductImageFeature). \
                           filter(VcmsCompanyProductImageFeature.company_sn==int(company_sn)). \
                           filter(VcmsCompanyProductImageFeature.service_sn==int(service_sn)). \
                           filter(VcmsCompanyProductImageFeature.product_sn==int(product_sn)). \
                           update({
                                   "enabled" : int(enabled),
                                   "ut" : ut
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_company_service_product_image_deprecated_status_data(self,company_sn,service_sn,deprecated) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImage). \
                                  filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProductImage.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProductImage.deprecated==int(deprecated)). \
                                  order_by(VcmsCompanyProductImage.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "image_sn" : row.sn,
                                   "product_sn" : row.product_sn,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "thumbnail" : row.thumbnail,
                                   "enabled" : row.enabled
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _reset_feature_by_product_image_status(self,company_sn,service_sn,image_sn,enabled) :
        sql_connector = PgConnector(self.service)
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rs = sql_connector.query(VcmsCompanyProductImageFeature). \
                           filter(VcmsCompanyProductImageFeature.company_sn==int(company_sn)). \
                           filter(VcmsCompanyProductImageFeature.service_sn==int(service_sn)). \
                           filter(VcmsCompanyProductImageFeature.image_sn==int(image_sn)). \
                           update({
                                   "enabled" : int(enabled),
                                   "ut" : ut
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_image_status_by_file_status(self,image_sn,enabled,deprecated) :
        sql_connector = PgConnector(self.service)
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rs = sql_connector.query(VcmsCompanyProductImage). \
                           filter(VcmsCompanyProductImage.sn==int(image_sn)). \
                           update({
                                   "enabled" : int(enabled),
                                   "ut" : ut,
                                   "deprecated" : int(deprecated)
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs
