import os,sys,traceback
import datetime,time
import collections
from flask import session
from utils.pgconnector import PgConnector
from orm_models.vcmscompanyproductcsv import VcmsCompanyProductCsv
from orm_models.vcmscompanyproductcsvcontent import VcmsCompanyProductCsvContent
from orm_models.vcmscompanyproductimagecsv import VcmsCompanyProductImageCsv
from orm_models.vcmscompanyproductimagecsvcontent import VcmsCompanyProductImageCsvContent
from orm_models.vcmscompanyproduct import VcmsCompanyProduct
from orm_models.vcmscompanyproductimage import VcmsCompanyProductImage
from orm_models.vcmscompanyservice import VcmsCompanyService

class VcmsCsvDbAgent : 

    service = "app"

    def __init__(self) :
        pass

    def _set_csv_for_importing_products(self,company_sn,user_file_name,sys_file_name,service_sn) :
        sql_connector = PgConnector(self.service)
        csv = VcmsCompanyProductCsv(company_sn=company_sn,
                                    user_file_name=user_file_name,
                                    sys_file_name=sys_file_name,
                                    service_sn=service_sn,
                                    ct_user_sn=int(session["admin_id"]))
        sql_connector.get_session().add(csv)
        sql_connector.get_session().commit()
        sn = csv.sn
        sql_connector.get_session().get_bind().close()
        return sn

    def _get_csv_for_importing_products(self,limitation=100) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductCsv). \
                                  filter(VcmsCompanyProductCsv.file_manage_time==None). \
                                  filter(VcmsCompanyProductCsv.file_manage_mark==0). \
                                  filter(VcmsCompanyProductCsv.enabled==1). \
                                  filter(VcmsCompanyProductCsv.deprecated==0). \
                                  order_by(VcmsCompanyProductCsv.sn).limit(limitation)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "user_file_name" : row.user_file_name,
                                   "sys_file_name" : row.sys_file_name,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "ct_user_sn" : row.ct_user_sn
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_file_manage_time_for_importing_products(self,sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductCsv). \
                           filter(VcmsCompanyProductCsv.sn==int(sn)). \
                           update({
                                   "file_manage_time" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_file_manage_mark_for_importing_products(self,sn,data_total) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductCsv). \
                           filter(VcmsCompanyProductCsv.sn==int(sn)). \
                           update({
                                   "file_manage_mark" : 1,
                                   "file_manage_time" : ut,
                                   "data_total" : int(data_total),
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_product_csv_contents(self,company_sn,product_csv_sn,sku,barcode,product_name,
                                       ori_file_path,sys_file_path,url,service_sn,ct_user_sn) :
        sql_connector = PgConnector(self.service)
        csv = VcmsCompanyProductCsvContent(company_sn=company_sn,
                                           product_csv_sn=product_csv_sn,
                                           sku=sku,
                                           barcode=barcode,
                                           product_name=product_name,
                                           ori_file_path=ori_file_path,
                                           sys_file_path=sys_file_path,
                                           url=url,
                                           service_sn=service_sn,
                                           ct_user_sn=ct_user_sn)
        sql_connector.get_session().add(csv)
        sql_connector.get_session().commit()
        sn = csv.sn
        sql_connector.get_session().get_bind().close()
        return sn

    def _set_csv_for_importing_product_images(self,company_sn,user_file_name,sys_file_name,service_sn) :
        sql_connector = PgConnector(self.service)
        csv = VcmsCompanyProductImageCsv(company_sn=company_sn,
                                         user_file_name=user_file_name,
                                         sys_file_name=sys_file_name,
                                         service_sn=service_sn,
                                         ct_user_sn=int(session["admin_id"]))
        sql_connector.get_session().add(csv)
        sql_connector.get_session().commit()
        sn = csv.sn
        sql_connector.get_session().get_bind().close()
        return sn

    def _get_csv_for_importing_product_images(self,limitation=100) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImageCsv). \
                                  filter(VcmsCompanyProductImageCsv.file_manage_time==None). \
                                  filter(VcmsCompanyProductImageCsv.file_manage_mark==0). \
                                  filter(VcmsCompanyProductImageCsv.enabled==1). \
                                  filter(VcmsCompanyProductImageCsv.deprecated==0). \
                                  order_by(VcmsCompanyProductImageCsv.sn).limit(limitation)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "user_file_name" : row.user_file_name,
                                   "sys_file_name" : row.sys_file_name,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "ct_user_sn" : row.ct_user_sn,
                                   "zip_user_file_name" : row.zip_user_file_name,
                                   "zip_sys_file_name" : row.zip_sys_file_name,
                                   "zip_manage_mark" : row.zip_manage_mark,
                                   "zip_manage_time" : row.zip_manage_time
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_file_manage_time_for_importing_product_images(self,sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImageCsv). \
                           filter(VcmsCompanyProductImageCsv.sn==int(sn)). \
                           update({
                                   "file_manage_time" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_file_manage_mark_for_importing_product_images(self,sn,data_total) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImageCsv). \
                           filter(VcmsCompanyProductImageCsv.sn==int(sn)). \
                           update({
                                   "file_manage_mark" : 1,
                                   "file_manage_time" : ut,
                                   "data_total" : int(data_total),
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_product_image_csv_contents(self,company_sn,product_image_csv_sn,sku,product_name,
                                             ori_file_path,sys_file_path,url,service_sn,ct_user_sn,
                                             barcode,enabled) :
        sql_connector = PgConnector(self.service)
        csv = VcmsCompanyProductImageCsvContent(company_sn=company_sn,
                                                product_image_csv_sn=product_image_csv_sn,
                                                sku=sku,
                                                product_name=product_name,
                                                ori_file_path=ori_file_path,
                                                sys_file_path=sys_file_path,
                                                url=url,
                                                service_sn=service_sn,
                                                ct_user_sn=ct_user_sn,
                                                barcode=barcode,
                                                enabled=enabled)
        sql_connector.get_session().add(csv)
        sql_connector.get_session().commit()
        sn = csv.sn
        sql_connector.get_session().get_bind().close()
        return sn

    def _get_product_csv_contents_for_creating_products(self,product_csv_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductCsvContent). \
                                  filter(VcmsCompanyProductCsvContent.product_csv_sn==int(product_csv_sn)) . \
                                  filter(VcmsCompanyProductCsvContent.product_created_time==None). \
                                  filter(VcmsCompanyProductCsvContent.product_created_mark==0). \
                                  filter(VcmsCompanyProductCsvContent.enabled==1). \
                                  filter(VcmsCompanyProductCsvContent.deprecated==0). \
                                  order_by(VcmsCompanyProductCsvContent.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "company_sn" : row.company_sn,
                                   "product_csv_sn" : row.product_csv_sn,
                                   "sku" : row.sku,
                                   "barcode" : row.barcode,
                                   "product_name" : row.product_name,
                                   "ori_file_path" : row.ori_file_path,
                                   "sys_file_path" : row.sys_file_path,
                                   "url" : row.url,
                                   "service_sn" : row.service_sn,
                                   "ct_user_sn" : row.ct_user_sn
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_product_created_time_for_importing_products(self,sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductCsvContent). \
                           filter(VcmsCompanyProductCsvContent.sn==int(sn)). \
                           update({
                                   "product_created_time" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_product_created_mark_for_importing_products(self,sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductCsvContent). \
                           filter(VcmsCompanyProductCsvContent.sn==int(sn)). \
                           update({
                                   "product_created_mark" : 1,
                                   "product_created_time" : ut,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _add_company_product_data(self,company_sn,service_sn,barcode,sku,product_name,
                                       abbreviation,thumbnail,ct_user_sn,product_csv_sn) :
        sql_connector = PgConnector(self.service)
        company_product = VcmsCompanyProduct(company_sn=company_sn,
                                             service_sn=service_sn,
                                             barcode=barcode,
                                             sku=sku,
                                             product_name=product_name,
                                             abbreviation=abbreviation,
                                             thumbnail=thumbnail,
                                             ct_user_sn=ct_user_sn,
                                             product_csv_sn=product_csv_sn)
        sql_connector.get_session().add(company_product)
        sql_connector.get_session().commit()
        company_product = company_product.sn
        sql_connector.get_session().get_bind().close()
        return company_product

    def _get_product_image_csv_contents_for_creating_product_images(self,product_image_csv_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImageCsvContent). \
                                  filter(VcmsCompanyProductImageCsvContent.product_image_csv_sn==int(product_image_csv_sn)) . \
                                  filter(VcmsCompanyProductImageCsvContent.image_created_time==None). \
                                  filter(VcmsCompanyProductImageCsvContent.image_created_mark==0). \
                                  filter(VcmsCompanyProductImageCsvContent.enabled==1). \
                                  filter(VcmsCompanyProductImageCsvContent.deprecated==0). \
                                  order_by(VcmsCompanyProductImageCsvContent.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "company_sn" : row.company_sn,
                                   "product_image_csv_sn" : row.product_image_csv_sn,
                                   "sku" : row.sku,
                                   "barcode" : row.barcode,
                                   "product_name" : row.product_name,
                                   "ori_file_path" : row.ori_file_path,
                                   "sys_file_path" : row.sys_file_path,
                                   "url" : row.url,
                                   "service_sn" : row.service_sn,
                                   "ct_user_sn" : row.ct_user_sn
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_image_created_time_for_importing_product_images(self,sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImageCsvContent). \
                           filter(VcmsCompanyProductImageCsvContent.sn==int(sn)). \
                           update({
                                   "image_created_time" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_image_created_mark_for_importing_product_images(self,sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImageCsvContent). \
                           filter(VcmsCompanyProductImageCsvContent.sn==int(sn)). \
                           update({
                                   "image_created_mark" : 1,
                                   "image_created_time" : ut,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_prod_sku_mapping_data(self,company_sn,service_sn,sku,barcode,product_name) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProduct.sku==str(sku)). \
                                  filter(VcmsCompanyProduct.barcode==str(barcode)). \
                                  filter(VcmsCompanyProduct.product_name==str(product_name)). \
                                  filter(VcmsCompanyProduct.enabled==1). \
                                  order_by(VcmsCompanyProduct.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row_sn] = row.sn
        sql_connector.get_session().get_bind().close()
        return return_data 

    def _add_company_product_image_data(self,company_sn,service_sn,product_sn,thumbnail,ct_user_sn,image_csv_sn) :
        sql_connector = PgConnector(self.service)
        product_image = VcmsCompanyProductImage(company_sn=company_sn,
                                                service_sn=service_sn,
                                                product_sn=product_sn,
                                                thumbnail=thumbnail,
                                                ct_user_sn=ct_user_sn,
                                                image_csv_sn=image_csv_sn)
        sql_connector.get_session().add(product_image)
        sql_connector.get_session().commit()
        product_image = product_image.sn
        sql_connector.get_session().get_bind().close()
        return product_image

    def _reset_product_image_cnt(self) :
        sql_connector = PgConnector(self.service)
        sql = """
              select product_sn,
                     count(sn) as cnt 
              from company_product_images 
              where deprecated = 0
              group by product_sn
              """
        rs = sql_connector.execute_raw_sql(sql)
        for row in rs :
            cnt_sql = """
                      update company_products
                      set image_totals = '%s' 
                      where sn = '%s'
                      """ % (row.cnt,row.product_sn)
            sql_connector.execute_raw_sql(cnt_sql)
            sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 0

    def _get_empty_main_product_image(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.thumbnail==""). \
                                  order_by(VcmsCompanyProduct.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_product_images_by_uploading(self,company_sn,service_sn,product_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImage). \
                                  filter(VcmsCompanyProductImage.company_sn==company_sn). \
                                  filter(VcmsCompanyProductImage.service_sn==service_sn). \
                                  filter(VcmsCompanyProductImage.product_sn==product_sn). \
                                  order_by(VcmsCompanyProductImage.sn).limit(1)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data = {
                           "sn" : row.sn, 
                           "company_sn" : row.company_sn,
                           "service_sn" : row.service_sn,
                           "product_sn" : row.product_sn,
                           "thumbnail" : row.thumbnail
                          }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_main_product_image(self,company_sn,service_sn,product_sn,thumbnail) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProduct). \
                           filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                           filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                           filter(VcmsCompanyProduct.sn==int(product_sn)). \
                           update({
                                   "thumbnail" : thumbnail,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _check_product_by_sku(self,company_sn,service_sn,sku) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProduct.sku==str(sku)). \
                                  filter(VcmsCompanyProduct.deprecated==0)
        check_data = 0
        for row in db_result :
            check_data = 1
        sql_connector.get_session().get_bind().close()
        return check_data

    def _set_fail_for_importing_products(self,sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductCsvContent). \
                           filter(VcmsCompanyProductCsvContent.sn==int(sn)). \
                           update({
                                   "enabled" : 0,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_product_csv_file(self,company_sn,user_file_name,sys_file_name,service_sn,ct_user_sn,enabled) :
        sql_connector = PgConnector(self.service)
        csv = VcmsCompanyProductCsv(company_sn=company_sn,
                                    user_file_name=user_file_name,
                                    sys_file_name=sys_file_name,
                                    service_sn=service_sn,
                                    ct_user_sn=ct_user_sn,
                                    enabled=enabled)
        sql_connector.get_session().add(csv)
        sql_connector.get_session().commit()
        sn = csv.sn
        sql_connector.get_session().get_bind().close()
        return sn

    def _set_csv_enabled_for_importing_products(self,sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductCsv). \
                           filter(VcmsCompanyProductCsv.sn==int(sn)). \
                           update({
                                   "enabled" : 1,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _set_product_image_csv_file(self,company_sn,user_file_name,sys_file_name,service_sn,
                                         ct_user_sn,enabled,zip_user_file_name,zip_sys_file_name) :
        sql_connector = PgConnector(self.service)
        csv = VcmsCompanyProductImageCsv(company_sn=company_sn,
                                         user_file_name=user_file_name,
                                         sys_file_name=sys_file_name,
                                         service_sn=service_sn,
                                         ct_user_sn=ct_user_sn,
                                         enabled=enabled,
                                         zip_user_file_name=zip_user_file_name,
                                         zip_sys_file_name=zip_sys_file_name)
        sql_connector.get_session().add(csv)
        sql_connector.get_session().commit()
        sn = csv.sn
        sql_connector.get_session().get_bind().close()
        return sn

    def _set_csv_enabled_for_importing_product_images(self,sn) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImageCsv). \
                           filter(VcmsCompanyProductImageCsv.sn==int(sn)). \
                           update({
                                   "enabled" : 1,
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_csv_for_importing_products_log(self,company_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        system_service_list = self._get_company_service_list(company_sn)
        db_result = sql_connector.query(VcmsCompanyProductCsv). \
                                  filter(VcmsCompanyProductCsv.company_sn==company_sn). \
                                  filter(VcmsCompanyProductCsv.service_sn==service_sn). \
                                  filter(VcmsCompanyProductCsv.deprecated==0). \
                                  order_by(VcmsCompanyProductCsv.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "user_file_name" : row.user_file_name,
                                   "sys_file_name" : row.sys_file_name,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "system_service_sn" : system_service_list[row.service_sn]["sysyem_service_sn"],
                                   "ct_user_sn" : row.ct_user_sn,
                                   "data_total" : row.data_total,
                                   "file_manage_mark" : row.file_manage_mark,
                                   "file_manage_time" : row.file_manage_time,
                                   "enabled" : row.enabled,
                                   "ct" : row.ct,
                                   "error_mark" : self._get_error_csv_content(row.sn)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_download_error_csv_content(self,company_sn,service_sn,csv_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductCsvContent). \
                                  filter(VcmsCompanyProductCsvContent.company_sn==company_sn). \
                                  filter(VcmsCompanyProductCsvContent.service_sn==service_sn). \
                                  filter(VcmsCompanyProductCsvContent.product_csv_sn==int(csv_sn)). \
                                  filter(VcmsCompanyProductCsvContent.product_created_mark==0). \
                                  order_by(VcmsCompanyProductCsvContent.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sku" : row.sku,
                                   "barcode" : row.barcode,
                                   "product_name" : row.product_name,
                                   "message" : "Duplicated"
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_download_success_csv_content(self,company_sn,service_sn,csv_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductCsvContent). \
                                  filter(VcmsCompanyProductCsvContent.company_sn==company_sn). \
                                  filter(VcmsCompanyProductCsvContent.service_sn==service_sn). \
                                  filter(VcmsCompanyProductCsvContent.product_csv_sn==int(csv_sn)). \
                                  filter(VcmsCompanyProductCsvContent.product_created_mark==1). \
                                  order_by(VcmsCompanyProductCsvContent.sn)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sku" : row.sku,
                                   "barcode" : row.barcode,
                                   "product_name" : row.product_name,
                                   "message" : "Success"
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_error_csv_content(self,csv_sn) :
        return_value = 0
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductCsvContent). \
                           filter(VcmsCompanyProductCsvContent.product_csv_sn==int(csv_sn)). \
                           filter(VcmsCompanyProductCsvContent.product_created_mark==0).count()
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        if rs > 0 :
            return_value = 1
        return return_value

    def _get_company_service_list(self,company_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyService). \
                                  filter(VcmsCompanyService.company_sn==company_sn). \
                                  filter(VcmsCompanyService.enabled==1). \
                                  filter(VcmsCompanyService.deprecated==0). \
                                  order_by(VcmsCompanyService.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sysyem_service_sn" : row.service_sn,
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data
