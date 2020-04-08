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
from orm_models.vcmssystemannouncement import VcmsSystemAnnouncement
from orm_models.vcmssystemannouncementdetail import VcmsSystemAnnouncementDetail
from orm_models.vcmssystemlockuploadimage import VcmsSystemLockUploadImage

class VcmsDbAgent : 

    service = "app"

    def __init__(self) :
        pass

    def _get_login_user_data(self,account,password) :
        return_data = collections.OrderedDict()
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsUser). \
                                  filter(VcmsUser.account==account). \
                                  filter(VcmsUser.passwords==password)
        for row in db_result :
            return_data["admin_id"] = row.sn
            return_data["user_id"] = row.sn
            return_data["account"] = row.account
            return_data["company_sn"] = row.company_sn
            return_data["company_branch_sn"] = row.company_branch_sn
            return_data["user_rank_sn"] = row.user_rank_sn
            return_data["permission_js"] = self._get_all_system_user_ranks()[row.user_rank_sn]["rank_js"]
            return_data["lock_mark"] = row.lock_mark
            return_data["lock_reason"] = row.lock_reason
            return_data["enabled"] = row.enabled
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_user_last_login_time(self,user_sn) :
        sql_connector = PgConnector(self.service)
        last_login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector.query(VcmsUser).filter(VcmsUser.sn==user_sn). \
                                      update({"last_login_time":last_login_time})
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 1

    def _get_user_data_by_user_sn(self,user_sn) :
        return_data = collections.OrderedDict()
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsUser). \
                                  filter(VcmsUser.sn==user_sn)
        for row in db_result :
            return_data["admin_id"] = row.sn
            return_data["user_id"] = row.sn
            return_data["account"] = row.account
            return_data["company_sn"] = row.company_sn
            return_data["company_branch_sn"] = row.company_branch_sn
            return_data["user_rank_sn"] = row.user_rank_sn
            return_data["enabled"] = row.enabled
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_user_pwd_data(self,password) :
        return_data = collections.OrderedDict()
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsUser). \
                                  filter(VcmsUser.sn==session["admin_id"]). \
                                  filter(VcmsUser.passwords==password)
        for row in db_result :
            return_data["admin_id"] = row.sn
            return_data["user_id"] = row.sn
            return_data["account"] = row.account
            return_data["company_sn"] = row.company_sn
            return_data["company_branch_sn"] = row.company_branch_sn
            return_data["user_rank_sn"] = row.user_rank_sn
            return_data["lock_mark"] = row.lock_mark
            return_data["lock_reason"] = row.lock_reason
        sql_connector.get_session().get_bind().close()
        return return_data

    def _upd_self_pwd(self,password) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        sql_connector.query(VcmsUser). \
                      filter(VcmsUser.sn==session["admin_id"]). \
                      update({"passwords" : password,
                              "ut" : ut})
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 1

    def _check_company_data(self,company_name) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompany). \
                                  filter(VcmsCompany.company_name==str(company_name))
        return_value = 0
        for row in db_result :
            return_value = 1
        sql_connector.get_session().get_bind().close()
        return return_value

    def _add_company_data(self,company_name,max_admin_cnt,max_branch_user_cnt,max_branch_cnt) :
        sql_connector = PgConnector(self.service)
        company = VcmsCompany(company_name=company_name,
                              max_admin_cnt=max_admin_cnt,
                              max_branch_user_cnt=max_branch_user_cnt,
                              max_branch_cnt=max_branch_cnt,
                              ct_user_sn=int(session["admin_id"]))
        sql_connector.get_session().add(company)
        sql_connector.get_session().commit()
        company = company.sn
        sql_connector.get_session().get_bind().close()
        return company
  
    def _add_company_profile_data(self,company_sn,company_name) :
        sql_connector = PgConnector(self.service)
        company_profile = VcmsCompanyProfile(
                                             company_sn=company_sn,
                                             company_name=company_name,
                                             ct_user_sn=int(session["admin_id"])
                                            )
        sql_connector.get_session().add(company_profile)
        sql_connector.get_session().commit()
        company_profile = company_profile.sn
        sql_connector.get_session().get_bind().close()
        return company_profile

    def _upd_company_profile_data(self,company_sn,company_profile) :
        sql_connector = PgConnector(self.service)
        company_profile["ut"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        company_profile["ut_user_sn"] = int(session["admin_id"])
        sql_connector.query(VcmsCompanyProfile). \
                      filter(VcmsCompanyProfile.company_sn==int(company_sn)). \
                      update(company_profile)
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 1

    def _check_account_data(self,account) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsUser).filter(VcmsUser.account==str(account))
        return_value = 0
        for row in db_result :
            return_value = 1
        sql_connector.get_session().get_bind().close()
        return return_value

    def _add_company_service_data(self,company_sn,per_product_image_cnt,service_sn,
                                       max_product_cnt,min_training_cnt,detection_api,feature_api,pkl_update_api) :
        sql_connector = PgConnector(self.service)
        company_service = VcmsCompanyService(
                                             company_sn=int(company_sn),
                                             per_product_image_cnt=int(per_product_image_cnt),
                                             service_sn=int(service_sn),
                                             max_product_cnt=int(max_product_cnt),
                                             min_training_cnt=int(min_training_cnt),
                                             detection_api=detection_api,
                                             feature_api=feature_api,
                                             pkl_update_api=pkl_update_api,
                                             ct_user_sn=int(session["admin_id"])
                                            )
        sql_connector.get_session().add(company_service)
        sql_connector.get_session().commit()
        company_service = company_service.sn
        sql_connector.get_session().get_bind().close()
        return company_service

    def _get_company_profile_data(self,company_sn) :
        return_data = collections.OrderedDict()
        if company_sn > 0 :
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsCompanyProfile). \
                                      filter(VcmsCompanyProfile.company_sn==company_sn)
            for row in db_result :
                return_data = {
                               "company_sn" : row.company_sn,
                               "company_name" : row.company_name,
                               "company_no" : row.company_no,
                               "company_address" : row.company_address,
                               "company_tel" : row.company_tel,
                               "company_contact" : row.company_contact,
                               "company_contact_tel" : row.company_contact_tel,
                               "company_contact_email" : row.company_contact_email
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
                                       "per_product_image_cnt" : row.per_product_image_cnt,
                                       "service_sn" : row.service_sn,
                                       "service_name" : system_service[row.service_sn]["service_name"],
                                       "service_type" : system_service[row.service_sn]["service_type"],
                                       "max_product_cnt" : row.max_product_cnt,
                                       "min_training_cnt" : row.min_training_cnt,
                                       "pkl_update_api" : row.pkl_update_api,
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

    def _get_company_branch_data(self,company_sn) :
        return_data = collections.OrderedDict()
        if company_sn > 0 :
            company_list = self._get_all_company_data()
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsCompanyBranch). \
                                      filter(VcmsCompanyBranch.company_sn==company_sn). \
                                      filter(VcmsCompanyBranch.deprecated==0). \
                                      order_by(VcmsCompanyBranch.sn.desc())
            for row in db_result :
                return_data[row.sn] = {
                                       "sn" : row.sn,
                                       "company_sn" : row.company_sn,
                                       "company_name" : company_list[row.company_sn]["company_name"],
                                       "branch_name" : row.branch_name,
                                       "ct_user_sn" : row.ct_user_sn,
                                       "ut_user_sn" : row.ut_user_sn,
                                       "enabled" : row.enabled,
                                       "ct" : str(row.ct)
                                      }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_account_data(self,company_sn) :
        return_data = collections.OrderedDict()
        if company_sn > 0 :
            company_list = self._get_all_company_data()
            system_user_rank_list = self._get_all_system_user_ranks()
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsUser). \
                                      filter(VcmsUser.company_sn==company_sn). \
                                      filter(VcmsUser.deprecated==0). \
                                      order_by(VcmsUser.sn.desc())
            for row in db_result :
                return_data[row.sn] = {
                                       "sn" : row.sn,
                                       "company_sn" : row.company_sn,
                                       "company_name" : company_list[row.company_sn]["company_name"],
                                       "account" : row.account,
                                       "lock_mark" : row.lock_mark,
                                       "lock_time" : str(row.lock_time),
                                       "lock_reason" : row.lock_reason,
                                       "user_rank_sn" : row.user_rank_sn,
                                       "user_rank_name" : system_user_rank_list[row.user_rank_sn]["rank_name"],
                                       "last_login_time" : str(row.last_login_time),
                                       "company_branch_sn" : row.company_branch_sn,
                                       "ct_user_sn" : row.ct_user_sn,
                                       "ut_user_sn" : row.ut_user_sn,
                                       "enabled" : row.enabled,
                                       "ct" : str(row.ct)
                                      }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _get_all_system_user_ranks(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsUserRank). \
                                  filter(VcmsUserRank.deprecated==0). \
                                  order_by(VcmsUserRank.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "rank_name" : row.rank_name,
                                   "rank_function" : row.rank_function,
                                   "rank_js" : row.rank_js,
                                   "enabled" : row.enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_rank_user_cnt(self,company_sn,user_rank_sn) :
        sql_connector = PgConnector(self.service)
        db_data_cnt = sql_connector.query(VcmsUser). \
                                    filter(VcmsUser.company_sn==company_sn). \
                                    filter(VcmsUser.user_rank_sn==user_rank_sn). \
                                    filter(VcmsUser.deprecated==0).count()
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _add_company_account_data(self,company_sn,account,pwd,user_rank_sn,company_branch_sn) :
        sql_connector = PgConnector(self.service)
        company_account = VcmsUser(
                                   account=account,
                                   passwords=pwd,
                                   company_sn=company_sn,
                                   user_rank_sn=user_rank_sn,
                                   company_branch_sn=company_branch_sn,
                                   ct_user_sn=int(session["admin_id"])
                                  )
        sql_connector.get_session().add(company_account)
        sql_connector.get_session().commit()
        company_account_sn = company_account.sn
        sql_connector.get_session().get_bind().close()
        return company_account_sn

    def _get_account_data(self,user_sn) :
        return_data = collections.OrderedDict()
        if int(user_sn) > 0 :        
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsUser). \
                                      filter(VcmsUser.sn==int(user_sn))
            for row in db_result :
                return_data["admin_id"] = row.sn
                return_data["user_id"] = row.sn
                return_data["account"] = row.account
                return_data["company_sn"] = row.company_sn
                return_data["user_rank_sn"] = row.user_rank_sn
                return_data["company_branch_sn"] = row.company_branch_sn
                return_data["lock_mark"] = row.lock_mark
                return_data["lock_reason"] = row.lock_reason
                return_data["ct_user_sn"] = row.ct_user_sn
                return_data["ut_user_sn"] = row.ut_user_sn
            sql_connector.get_session().get_bind().close()
        return return_data

    def _upd_account_pwd(self,user_sn,password) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        sql_connector.query(VcmsUser). \
                      filter(VcmsUser.sn==int(user_sn)). \
                      update({"passwords" : password,
                              "ut_user_sn" : int(session["admin_id"]),
                              "ut" : ut})
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 1

    def _get_user_service_data(self,user_sn) :
        return_data = collections.OrderedDict()
        if int(user_sn) > 0 :
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsUserServicePermission). \
                                      filter(VcmsUserServicePermission.user_sn==int(user_sn)). \
                                      filter(VcmsUserServicePermission.deprecated==0). \
                                      order_by(VcmsUserServicePermission.sn.desc())
            for row in db_result :
                return_data[row.sn] = {
                                       "sn" : row.sn,
                                       "company_sn" : row.company_sn,
                                       "company_service_sn" : row.company_service_sn,
                                       "service_sn" : row.service_sn,
                                       "ct_user_sn" : row.ct_user_sn,
                                       "ut_user_sn" : row.ut_user_sn,
                                       "enabled" : row.enabled,
                                       "ct" : str(row.ct)
                                      }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _add_user_service_permission_data(self,company_sn,user_sn,company_service_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        permission = VcmsUserServicePermission(
                                               user_sn=int(user_sn),
                                               company_service_sn=int(company_service_sn),
                                               service_sn=int(service_sn),
                                               company_sn=int(company_sn),
                                               ct_user_sn=int(session["admin_id"])
                                              )
        sql_connector.get_session().add(permission)
        sql_connector.get_session().commit()
        permission_sn = permission.sn
        sql_connector.get_session().get_bind().close()
        return permission_sn

    def _upd_user_service_permission_data(self,user_sn,company_service_sn,enabled) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        sql_connector.query(VcmsUserServicePermission). \
                      filter(VcmsUserServicePermission.user_sn==int(user_sn)). \
                      filter(VcmsUserServicePermission.company_service_sn==int(company_service_sn)). \
                      update({"enabled" : enabled,
                              "ut_user_sn" : int(session["admin_id"]),
                              "ut" : ut})
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 1

    def _upd_all_user_service_permission_data(self,user_sn,enabled) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        sql_connector.query(VcmsUserServicePermission). \
                      filter(VcmsUserServicePermission.user_sn==int(user_sn)). \
                      update({"enabled" : enabled,
                              "ut_user_sn" : int(session["admin_id"]),
                              "ut" : ut})
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 1

    def _check_company_branch_data(self,company_sn,branch_name) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyBranch). \
                                  filter(VcmsCompanyBranch.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyBranch.branch_name==str(branch_name))
        return_value = 0
        for row in db_result :
            return_value = 1
        sql_connector.get_session().get_bind().close()
        return return_value

    def _get_company_branch_cnt(self,company_sn) :
        sql_connector = PgConnector(self.service)
        db_data_cnt = sql_connector.query(VcmsCompanyBranch). \
                                    filter(VcmsCompanyBranch.company_sn==company_sn). \
                                    filter(VcmsCompanyBranch.deprecated==0).count()
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _add_company_branch_data(self,company_sn,branch_name) :
        sql_connector = PgConnector(self.service)
        company_branch = VcmsCompanyBranch(company_sn=company_sn,
                                           branch_name=branch_name,
                                           ct_user_sn=int(session["admin_id"]))
        sql_connector.get_session().add(company_branch)
        sql_connector.get_session().commit()
        company_branch = company_branch.sn
        sql_connector.get_session().get_bind().close()
        return company_branch

    def _get_all_company_branches(self,company_sn) :
        return_data = collections.OrderedDict()
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyBranch). \
                                  filter(VcmsCompanyBranch.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyBranch.deprecated==0). \
                                  order_by(VcmsCompanyBranch.sn.desc())
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "company_sn" : row.company_sn,
                                   "branch_name" : row.branch_name,
                                   "ct_user_sn" : row.ct_user_sn,
                                   "ut_user_sn" : row.ut_user_sn,
                                   "enabled" : row.enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_branch_account_data(self,company_sn,branch_sn) :
        return_data = collections.OrderedDict()
        if int(branch_sn) > 0 :
            system_user_rank_list = self._get_all_system_user_ranks()
            company_branch_list = self._get_all_company_branches(company_sn)
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsUser). \
                                      filter(VcmsUser.company_sn==int(company_sn)). \
                                      filter(VcmsUser.company_branch_sn==int(branch_sn)). \
                                      filter(VcmsUser.deprecated==0). \
                                      order_by(VcmsUser.sn.desc())
            for row in db_result :
                return_data[row.sn] = {
                                       "sn" : row.sn,
                                       "admin_id" : row.sn,
                                       "user_id" : row.sn,
                                       "account" : row.account,
                                       "company_sn" : row.company_sn,
                                       "company_branch_sn" : row.company_branch_sn,
                                       "branch_name" : company_branch_list[int(row.company_branch_sn)]["branch_name"],
                                       "user_rank_sn" : row.user_rank_sn,
                                       "user_rank_name" : system_user_rank_list[row.user_rank_sn]["rank_name"],
                                       "lock_mark" : row.lock_mark,
                                       "lock_reason" : row.lock_reason,
                                       "ct_user_sn" : row.ct_user_sn,
                                       "ut_user_sn" : row.ut_user_sn,
                                       "enabled" : row.enabled,
                                       "ct" : str(row.ct)
                                      }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _check_company_service(self,company_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyService). \
                                  filter(VcmsCompanyService.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyService.sn==int(service_sn))
        return_value = 0
        for row in db_result :
            return_value = 1
        sql_connector.get_session().get_bind().close()
        return return_value

    def _add_company_product_data(self,company_sn,service_sn,barcode,sku,product_name,abbreviation,thumbnail,category) :
        sql_connector = PgConnector(self.service)
        company_product = VcmsCompanyProduct(company_sn=company_sn,
                                             service_sn=service_sn,
                                             barcode=barcode,
                                             sku=sku,
                                             product_name=product_name,
                                             abbreviation=abbreviation,
                                             thumbnail=thumbnail,
                                             ct_user_sn=int(session["admin_id"]),
                                             category=category)
        sql_connector.get_session().add(company_product)
        sql_connector.get_session().commit()
        company_product = company_product.sn
        sql_connector.get_session().get_bind().close()
        return company_product

    def _check_company_product_data(self,company_sn,service_sn,barcode,sku,product_name,abbreviation) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProduct.barcode==str(barcode)). \
                                  filter(VcmsCompanyProduct.sku==str(sku)). \
                                  filter(VcmsCompanyProduct.product_name==str(product_name)). \
                                  filter(VcmsCompanyProduct.abbreviation==str(abbreviation))
        return_value = 0
        for row in db_result :
            return_value = 1
        sql_connector.get_session().get_bind().close()
        return return_value

    def _get_company_service_product_cnt(self,company_sn,service_sn,search) :
        sql_connector = PgConnector(self.service)
        sql = """
              select count(sn) as db_data_cnt
              from company_products 
              where company_sn = '%s' and 
                    service_sn = '%s' """ % (company_sn,service_sn)
        sql = self.__search_patern(sql,search)
        sql += " and deprecated = 0 "
        rs = sql_connector.execute_raw_sql(sql)
        db_data_cnt = 0
        #print (sql)
        for row in rs :
            db_data_cnt = row["db_data_cnt"]
        '''db_data_cnt = sql_connector.query(VcmsCompanyProduct). \
                                    filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                    filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                    filter(VcmsCompanyProduct.deprecated==0).count()'''
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _get_company_service_enabled_product_cnt(self,company_sn,service_sn,search) :
        sql_connector = PgConnector(self.service)
        '''db_data_cnt = sql_connector.query(VcmsCompanyProduct). \
                                    filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                    filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                    filter(VcmsCompanyProduct.enabled==1). \
                                    filter(VcmsCompanyProduct.deprecated==0).count()'''
        sql = """
              select count(sn) as db_data_cnt
              from company_products
              where company_sn = '%s' and
                    service_sn = '%s' and 
                    enabled = 1 """ % (company_sn,service_sn)
        sql = self.__search_patern(sql,search)
        sql += " and deprecated = 0 "
        rs = sql_connector.execute_raw_sql(sql)
        db_data_cnt = 0
        #print (sql)
        for row in rs :
            db_data_cnt = row["db_data_cnt"]
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _get_company_service_product_image_cnt(self,company_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        db_data_cnt = sql_connector.query(VcmsCompanyProductImage). \
                                    filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                                    filter(VcmsCompanyProductImage.service_sn==int(service_sn)). \
                                    filter(VcmsCompanyProductImage.deprecated==0).count()
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _get_company_service_enabled_product_image_cnt(self,company_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        db_data_cnt = sql_connector.query(VcmsCompanyProductImage). \
                                    filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                                    filter(VcmsCompanyProductImage.service_sn==int(service_sn)). \
                                    filter(VcmsCompanyProductImage.enabled==1). \
                                    filter(VcmsCompanyProductImage.deprecated==0).count()
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _get_company_service_product_data(self,company_sn,service_sn,search,limit,offset) :
        sql_connector = PgConnector(self.service)
        '''db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProduct.deprecated==0). \
                                  order_by(VcmsCompanyProduct.sn.desc()). \
                                  limit(limit).offset(offset)'''
        sql = """
              select * 
              from company_products
              where company_sn = '%s' and
                    service_sn = '%s' """ % (company_sn,service_sn)
        sql = self.__search_patern(sql,search)
        sql += " and deprecated = 0 order by sn desc limit " + str(limit) + " offset " + str(offset)
        db_result = sql_connector.execute_raw_sql(sql)
        print (sql)
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

    def _get_product_data(self,company_sn,product_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.sn==int(product_sn)). \
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
                           "category" : row.category
                          }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _upd_company_product_data(self,company_sn,product_sn,barcode,sku,product_name,abbreviation,category) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        sql_connector.query(VcmsCompanyProduct). \
                      filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                      filter(VcmsCompanyProduct.sn==int(product_sn)). \
                      update({
                              "barcode" : barcode,
                              "sku" : sku,
                              "product_name" : product_name,
                              "abbreviation" : abbreviation,
                              "ut_user_sn" : int(session["admin_id"]),
                              "ut" : ut,
                              "category" : category
                             })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 1

    def _upd_company_product_image_data(self,company_sn,product_sn,thumbnail) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        sql_connector.query(VcmsCompanyProduct). \
                      filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                      filter(VcmsCompanyProduct.sn==int(product_sn)). \
                      update({
                              "thumbnail" : thumbnail,
                              "ut_user_sn" : int(session["admin_id"]),
                              "ut" : ut
                             })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return 1

    def _upd_company_product_status_data(self,company_sn,product_sn,enabled,deprecated) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProduct). \
                           filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                           filter(VcmsCompanyProduct.sn==int(product_sn)). \
                           update({
                                   "enabled" : enabled,
                                   "deprecated" : deprecated,
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _upd_company_product_image_feature_status_by_product(self,company_sn,product_sn,enabled,deprecated) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImageFeature). \
                           filter(VcmsCompanyProductImageFeature.company_sn==int(company_sn)). \
                           filter(VcmsCompanyProductImageFeature.product_sn==int(product_sn)). \
                           update({
                                   "enabled" : enabled,
                                   "deprecated" : deprecated,
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _upd_company_product_image_status_by_product(self,company_sn,product_sn,enabled) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImage). \
                           filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                           filter(VcmsCompanyProductImage.product_sn==int(product_sn)). \
                           update({
                                   "enabled" : enabled,
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_company_product_image_cnt(self,company_sn,product_sn) :
        sql_connector = PgConnector(self.service)
        db_data_cnt = sql_connector.query(VcmsCompanyProductImage). \
                                    filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                                    filter(VcmsCompanyProductImage.product_sn==int(product_sn)). \
                                    filter(VcmsCompanyProductImage.deprecated==0).count()
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _get_company_product_image_data(self,company_sn,product_sn,limit,offset) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImage). \
                                  filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProductImage.product_sn==int(product_sn)). \
                                  filter(VcmsCompanyProductImage.deprecated==0). \
                                  order_by(VcmsCompanyProductImage.sn.desc()). \
                                  limit(limit).offset(offset)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "company_sn" : row.company_sn,
                                   "service_sn" : row.service_sn,
                                   "product_sn" : row.product_sn,
                                   "thumbnail" : row.thumbnail,
                                   "feature_extraction_send_mark" : row.feature_extraction_send_mark,
                                   "feature_extraction_send_time" : str(row.feature_extraction_send_time),
                                   "feature_extraction_finish_mark" : row.feature_extraction_finish_mark,
                                   "feature_extraction_finish_time" : str(row.feature_extraction_finish_time),
                                   "bbox_totals" : row.bbox_totals,
                                   "detection_send_mark" : row.detection_send_mark,
                                   "detection_send_time" : str(row.detection_send_time),
                                   "detection_finish_mark" : row.detection_finish_mark,
                                   "detection_finish_time" : str(row.detection_finish_time),
                                   "ct_user_sn" : row.ct_user_sn,
                                   "ut_user_sn" : row.ut_user_sn,
                                   "enabled" : row.enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _add_company_product_image_data(self,company_sn,service_sn,product_sn,thumbnail) :
        sql_connector = PgConnector(self.service)
        product_image = VcmsCompanyProductImage(company_sn=company_sn,
                                                service_sn=service_sn,
                                                product_sn=product_sn,
                                                thumbnail=thumbnail,
                                                ct_user_sn=int(session["admin_id"]))
        sql_connector.get_session().add(product_image)
        sql_connector.get_session().commit()
        product_image = product_image.sn
        sql_connector.get_session().get_bind().close()
        return product_image

    def _upd_company_product_image_status_data(self,company_sn,image_sn,enabled,deprecated) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImage). \
                           filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                           filter(VcmsCompanyProductImage.sn==int(image_sn)). \
                           update({
                                   "enabled" : enabled,
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut,
                                   "deprecated" : deprecated
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _upd_company_product_image_feature_status_by_image(self,company_sn,image_sn,enabled,deprecated) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProductImageFeature). \
                           filter(VcmsCompanyProductImageFeature.company_sn==int(company_sn)). \
                           filter(VcmsCompanyProductImageFeature.image_sn==int(image_sn)). \
                           update({
                                   "enabled" : enabled,
                                   "deprecated" : deprecated,
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut
                                 })   
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_company_service_product_enabled_cnt(self,company_sn,service_sn) :
        sql_connector = PgConnector(self.service)
        db_data_cnt = sql_connector.query(VcmsCompanyProduct). \
                                    filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                    filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                    filter(VcmsCompanyProduct.enabled==1). \
                                    filter(VcmsCompanyProduct.deprecated==0).count()
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _get_company_service_product_enabled_data(self,company_sn,service_sn,limit,offset,branch_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProduct.enabled==1). \
                                  filter(VcmsCompanyProduct.deprecated==0). \
                                  order_by(VcmsCompanyProduct.sn.desc()). \
                                  limit(limit).offset(offset)
        return_data = collections.OrderedDict()
        branch_selected = self._get_company_service_branch_product_data(company_sn,service_sn,branch_sn)
        for row in db_result :
            enabled = 0
            if int(row.sn) in branch_selected : 
                enabled = 1
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
                                   "enabled" : enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_service_branch_product_data(self,company_sn,service_sn,branch_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyBranchProduct). \
                                  filter(VcmsCompanyBranchProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyBranchProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyBranchProduct.branch_sn==int(branch_sn)). \
                                  filter(VcmsCompanyBranchProduct.enabled==1). \
                                  filter(VcmsCompanyBranchProduct.deprecated==0). \
                                  order_by(VcmsCompanyBranchProduct.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[int(row.product_sn)] = int(row.enabled)
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_branch_product_settings_data(self,company_sn,service_sn,branch_sn,product_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyBranchProduct). \
                                  filter(VcmsCompanyBranchProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyBranchProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyBranchProduct.branch_sn==int(branch_sn)). \
                                  filter(VcmsCompanyBranchProduct.product_sn==int(product_sn))
        return_value = 0
        for row in db_result :
            return_value = 1
        sql_connector.get_session().get_bind().close()
        return return_value

    def _add_company_branch_product_settings(self,company_sn,service_sn,branch_sn,product_sn) :
        sql_connector = PgConnector(self.service)
        company_branch_product = VcmsCompanyBranchProduct(company_sn=company_sn,
                                                          service_sn=service_sn,
                                                          branch_sn=branch_sn,
                                                          product_sn=product_sn,
                                                          ct_user_sn=int(session["admin_id"]))
        sql_connector.get_session().add(company_branch_product)
        sql_connector.get_session().commit()
        company_branch_product = company_branch_product.sn
        sql_connector.get_session().get_bind().close()
        return company_branch_product

    def _upd_company_branch_product_settings(self,company_sn,service_sn,branch_sn,product_sn,enabled) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyBranchProduct). \
                           filter(VcmsCompanyBranchProduct.company_sn==int(company_sn)). \
                           filter(VcmsCompanyBranchProduct.service_sn==int(service_sn)). \
                           filter(VcmsCompanyBranchProduct.branch_sn==int(branch_sn)). \
                           filter(VcmsCompanyBranchProduct.product_sn==int(product_sn)). \
                           update({
                                   "enabled" : enabled,
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _upd_company_product_image_totals(self,company_sn,product_sn,image_totals) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsCompanyProduct). \
                           filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                           filter(VcmsCompanyProduct.sn==int(product_sn)). \
                           update({
                                   "image_totals" : image_totals,
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut
                                 })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs 

    def _get_image_info_data(self,company_sn,image_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProductImage). \
                                  filter(VcmsCompanyProductImage.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProductImage.sn==int(image_sn))
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data = {
                           "sn" : row.sn,
                           "service_sn" : row.service_sn,
                           "product_sn" : row.product_sn,
                           "thumbnail" : row.thumbnail,
                           "feature_extraction_send_mark" : row.feature_extraction_send_mark,
                           "feature_extraction_send_time" : str(row.feature_extraction_send_time),
                           "feature_extraction_finish_mark" : row.feature_extraction_finish_mark,
                           "feature_extraction_finish_time" : str(row.feature_extraction_finish_time),
                           "bbox_totals" : row.bbox_totals,
                           "detection_send_mark" : row.detection_send_mark,
                           "detection_send_time" : str(row.detection_send_time),
                           "detection_finish_mark" : row.detection_finish_mark,
                           "detection_finish_time" : str(row.detection_finish_time),
                           "ct_user_sn" : row.ct_user_sn,
                           "ut_user_sn" : row.ut_user_sn,
                           "enabled" : row.enabled
                          }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_product_by_sku(self,company_sn,sku,service_sn) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProduct.sku==str(sku)). \
                                  filter(VcmsCompanyProduct.enabled==1). \
                                  filter(VcmsCompanyProduct.deprecated==0)
        data_check = 0
        for row in db_result :
            data_check = 1
        return data_check

    def _add_system_announcement_data(self,board_hash,publish_time) :
        sql_connector = PgConnector(self.service)
        system_announcement = VcmsSystemAnnouncement(board_hash=board_hash,
                                                     publish_time=publish_time,
                                                     ct_user_sn=int(session["admin_id"]))
        sql_connector.get_session().add(system_announcement)
        sql_connector.get_session().commit()
        system_announcement= system_announcement.sn
        sql_connector.get_session().get_bind().close()
        return system_announcement

    def _upd_system_announcement_data(self,board_hash,publish_time) :
        sql_connector = PgConnector(self.service)
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rs = sql_connector.query(VcmsSystemAnnouncement). \
                           filter(VcmsSystemAnnouncement.board_hash==str(board_hash)). \
                           update({
                                   "publish_time" : publish_time,         
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _add_system_announcement_detail_data(self,board_hash,language_type,titles,contents) :
        sql_connector = PgConnector(self.service)
        system_announcement = VcmsSystemAnnouncementDetail(board_hash=board_hash,
                                                           language_type=language_type,
                                                           titles=titles,
                                                           contents=contents,
                                                           ct_user_sn=int(session["admin_id"]))
        sql_connector.get_session().add(system_announcement)
        sql_connector.get_session().commit()
        system_announcement= system_announcement.sn
        sql_connector.get_session().get_bind().close()
        return system_announcement

    def _upd_system_announcement_detail_data(self,board_hash,language_type,titles,contents) :
        sql_connector = PgConnector(self.service)
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rs = sql_connector.query(VcmsSystemAnnouncementDetail). \
                           filter(VcmsSystemAnnouncementDetail.board_hash==str(board_hash)). \
                           filter(VcmsSystemAnnouncementDetail.language_type==str(language_type)). \
                           update({
                                   "titles" : titles,
                                   "contents" : contents,
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_all_system_announcement_cnt(self) :
        sql_connector = PgConnector(self.service)
        db_data_cnt = sql_connector.query(VcmsSystemAnnouncement). \
                                    filter(VcmsSystemAnnouncement.deprecated==0).count()
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _get_all_system_announcement_data(self,limit,offset) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsSystemAnnouncement). \
                                  filter(VcmsSystemAnnouncement.deprecated==0). \
                                  order_by(VcmsSystemAnnouncement.sn.desc()). \
                                  limit(limit).offset(offset)
        return_data = collections.OrderedDict()
        user_map = self._get_root_info()
        for row in db_result :
            publish_time = "N/A"
            if row.publish_time is not None and row.publish_time != "" :
                publish_time = row.publish_time
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "board_hash" : str(row.board_hash),
                                   "publish_mark" : row.publish_mark,
                                   "publish_time" : publish_time,
                                   "user_name" : user_map[row.ct_user_sn],
                                   "ct_user_sn" : row.ct_user_sn,
                                   "ut_user_sn" : row.ut_user_sn,
                                   "enabled" : row.enabled,
                                   "boards" : self._get_all_system_announcement_detail_data(row.board_hash)
                                 }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_root_info(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsUser). \
                                  filter(VcmsUser.company_sn==0). \
                                  filter(VcmsUser.deprecated==0)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = row.account
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_all_system_announcement_detail_data(self,board_hash) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsSystemAnnouncementDetail). \
                                  filter(VcmsSystemAnnouncementDetail.board_hash==str(board_hash)). \
                                  filter(VcmsSystemAnnouncementDetail.enabled==1). \
                                  filter(VcmsSystemAnnouncementDetail.deprecated==0)
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[str(row.language_type)] = {
                                                   "board_hash" : str(row.board_hash),
                                                   "titles" : str(row.titles),
                                                   "contents" : str(row.contents),
                                                   "ct_user_sn" : row.ct_user_sn,
                                                   "ut_user_sn" : row.ut_user_sn
                                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_system_announcement_data_by_board_hash(self,board_hash) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsSystemAnnouncement). \
                                  filter(VcmsSystemAnnouncement.board_hash==str(board_hash))
        return_data = collections.OrderedDict()
        for row in db_result :
            publish_time = "N/A"
            if row.publish_time is not None and row.publish_time != "" :
                publish_time = row.publish_time 
            return_data = {
                           "sn" : row.sn,
                           "board_hash" : str(row.board_hash),
                           "publish_mark" : row.publish_mark,
                           "publish_time" : publish_time,
                           "ct_user_sn" : row.ct_user_sn,
                           "ut_user_sn" : row.ut_user_sn,
                           "enabled" : row.enabled,
                          }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _set_system_announcement_status(self,board_hash,publish_mark,publish_time) :
        sql_connector = PgConnector(self.service)
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rs = sql_connector.query(VcmsSystemAnnouncement). \
                           filter(VcmsSystemAnnouncement.board_hash==str(board_hash)). \
                           update({
                                   "publish_mark" : publish_mark,
                                   "publish_time" : publish_time,
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_all_enabled_system_announcement_cnt(self,publish_time) :
        sql_connector = PgConnector(self.service)
        db_data_cnt = sql_connector.query(VcmsSystemAnnouncement). \
                                    filter(VcmsSystemAnnouncement.publish_mark==1). \
                                    filter(VcmsSystemAnnouncement.publish_time!=None). \
                                    filter(VcmsSystemAnnouncement.publish_time<=publish_time). \
                                    filter(VcmsSystemAnnouncement.enabled==1). \
                                    filter(VcmsSystemAnnouncement.deprecated==0).count()
        sql_connector.get_session().get_bind().close()
        return int(db_data_cnt)

    def _get_all_enabled_system_announcement_data(self,publish_time,limit,offset) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsSystemAnnouncement). \
                                  filter(VcmsSystemAnnouncement.publish_mark==1). \
                                  filter(VcmsSystemAnnouncement.publish_time!=None). \
                                  filter(VcmsSystemAnnouncement.publish_time<=publish_time). \
                                  filter(VcmsSystemAnnouncement.enabled==1). \
                                  filter(VcmsSystemAnnouncement.deprecated==0). \
                                  order_by(VcmsSystemAnnouncement.sn.desc()). \
                                  limit(limit).offset(offset)
        return_data = collections.OrderedDict()
        user_map = self._get_root_info()
        for row in db_result :
            publish_time = "N/A"
            if row.publish_time is not None and row.publish_time != "" :
                publish_time = row.publish_time
            return_data[row.sn] = {
                                   "sn" : row.sn, 
                                   "board_hash" : str(row.board_hash),
                                   "publish_mark" : row.publish_mark,
                                   "publish_time" : publish_time,
                                   "user_name" : user_map[row.ct_user_sn],
                                   "ct_user_sn" : row.ct_user_sn,
                                   "ut_user_sn" : row.ut_user_sn,
                                   "enabled" : row.enabled,
                                   "boards" : self._get_all_system_announcement_detail_data(row.board_hash)
                                 }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_system_lock_for_uploading_images(self,lock_token) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsSystemLockUploadImage). \
                                  filter(VcmsSystemLockUploadImage.lock_token==str(lock_token)). \
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

    def _set_system_lock_for_uploading_images(self,lock_token,lock_mark) :
        sql_connector = PgConnector(self.service)
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lock_time = None
        unlock_time = None
        if int(lock_mark) == 1 :
            lock_time = ut
        else :
            unlock_time = ut
        rs = sql_connector.query(VcmsSystemLockUploadImage). \
                           filter(VcmsSystemLockUploadImage.lock_token==str(lock_token)). \
                           update({
                                   "lock_mark" : lock_mark,
                                   "lock_time" : lock_time,
                                   "unlock_time" : unlock_time,
                                   "ut" : ut
                                  })
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _upd_company_account_status(self,company_sn,user_sn,enabled) :
        ut = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_connector = PgConnector(self.service)
        rs = sql_connector.query(VcmsUser). \
                           filter(VcmsUser.company_sn==int(company_sn)). \
                           filter(VcmsUser.sn==int(user_sn)). \
                           update({"enabled" : int(enabled),
                                   "ut_user_sn" : int(session["admin_id"]),
                                   "ut" : ut}) 
        sql_connector.get_session().commit()
        sql_connector.get_session().get_bind().close()
        return rs

    def _get_company_service_product_csv_data(self,company_sn,service_sn,search) :
        sql_connector = PgConnector(self.service)
        '''db_result = sql_connector.query(VcmsCompanyProduct). \
                                  filter(VcmsCompanyProduct.company_sn==int(company_sn)). \
                                  filter(VcmsCompanyProduct.service_sn==int(service_sn)). \
                                  filter(VcmsCompanyProduct.deprecated==0). \
                                  order_by(VcmsCompanyProduct.sn.desc()). \
                                  limit(limit).offset(offset)'''
        sql = """
              select *
              from company_products
              where company_sn = '%s' and
                    service_sn = '%s' """ % (company_sn,service_sn)
        sql = self.__search_patern(sql,search)
        sql += " and deprecated = 0 order by sn desc"
        db_result = sql_connector.execute_raw_sql(sql)
        #print (sql)
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

    def __search_patern(self,sql,search) :
        if search :
            if search["product_sn"] is not None and search["product_sn"] != "" :
                sql += " and sku like '%s' " % ("%"+search["product_sn"]+"%")
            if search["product_name"] is not None and search["product_name"] != "" :
                sql += " and product_name like '%s' " % ("%"+search["product_name"]+"%")
            if search["abbreviation"] is not None and search["abbreviation"] != "" :
                sql += " and abbreviation like '%s' " % ("%"+search["abbreviation"]+"%")
            if search["barcode"] is not None and search["barcode"] != "" :
                sql += " and barcode like '%s' " % ("%"+search["barcode"]+"%")
            if search["ct_start_date"] is None or search["ct_start_date"] == "" :
                search["ct_start_date"] = "1970-01-01"
            if search["ct_end_date"] is None or search["ct_end_date"] == "" :
                search["ct_end_date"] = datetime.datetime.now().strftime("%Y-%m-%d")
            sql += " and to_char(ct,'YYYY-MM-DD') between '%s' and '%s' " % (search["ct_start_date"],search["ct_end_date"])
            if search["ut_start_date"] is not None and search["ut_start_date"] != "" :
                sql += " and to_char(ut,'YYYY-MM-DD') >= '%s' " % (search["ut_start_date"])
            if search["ut_end_date"] is not None and search["ut_end_date"] != "" :
                sql += " and to_char(ut,'YYYY-MM-DD') <= '%s' " % (search["ut_end_date"])
            if search["image_cnt"] is not None and search["image_cnt"] != "" :
                if int(search["image_cnt"]) > 0 :
                    sql += " and image_totals > 0 "
                else :
                    sql += " and image_totals = 0 "
            if search["enabled"] is not None and search["enabled"] != "" :
                if int(search["enabled"]) > 0 :
                    sql += " and enabled = 1 "
                else :
                    sql += " and enabled = 0 "
        return sql
