<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary iblock-tooltip company_account"
          data_sn="{{data["company_sn"]}}" 
          tab_sn="7" 
          ajax_url="{{data["company_account_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_account_list_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 padding-15">
  <form class="bind_service-form" method="POST" 
        action="{{data["upd_bind_service_account_url"]}}" tab_sn="{{data["bind_service_tab"]}}">
    {% for key,value in data["company_service_list"].items() %}
    <div class="form-input-group">
      {% if value["user_enabled"] == 1 %}
      <input type="checkbox" name="company_service_sn" value="{{value["sn"]}}" 
             id="service_sn_{{data[value["sn"]]}}_error" checked="checked" />
      {% else %}
      <input type="checkbox" name="company_service_sn" value="{{value["sn"]}}" 
             id="service_sn_{{data[value["sn"]]}}_error" />
      {% endif %}
      <label>{{value["service_name"]}} - {{value["service_type"]}}</label>
      <span class="danger input-error"></span>
    </div>
    {% endfor%}
    <input type="hidden" name="company_sn" value="{{data["company_sn"]}}" />
    <input type="hidden" name="user_sn" value="{{data["user_sn"]}}" />
    <div class="ta-r">
      <button type="button" class="btn btn-primary save-bind-service">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
