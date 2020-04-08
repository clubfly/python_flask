import os,sys,traceback
import datetime,time
import collections
from flask import session
from utils.pgconnector import PgConnector
from utils.vcmsdbagent import VcmsDbAgent
from orm_models.vcmslicense import VcmsLicense
from orm_models.vcmslicenseencrypttype import VcmsLicenseEncryptType
from orm_models.vcmslicenseidtype import VcmsLicenseIdType
from orm_models.vcmslicensetrialtype import VcmsLicenseTrialType
from orm_models.vcmslicenserequest import VcmsLicenseRequest


class VcmsLicenseDbAgent :

    service = "app"

    def __init__(self) :
        pass

    def _get_all_license_encrypt_type_data(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsLicenseEncryptType). \
                                  filter(VcmsLicenseEncryptType.deprecated==0). \
                                  order_by(VcmsLicenseEncryptType.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "encrypt_type" : row.encrypt_type,
                                   "encrypt_name" : row.encrypt_name,
                                   "default_select" : row.default_select,
                                   "ct_user_sn" : row.ct_user_sn,
                                   "ut_user_sn" : row.ut_user_sn,
                                   "enabled" : row.enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_all_license_id_type_data(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsLicenseIdType). \
                                  filter(VcmsLicenseIdType.deprecated==0). \
                                  order_by(VcmsLicenseIdType.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "id_type" : row.id_type,
                                   "id_name" : row.id_name,
                                   "default_select" : row.default_select,
                                   "ct_user_sn" : row.ct_user_sn,
                                   "ut_user_sn" : row.ut_user_sn,
                                   "enabled" : row.enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_all_license_trial_type_data(self) :
        sql_connector = PgConnector(self.service)
        db_result = sql_connector.query(VcmsLicenseTrialType). \
                                  filter(VcmsLicenseTrialType.deprecated==0). \
                                  order_by(VcmsLicenseTrialType.sn.desc())
        return_data = collections.OrderedDict()
        for row in db_result :
            return_data[row.sn] = {
                                   "sn" : row.sn,
                                   "trial_type" : row.trial_type,
                                   "trial_name" : row.trial_name,
                                   "trial_days" : row.trial_days,
                                   "default_select" : row.default_select,
                                   "ct_user_sn" : row.ct_user_sn,
                                   "ut_user_sn" : row.ut_user_sn,
                                   "enabled" : row.enabled,
                                   "ct" : str(row.ct)
                                  }
        sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_license_request_data(self, company_sn):
        return_data = collections.OrderedDict()
        if company_sn > 0:
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsLicenseRequest). \
                filter(VcmsLicenseRequest.company_sn == company_sn). \
                filter(VcmsLicenseRequest.deprecated == 0). \
                order_by(VcmsLicenseRequest.sn.desc())
            for row in db_result:
                return_data[row.sn] = {
                    "sn": row.sn,
                    "company_sn": row.company_sn,
                    "company_name": row.company_name,
                    "service_name": row.service_name,
                    "license_feature": row.license_feature,
                    "version": row.version,
                    "trial_type": row.trial_type,
                    "start_date": row.start_date,
                    "expire_date": row.expire_date,
                    "license_count": row.license_count,
                    "batch_license_count": row.batch_license_count,
                    "ct_user_sn": row.ct_user_sn,
                    "ut_user_sn": row.ut_user_sn,
                    "enabled": row.enabled,
                    "ct": str(row.ct),
                    "ut": str(row.ut)
                }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_license_request_detail_data(self, sn):
        return_data = collections.OrderedDict()
        if sn > 0:
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsLicenseRequest). \
                filter(VcmsLicenseRequest.sn == sn). \
                filter(VcmsLicenseRequest.deprecated == 0). \
                order_by(VcmsLicenseRequest.sn.desc())
            for row in db_result:
                return_data[row.sn] = {
                    "sn": row.sn,
                    "company_sn": row.company_sn,
                    "company_name": row.company_name,
                    "encrypt_sn": row.encrypt_sn,
                    "encrypt_type": row.encrypt_type,
                    "service_sn": row.service_sn,
                    "service_name": row.service_name,
                    "license_feature": row.license_feature,
                    "version": row.version,
                    "trial_sn": row.trial_sn,
                    "trial_type": row.trial_type,
                    "id_sn": row.id_sn,
                    "id_type": row.id_type,
                    "hostid": row.hostid,
                    "start_date": row.start_date,
                    "expire_date": row.expire_date,
                    "connect_count": row.connect_count,
                    "server": row.server,
                    "port": row.port,
                    "license_count": row.license_count,
                    "batch_license_count": row.batch_license_count,
                    "ct_user_sn": row.ct_user_sn,
                    "ut_user_sn": row.ut_user_sn,
                    "enabled": row.enabled,
                    "ct": str(row.ct),
                    "ut": str(row.ut)
                }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_license_request_license_data(self, request_sn):
        return_data = collections.OrderedDict()
        if request_sn > 0:
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsLicense). \
                filter(VcmsLicense.request_sn == request_sn). \
                filter(VcmsLicense.deprecated == 0). \
                order_by(VcmsLicense.sn.desc())
            for row in db_result:
                return_data[row.sn] = {
                    "sn": row.sn,
                    "license_key": row.license_key,
                    "generate_type": row.generate_type,
                    "request_sn": row.request_sn,
                    "company_sn": row.company_sn,
                    "company_name": row.company_name,
                    "encrypt_type": row.encrypt_type,
                    "license_feature": row.license_feature,
                    "version": row.version,
                    "trial_type": row.trial_type,
                    "id_type": row.id_type,
                    "hostid": row.hostid,
                    "start_date": row.start_date,
                    "expire_date": row.expire_date,
                    "connect_count": row.connect_count,
                    "server": row.server,
                    "port": row.port,
                    "ct_user_sn": row.ct_user_sn,
                    "ut_user_sn": row.ut_user_sn,
                    "enabled": row.enabled,
                    "ct": str(row.ct),
                    "ut": str(row.ut)
                }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _get_company_license_detail_data(self, sn):
        return_data = collections.OrderedDict()
        if sn > 0:
            sql_connector = PgConnector(self.service)
            db_result = sql_connector.query(VcmsLicense). \
                filter(VcmsLicense.sn == sn). \
                filter(VcmsLicense.deprecated == 0). \
                order_by(VcmsLicense.sn.desc())
            for row in db_result:
                return_data[row.sn] = {
                    "sn": row.sn,
                    "license_key": row.license_key,
                    "generate_type": row.generate_type,
                    "request_sn": row.request_sn,
                    "company_sn": row.company_sn,
                    "company_name": row.company_name,
                    "encrypt_type": row.encrypt_type,
                    "license_feature": row.license_feature,
                    "version": row.version,
                    "trial_type": row.trial_type,
                    "id_type": row.id_type,
                    "hostid": row.hostid,
                    "start_date": row.start_date,
                    "expire_date": row.expire_date,
                    "connect_count": row.connect_count,
                    "server": row.server,
                    "port": row.port,
                    "ct_user_sn": row.ct_user_sn,
                    "ut_user_sn": row.ut_user_sn,
                    "enabled": row.enabled,
                    "ct": str(row.ct),
                    "ut": str(row.ut)
                }
            sql_connector.get_session().get_bind().close()
        return return_data

    def _add_company_license_request_data(self, parameters) :
        sql_connector = PgConnector(self.service)
        company_license_request = VcmsLicenseRequest(
                                             company_sn=parameters["company_sn"],
                                             company_name=parameters["company_name"],
                                             encrypt_sn=parameters["encrypt_sn"],
                                             encrypt_type=parameters["encrypt_type"],
                                             service_sn=parameters["service_sn"],
                                             service_name=parameters["service_name"],
                                             license_feature=parameters["license_feature"],
                                             version=parameters["version"],
                                             trial_sn=parameters["trial_sn"],
                                             trial_type=parameters["trial_type"],
                                             id_sn=parameters["id_sn"],
                                             id_type=parameters["id_type"],
                                             hostid=parameters["hostid"],
                                             start_date=parameters["start_date"],
                                             expire_date=parameters["expire_date"],
                                             connect_count=parameters["connect_count"],
                                             server=parameters["server"],
                                             port=parameters["port"],
                                             license_count=parameters["license_count"],
                                             batch_license_count=parameters["batch_license_count"],
                                             ct_user_sn=int(session["admin_id"])
                                            )
        sql_connector.get_session().add(company_license_request)
        sql_connector.get_session().commit()
        company_license_request_sn = company_license_request.sn
        sql_connector.get_session().get_bind().close()
        return company_license_request_sn

