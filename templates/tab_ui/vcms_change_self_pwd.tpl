<div class="layout-style-1 padding-15">
  <form class="change-self-pwd_form" action="{{data["upd_self_pwd_url"]}}" method="POST" tab_sn="1">
    <div class="form-input-group">
      <input type="text" value="{{data["account"]}}" class="input-with-icon input-icon-account" disabled/>
      <input type="hidden" name="user_id" value="{{data["admin_id"]}}" />
    </div>
    <div class="form-input-group">
      <input type="password" name="old_password" class="current_password" id="current_password_error" />
      <label class="input-label">{{data["current_pwd_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="password" name="new_password" class="new_password" id="new_password_error" />
      <label class="input-label">{{data["new_pwd_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="password" name="confirm_password" class="confirm_new_password" id="confirm_password_error" />
      <label class="input-label">{{data["confirm_pwd_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="ta-r">
      <button type="button" class="btn btn-primary save-change-self-pwd">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
