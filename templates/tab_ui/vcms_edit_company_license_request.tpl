<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary block-tooltip company_license_request"
          data_sn="{{data["company_sn"]}}"
          tab_sn="{{data["company_license_request_tab"]}}"
          ajax_url="{{data["company_license_request_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_license_request_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 padding-15">
  <form class="upd_company_license_request-form" method="POST" action="{{data["upd_company_license_request_url"]}}" tab_sn="{{data["company_license_request_tab"]}}">
    <div class="form-input-group">
      {% if data["company_sn"] > 0 %}
      <input type="text" value="{{data["company_name"]}}" class="input-with-icon input-icon-account" disabled/>
      {% else %}
      <input type="text" name="company_name" value="" id="company_name_error" />
      <label class="input-label">{{data["company_name_text"]}}</label>
      <span class="danger input-error"></span>
      {% endif %}
      <input type="hidden" name="company_sn" value="{{data["company_sn"]}}" />
    </div>
    <div class="form-input-group">
      <select name="encrypt_sn" id="encrypt_sn_error">
        {% for key,value in data["license_encrypt_list"].items() %}
        {% if value["default_select"] > 0 %}
        <option selected="true" value="{{key}}">{{value["encrypt_name"]}}-{{value["encrypt_type"]}}</option>
        {% else %}
        <option value="{{key}}">{{value["encrypt_name"]}}-{{value["encrypt_type"]}}</option>
        {% endif %}
        {% endfor %}
      </select>
      <label class="input-label">{{data["license_encrypt_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <select name="service_sn" id="service_sn_error">
        {% for key,value in data["service_list"].items() %}
        <option value="{{key}}">{{value["service_name"]}}-{{value["service_type"]}}</option>
        {% endfor %}
      </select>
      <label class="input-label">{{data["service_list_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="version" id="version_error" value="{{data["version"]}}" title="{{data["version_pattern_text"]}}" required />
      <label class="input-label">{{data["version_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <select name="trial_sn" id="trial_sn_error">
        {% for key,value in data["license_trial_list"].items() %}
        {% if value["default_select"] > 0 %}
        <option selected="true" value="{{key}}">{{value["trial_name"]}}-{{value["trial_type"]}}</option>
        {% else %}
        <option value="{{key}}">{{value["trial_name"]}}-{{value["trial_type"]}}</option>
        {% endif %}
        {% endfor %}
      </select>
      <label class="input-label">{{data["license_trial_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <select name="id_sn" id="id_sn_error">
        {% for key,value in data["license_id_type_list"].items() %}
        {% if value["default_select"] > 0 %}
        <option selected="true" value="{{key}}">{{value["id_name"]}}-{{value["id_type"]}}</option>
        {% else %}
        <option value="{{key}}">{{value["id_name"]}}-{{value["id_type"]}}</option>
        {% endif %}
        {% endfor %}
      </select>
      <label class="input-label">{{data["license_id_type_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="hostid" id="hostid_error" value="" />
      <label class="input-label">{{data["hostid_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="date" name="start_date" id="start_date_error" value="{{data["start_date"]}}" required />
      <label class="input-label">{{data["start_date_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="date" name="expire_date" id="expire_date_error" value="{{data["expire_date"]}}" required />
      <label class="input-label">{{data["expire_date_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="number" name="connect_count" id="connect_count_error" value="" />
      <label class="input-label">{{data["connect_count_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="server" id="server_error" value="" />
      <label class="input-label">{{data["server_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="port" id="port_error" value="" />
      <label class="input-label">{{data["port_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="number" name="license_count" id="license_count_error" value="1" />
      <label class="input-label">{{data["license_count_text"]}}</label>
      <span class="danger input-error"></span>
      <input type="hidden" name="batch_license_count" value="{{data["batch_license_count"]}}" />
    </div>
    <div class="ta-r">
      <button type="button" class="btn btn-primary save_company_license_request" tab_sn="{{data["add_company_license_request"]}}">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
