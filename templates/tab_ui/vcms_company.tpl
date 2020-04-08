<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary tab-btn block-tooltip" 
          tab-href="#tab-content-{{data["page_back_tab"]}}">
    <i class="icon icon-add-w"></i>
    <span class="block-tooltip-top">{{data["add_company_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-10 position-r">{{data["sn_text"]}}</th>
        <th class="width-20">{{data["company_name_text"]}}</th>
        <th class="width-25">{{data["ct_text"]}}</th>
        <th class="width-10">{{data["status_text"]}}</th>
        <th class="width-45 ta-c">{{data["manage_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange">
      {% for key,value in data["company_list"].items() %}
      <tr class="column">
        <td class="width-10 position-r">{{value["sn"]}}</td>
        <td class="width-20">{{value["company_name"]}}</td>
        <td class="width-25">{{value["ct"]}}</td>
        <td class="width-10">
        {% if value["enabled"] == 1 %}
          {{data["enabled_text"]}}
        {% else %}
          {{data["disabeld_text"]}}
        {% endif %}
        </td>
        <td class="width-45">
          <button type="button" 
                  class="btn btn-primary company_profile"
                  data-title="{{data["company_profile_list_text"]}}" 
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["company_profile_tab"]}}" 
                  ajax_url="{{data["company_profile_url"]}}">
            <i class="icon icon-profile-w"></i>
          </button>
          <button type="button" 
                  class="btn btn-primary company_service"
                  data-title="{{data["company_service_list_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom" 
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["company_service_tab"]}}" 
                  ajax_url="{{data["company_service_url"]}}">
            <i class="icon icon-service-w"></i>
          </button>
          <button type="button" 
                  class="btn btn-primary company_account" 
                  data-title="{{data["company_account_list_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["company_account_tab"]}}" 
                  ajax_url="{{data["company_account_url"]}}">
            <i class="icon icon-account-management-w"></i>
          </button>
          <button type="button" 
                  class="btn btn-primary company_license_request"
                  data-title="{{data["company_license_request_list_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["company_license_request_tab"]}}"
                  ajax_url="{{data["company_license_request_url"]}}">
            <i class="icon icon-ca-w"></i>
          </button>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
