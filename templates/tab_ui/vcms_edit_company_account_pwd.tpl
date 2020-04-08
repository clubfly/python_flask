<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary block-tooltip company_account"
          data_sn="{{data["company_sn"]}}" 
          tab_sn="{{data["company_account_tab"]}}" 
          ajax_url="{{data["company_account_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_account_list_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 padding-15">
  <form class="change-pwd_form" action="{{data["upd_account_pwd_url"]}}" method="POST" tab_sn="{{data["company_account_tab"]}}">
    <div class="form-input-group">
      <input type="text" value="{{data["account"]}}" disabled/>
      <label class="input-label">{{data["account_text"]}}</label>
      <input type="hidden" name="user_sn" value="{{data["user_sn"]}}" />
    </div>
    <div class="form-input-group">
      <input type="password" name="new_password" class="new_password" id="npwd_error" />
      <label class="input-label">{{data["new_pwd_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="password" name="confirm_password" class="confirm_new_password" id="cpwd_error" />
      <label class="input-label">{{data["confirm_pwd_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="ta-r">
      <button type="button" class="btn btn-primary save-change-pwd">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
