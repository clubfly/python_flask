<nav class="m-b-15">
  <div class="title">{{data["company_profile_text"]}}</div>
</nav>
<div class="layout-style-1 padding-15">
  <form class="company_profile-form" method="POST" action="{{data["upd_company_profile_url"]}}" tab_sn="{{data["company_profile_tab"]}}">
    <div class="form-input-group">
      <input type="text" value="{{data["company_profile_list"]["company_name"]}}" disabled/>
      <label class="input-label">{{data["company_name_text"]}}</label>
      <span class="danger input-error"></span>
      <input type="hidden" name="company_sn" value="{{data["company_profile_list"]["company_sn"]}}" />
    </div>
    <div class="form-input-group">
      <input type="text" name="company_no"
             id="company_no_error" 
             value="{{data["company_profile_list"]["company_no"] | replace("None","")}}"
             placeholder="{{data["text_placeholder_text"]}}"
             disabled />
      <label class="input-label">{{data["company_no_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="company_address" 
             id="company_address_error" 
             value="{{data["company_profile_list"]["company_address"] | replace("None","")}}"
             placeholder="{{data["text_placeholder_text"]}}"
             disabled />
      <label class="input-label">{{data["company_address_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="company_tel" 
             id="company_tel_error" 
             value="{{data["company_profile_list"]["company_tel"] | replace("None","")}}"
             placeholder="{{data["company_phone_placeholder_text"]}}"
             disabled />
      <label class="input-label">{{data["company_tel_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="company_contact" 
             id="company_contact_error" 
             value="{{data["company_profile_list"]["company_contact"] | replace("None","")}}"
             placeholder="{{data["text_placeholder_text"]}}"
             disabled />
      <label class="input-label">{{data["company_contact_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="company_contact_tel" 
             id="company_contact_tel_error" 
             value="{{data["company_profile_list"]["company_contact_tel"] | replace("None","")}}"
             placeholder="{{data["phone_placeholder_text"]}}"
             disabled />
      <label class="input-label">{{data["company_contact_tel_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="form-input-group">
      <input type="text" name="company_contact_email" 
             id="company_contact_email_error" 
             value="{{data["company_profile_list"]["company_contact_email"] | replace("None","")}}"
             placeholder="{{data["mail_placeholder_text"]}}"
             disabled />
      <label class="input-label">{{data["company_contact_email_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="ta-r">
      <button type="button" class="btn btn-primary edit_company_profile">{{data["edit_text"]}}</button>
      <button type="button" class="btn btn-light cancel_company_profile hidden">{{data["cancel_text"]}}</button>
      <button type="button" class="btn btn-primary save_company_profile hidden">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
