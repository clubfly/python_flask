<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary block-tooltip add_company_account" 
          data_sn="{{data["company_sn"]}}" 
          tab_sn="{{data["add_company_account"]}}" 
          ajax_url="{{data["add_company_account_url"]}}">
    <i class="icon icon-add-w"></i>
    <span class="block-tooltip-top">{{data["add_company_account_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-10 position-r">{{data["company_name_text"]}}</th>
        <th class="width-15">{{data["account_text"]}}</th>
        <th class="width-15">{{data["user_rank_sn_text"]}}</th>
        <th class="width-10">{{data["status_text"]}}</th>
        <th class="width-50" ta-c>{{data["manage_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange">
      {% for key,value in data["account_list"].items() %}
      <tr class="column">
        <td class="width-10 position-r">{{value["company_name"]}}</td>
        <td class="width-15">{{value["account"]}}</td>
        <td class="width-15">{{value["user_rank_name"]}}</td>
        <td class="width-10">
        {% if value["enabled"] == 1 %}
          {{data["enabled_text"]}}
        {% else %}
          {{data["disabeld_text"]}}
        {% endif %}
        </td>
        <td class="width-50">
          <button type="button" 
                  class="btn btn-primary account_password"
                  data-title="{{data["account_change_pwd_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["account_password_tab"]}}" 
                  ajax_url="{{data["account_change_pwd_url"]}}">
            <i class="icon icon-password-w"></i>
          </button>
          <button type="button" 
                  class="btn btn-primary bind_service_account"
                  data-title="{{data["bind_service_account_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["bind_service_account_tab"]}}" 
                  ajax_url="{{data["bind_service_account_url"]}}">
            <i class="icon icon-account-management-w"></i>
          </button>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
