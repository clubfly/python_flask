from flask import render_template,session,escape,redirect

def vcms_logout(self,functions,actions,html_template,page_settings,parameter_dict) :
    session.clear()
    return redirect("/vcms_login/view")
