from flask import jsonify,render_template,session,escape,request,make_response
from utils.htmlbuilder import HtmlBuilder
from utils.vcmsadminfunction import VcmsAdminFunction
import uuid

def vcms_download_product_log_csv(self,functions,actions,html_template,page_settings,parameter_dict) :
    return_data = {}
    if session["user_rank_sn"] == 3 :
        return_data = VcmsAdminFunction().download_company_product_error_csv_log(page_settings,parameter_dict)
        if int(return_data["code"]) == 1 :
            filename = str(uuid.uuid4()).replace("-","")
            response = make_response(return_data["data"])
            response.headers['Content-Disposition'] = 'attachment; filename='+filename+'.csv'
            response.headers['Content-Type'] = 'text/html; charset=utf-8'
            response.mimetype='text/csv'
            return response
    return jsonify(return_data)
