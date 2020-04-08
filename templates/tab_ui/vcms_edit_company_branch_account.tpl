<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary block-tooltip branch_account_manage"
          data_sn="{{data["branch_sn"]}}" 
          tab_sn="{{data["branch_account_manage_tab"]}}" 
          ajax_url="{{data["branch_account_manage_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_branch_account_list_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 padding-15">
  <form class="add_company_branch_account-form" method="POST" 
        action="{{data["upd_company_branch_account_url"]}}" tab_sn="{{data["branch_account_manage_tab"]}}">
    <div class="form-input-group">
      <input type="text" value="{{data["company_name"]}}" disabled/>
      <label class="input-label">{{data["company_name_text"]}}</label>
      <span class="danger input-error"></span>
      <input type="hidden" name="branch_sn" value="{{data["branch_sn"]}}" />
    </div>
    <div class="form-input-group">
      <input type="text" name="account" id="account_error" />
      <label class="input-label">{{data["branch_account_text"]}}</label>
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
    <div class="ta-r">
      <button type="button" class="btn btn-primary save_company_branch_account">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
