<nav class="m-b-15">
  <div class="title">{{data["company_license_detail_text"]}}</div>
  <button type="button"
          class="btn btn-primary block-tooltip company_license"
          data_sn="{{data["company_sn"]}},{{data["license_list"]["request_sn"]}}"
          tab_sn="{{data["company_license_tab"]}}"
          ajax_url="{{data["company_license_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_license_ext"]}}</span>
  </button>
</nav>
<div class="layout-style-1 padding-15">
    <div class="form-input-group">
      <label class="input-label">{{data["company_name_text"]}}</label>
      <input type="text" value="{{data["license_list"]["company_name"]}}" class="input-with-icon input-icon-account" readonly/>
      <input type="hidden" name="company_sn" value="{{data["license_list"]["company_sn"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["license_feature_text"]}}</label>
      <input type="text" value="{{data["license_list"]["license_feature"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["license_key_text"]}}</label>
      <input type="text" value="{{data["license_list"]["license_key"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["encrypt_type_text"]}}</label>
      <input type="text" value="{{data["license_list"]["encrypt_type"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["version_text"]}}</label>
      <input type="text" value="{{data["license_list"]["version"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["trial_type_text"]}}</label>
      <input type="text" value="{{data["license_list"]["trial_type"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["id_type_text"]}}</label>
      <input type="text" value="{{data["license_list"]["id_type"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["hostid_text"]}}</label>
      <input type="text" value="{{data["license_list"]["hostid"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["start_date_text"]}}</label>
      <input type="text" value="{{data["license_list"]["start_date"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["expire_date_text"]}}</label>
      <input type="text" value="{{data["license_list"]["expire_date"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["connect_count_text"]}}</label>
      <input type="text" value="{{data["license_list"]["connect_count"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["server_text"]}}</label>
      <input type="text" value="{{data["license_list"]["server"]}}" readonly/>
    </div>
    <div class="form-input-group">
      <label class="input-label">{{data["port_text"]}}</label>
      <input type="text" value="{{data["license_list"]["port"]}}" readonly/>
    </div>
</div>
