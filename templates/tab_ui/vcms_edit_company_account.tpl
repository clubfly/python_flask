<nav class="m-b-15">
  <button type="button" class="btn btn-primary company_account"
          data_sn="{{data["company_sn"]}}" tab_sn="{{data["company_account_tab"]}}" 
          ajax_url="{{data["company_account_url"]}}">
    <i class="icon icon-back-w"></i>{{data["back_to_company_account_list_text"]}}
  </button>
</nav>
<div class="layout-style-1 padding-15">
  <form class="add_company_account-form" method="POST" 
        action="{{data["upd_company_account_url"]}}" tab_sn="{{data["company_account_tab"]}}">
    <div class="form-input-group">
      <input type="text" value="{{data["company_name"]}}" disabled/>
      <label class="input-label">{{data["company_name_text"]}}</label>
      <span class="danger input-error"></span>
      <input type="hidden" name="company_sn" value="{{data["company_sn"]}}" />
    </div>
    <div class="form-input-group">
      <input type="text" name="account" id="account_error" />
      <label class="input-label">{{data["account_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="password" name="new_password" class="new_password" id="new_pwd_error" />
      <label class="input-label">{{data["new_pwd_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="password" name="confirm_password" class="confirm_new_password" id="confirm_pwd_error" />
      <label class="input-label">{{data["confirm_pwd_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <select name="user_rank_sn" id="user_rank_sn_error">
        {% for key,value in data["user_rank_list"].items() %}
        <option value="{{key}}">{{value["rank_name"]}}</option>
        {% endfor %}
      </select>
      <label class="input-label">{{data["user_rank_sn_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="ta-r">
      <button type="button" class="btn btn-primary save_company_account">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
