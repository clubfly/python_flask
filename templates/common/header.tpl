<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
    <meta http-equiv="content-language" content="zh-Hant-TW" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="0" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="format-detection" content="telephone=no" />
    <title>{{data["web_title_text"]}}</title>
    {% for css,css_value in data["css"].items() %}
    <link rel="stylesheet" type="text/css" href="/static/{{css_value}}?t={{data["seeds"]}}" />
    {% endfor %}
    <script>
sku_dialog = "{{data["sku_dialog_1_text"]}}<br />{{data["sku_dialog_2_text"]}}<br /><br />{{data["sku_dialog_3_text"]}}";
check_sku_url = "{{data["check_sku_url"]}}";
menu_service_setting = "{{data["menu_service_setting_text"]}}";
menu_company = "{{data["menu_company_text"]}}";
menu_service_list = "{{data["menu_service_list_text"]}}";
menu_branch = "{{data["menu_branch_text"]}}";
menu_customer = "{{data["menu_customer_text"]}}";
menu_customer_service = "{{data["menu_customer_service_text"]}}";
menu_system = "{{data["menu_system_text"]}}";
menu_recognition = "{{data["menu_recognition_text"]}}";
menu_system_announcement = "{{data["menu_system_announcement_text"]}}"
logout_api = "{{data["logout_url"]}}";
session_api = "{{data["check_session_url"]}}";
language_api = "{{data["change_language_url"]}}";
pkl_update_msg = "{{data["pkl_update_msg"]}}";
self_test_url = "{{data["self_test_api_url"]}}";
confirm_title = "{{data["confirm_title_text"]}}";
enabled_dialog = "{{data["enabled_dialog_text"]}}";
disabled_dialog = "{{data["disabled_dialog_text"]}}";
delete_dialog = "{{data["delete_dialog_text"]}}";
dialog_notice = "{{data["dialog_notice_text"]}}";
confirm_upload_file = "{{data["confirm_upload_file_text"]}}";
modal_title_camera = "{{data["modal_title_camera_text"]}}";
modal_title_upload = "{{data["modal_title_upload_text"]}}";
unselected_file = "{{data["unselected_file_text"]}}";
check_limitation_message = "{{data["check_limitation_message_text"]}}";
check_files_size_message = "{{data["check_files_size_message_text"]}}";
recognition_test_no_results = "{{data["recognition_test_no_results_text"]}}";
languages = "{{data["current_language"]}}";
unselected_file = "{{data['unselected_file']}}";
input_required_text = "{{data['input_required_text']}}";
input_format_error_text = "{{data['input_format_error_text']}}";
input_datepicker_error_text = "{{data['input_datepicker_error_text']}}";
input_start_date_error_text = "{{data['input_start_date_error_text']}}";
input_end_date_error_text = "{{data['input_end_date_error_text']}}";
service_name_1 = "{{data["service_name_1"]}}";
service_name_2 = "{{data["service_name_2"]}}";
service_name_3 = "{{data["service_name_3"]}}";
service_name_4 = "{{data["service_name_4"]}}";
service_name_5 = "{{data["service_name_5"]}}";
service_name_6 = "{{data["service_name_6"]}}";
service_name_7 = "{{data["service_name_7"]}}";
service_name_8 = "{{data["service_name_8"]}}";
service_name_9 = "{{data["service_name_9"]}}";
search_rule_title = "{{data["search_rule_title_text"]}}";
language_symbol = "{{data['sop_map']}}";
    </script>
    {% for js,js_value in data["js"].items() %}
      {% if js == "2" %}
        {% if data["permission_js"] != "" %}
    <script type="text/javascript" src="/static/js/{{data["permission_js"]}}?t={{data["seeds"]}}"></script>
        {% endif %}
      {% endif %}
    <script type="text/javascript" src="/static/{{js_value}}?t={{data["seeds"]}}"></script>
    {% endfor %}
  </head>
  <body class="bg-cube">
    {% if data["header_hide"] == 0 %}
    <header class="row">
      <div class="layout-3 layout-sm-3 layout-md-6 align-self-center">
        <div class="header-logo-warpper">
          <img src="/static/image/logo.svg" class="header-logo"/>
          <a href="#" title="{{data["web_title_text"]}}" class="header-link"></a>
        </div>
        <h1 class="header-title hidden-sm p-l-15">Visual Content Management System</h1>
      </div>
      <div class="layout-7 layout-sm-7 layout-md-4 align-self-center ta-r">
        <div class="btn-group dropdown">
          <button type="button" class="btn btn-sm btn-light dropdown-toggle" aria-expanded="false">
            {{data["sop_text"]}}
          </button>
          <div class="dropdown-menu dropdown-menu-right">
            <a class="dropdown-item sop-btn" language="{{data["sop_map"]}}" img="1">{{data["prepare_for_bread_text"]}}</a>
            <a class="dropdown-item sop-btn" language="{{data["sop_map"]}}" img="2">{{data["recognition_for_bread_text"]}}</a>
            <a class="dropdown-item sop-btn" language="{{data["sop_map"]}}" img="3">{{data["recognition_for_product_text"]}}</a>
          </div>
        </div>
        <div class="btn-group dropdown">
          <button type="button" class="btn btn-sm btn-light dropdown-toggle" aria-expanded="false">
            {{data["language_name"]}}
          </button>
          <div class="dropdown-menu dropdown-menu-right">
            {% for ks,vs in data["language_support"].items() %}
              {% if vs["accept"] == 1 %}
            <a class="dropdown-item change_language" language="{{vs["alias"][0]}}">{{vs["name"]}}</a>
              {% endif %}
            {% endfor %}
          </div>
        </div>
        <div class="btn-group dropdown">
          <button type="button" class="btn btn-sm btn-light dropdown-toggle" aria-expanded="false">
            <i class="icon icon-user"></i> {{data["account"]}}
          </button>
          <div class="dropdown-menu dropdown-menu-right">
            <a class="dropdown-item tab-btn" tab-href="#tab-content-1">{{data["change_pwd_text"]}}</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{{data["logout_url"]}}">{{data["logout_text"]}}</a>
          </div>
        </div>
      </div>
    </header>
    {% endif %}
    <main>
