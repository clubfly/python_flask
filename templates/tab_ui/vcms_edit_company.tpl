<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary tab-btn block-tooltip" 
          tab-href="#tab-content-2">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 padding-15">
  <form class="add_company-form" method="POST" action="{{data["add_company_url"]}}" tab_sn="2">
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
    <div class="ta-r">
      <button type="button" class="btn btn-primary save_company" tab_sn="2">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
