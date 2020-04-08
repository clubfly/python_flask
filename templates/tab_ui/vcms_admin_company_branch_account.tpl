<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary block-tooltip add_company_branch_account"
          data_sn="{{data["branch_sn"]}}" 
          tab_sn="{{data["add_company_branch_account_tab"]}}"
          ajax_url="{{data["add_company_branch_account_url"]}}">
    <i class="icon icon-add-w"></i>
    <span class="block-tooltip-top">{{data["add_company_branch_account_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-15 position-r">{{data["branch_name_text"]}}</th>
        <th class="width-15">{{data["account_text"]}}</th>
        <th class="width-10">{{data["user_rank_sn_text"]}}</th>
        <th class="width-10">{{data["status_text"]}}</th>
        <th class="width-50" ta-c>{{data["manage_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange">
      {% for key,value in data["account_list"].items() %}
      <tr class="column">
        <td class="width-15 position-r">{{value["branch_name"]}}</td>
        <td class="width-15">{{value["account"]}}</td>
        <td class="width-10">{{value["user_rank_name"]}}</td>
        <td class="width-10">
        {% if value["enabled"] == 1 %}
          {{data["enabled_text"]}}
        {% else %}
          {{data["disabled_text"]}}
        {% endif %}
        </td>
        <td class="width-50">
          <button type="button" 
                  class="btn btn-primary account_password" 
                  data-title="{{data["account_change_pwd_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["company_account_tab"]}}"
                  ajax_url="{{data["account_change_pwd_url"]}}">
            <i class="icon icon-password-w"></i>
          </button>
          {% if value["enabled"] == 1 %}
          <button type="button"
                  class="btn btn-light save_account_status"
                  data-title="{{data["disabled_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}"
                  tab_sn="{{data["branch_account_manage_tab"]}}"
                  status_sn="0"
                  ajax_url="{{data["upd_account_status_url"]}}"
                  page_sn="1">
            <i class="icon icon-disable"></i>
          </button>
          {% else %}
            <button type="button"
                  class="btn btn-light save_account_status"
                  data-title="{{data["enabled_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}"
                  status_sn="1"
                  tab_sn="{{data["branch_account_manage_tab"]}}"
                  ajax_url="{{data["upd_account_status_url"]}}"
                  page_sn="1">
            <i class="icon icon-enable"></i>
          </button>
          {% endif %}
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
