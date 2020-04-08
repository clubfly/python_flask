<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary block-tooltip company_service"
          data_sn="{{data["company_sn"]}}" 
          tab_sn="6" 
          ajax_url="{{data["company_service_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_service_list_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 padding-15">
  <form class="add_company_service-form" method="POST" action="{{data["upd_company_service_url"]}}" tab_sn="6">
    <div class="form-input-group">
      <input type="text" value="{{data["company_name"]}}" disabled/>
      <label class="input-label">{{data["company_name_text"]}}</label>
      <span class="danger input-error"></span>
      <input type="hidden" name="company_sn" value="{{data["company_sn"]}}" />
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
      <select name="per_product_image_cnt" id="per_product_image_cnt_error">
        {% for row in data["per_product_image_cnt_list"] %}
        <option value="{{row}}">{{row}}</option>
        {% endfor %}
      </select>
      <label class="input-label">{{data["per_product_image_cnt_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="max_product_cnt" id="max_product_cnt_error" />
      <label class="input-label">{{data["max_product_cnt_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="min_training_cnt" id="min_training_cnt_error" />
      <label class="input-label">{{data["min_training_cnt_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="detection_api" id="detection_api_ip_error" placeholder="{{data["api_format_text"]}}" />
      <label class="input-label">{{data["detection_api_ip_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="feature_api" id="feature_api_ip_error" placeholder="{{data["api_format_text"]}}" />
      <label class="input-label">{{data["feature_api_ip_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="pkl_update_api" id="pkl_update_api_ip_error" placeholder="{{data["api_format_text"]}}" />
      <label class="input-label">{{data["pkl_update_api_ip_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="ta-r">
      <button type="button" class="btn btn-primary save_company_service">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
