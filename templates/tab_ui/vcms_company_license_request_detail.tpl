<nav class="m-b-15">
  <div class="title">{{data["company_license_request_detail_text"]}}</div>
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
    <div class="form-input-group">
      <label class="input-label">{{data["company_name_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["company_name"]}}" class="input-with-icon input-icon-account" readonly/>
      <input type="hidden" name="company_sn" value="{{data["license_request_list"]["company_sn"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["encrypt_type_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["encrypt_type"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["service_name_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["service_name"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["license_feature_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["license_feature"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["version_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["version"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["trial_type_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["trial_type"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["id_type_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["id_type"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["hostid_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["hostid"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["start_date_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["start_date"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["expire_date_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["expire_date"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["connect_count_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["connect_count"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["server_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["server"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["port_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["port"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["license_count_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["license_count"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["batch_license_count_text"]}}</label>
      <input type="text" value="{{data["license_request_list"]["batch_license_count"]}}" readonly/>
    </div>
</div>
