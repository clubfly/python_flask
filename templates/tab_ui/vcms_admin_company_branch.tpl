{% if data["company_sn"] != 14 %}
<nav class="m-b-15">
  <button type="button" class="btn btn-primary block-tooltip add_company_branch"
          data_sn="{{data["company_sn"]}}" 
          tab_sn="{{data["add_company_branch_tab"]}}"
          ajax_url="{{data["add_company_branch_url"]}}">
    <i class="icon icon-add-w"></i>
    <span class="block-tooltip-top">{{data["add_company_branch_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-10 position-r">{{data["company_name_text"]}}</th>
        <th class="width-20">{{data["branch_name_text"]}}</th>
        <th class="width-70" ta-c>{{data["manage_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange">
      {% for key,value in data["branch_list"].items() %}
      <tr class="column">
        <td class="width-10 position-r">{{value["company_name"]}}</td>
        <td class="width-20">{{value["branch_name"]}}</td>
        <td class="width-70">
          <button type="button"
                  class="btn btn-primary branch_account_manage"
                  data-title="{{data["company_account_list_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["branch_account_manage_tab"]}}"
                  ajax_url="{{data["branch_account_manage_url"]}}">
            <i class="icon icon-account-management-w"></i>
          </button>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
{% endif %}
