<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary block-tooltip company_branch"
          data_sn="{{data["company_sn"]}}" 
          tab_sn="{{data["company_branch_tab"]}}" 
          ajax_url="{{data["company_branch_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_branch_list_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 padding-15">
  <form class="add_company_branch-form" method="POST" action="{{data["upd_company_branch_url"]}}" tab_sn="4">
    <div class="form-input-group">
      <input type="text" name="branch_name" id="branch_name_error" />
      <label class="input-label">{{data["branch_name_text"]}}</label>
      <span class="danger input-error"></span>
    </div>
    <div class="ta-r">
      <button type="button" class="btn btn-primary save_company_branch">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
