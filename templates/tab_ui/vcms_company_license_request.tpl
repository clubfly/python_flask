<nav class="m-b-15">
  <div class="title">{{data["company_license_request_text"]}}</div>
  <button type="button"
          class="btn btn-primary block-tooltip add_company_license_request"
          data_sn="{{data["company_sn"]}}"
          tab_sn="{{data["add_company_license_request"]}}"
          ajax_url="{{data["add_company_license_request_url"]}}">
    <i class="icon icon-add-w"></i>
    <span class="block-tooltip-top">{{data["add_company_license_request_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-15 position-r">{{data["company_name_text"]}}</th>
        <th class="width-15">{{data["service_name_text"]}}</th>
        <th class="width-20">{{data["expire_date_text"]}}</th>
        <th class="width-10">{{data["license_count_text"]}}</th>
        <th class="width-10">{{data["batch_license_count_text"]}}</th>
        <th class="width-10">{{data["status_text"]}}</th>
        <th class="width-20 ta-c">{{data["manage_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange">
      {% for key,value in data["license_request_list"].items() %}
      <tr class="column">
        <td class="width-15 position-r">
            {{value["company_name"]}}
        </td>
        <td class="width-15">
            {{value["service_name"]}}({{value["version"]}})
        </td>
        <td class="width-20">
            {{value["expire_date"]}}({{value["trial_type"]}})
        </td>
        <td class="width-10">
            {{value["license_count"]}}
        </td>
        <td class="width-10">
            {{value["batch_license_count"]}}
        </td>
        <td class="width-10">
            {% if value["enabled"] == 1 %}
              {{data["enabled_text"]}}
            {% else %}
              {{data["disabeld_text"]}}
            {% endif %}
        </td>
        <td class="width-20">
          <button type="button"
                  class="btn btn-primary company_license_request_detail"
                  data-title="{{data["company_license_request_detail_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}"
                  tab_sn="{{data["company_license_request_tab"]}}"
                  ajax_url="{{data["company_license_request_detail_url"]}}">
            <i class="icon icon-ca-w"></i>
          </button>
          <button type="button"
                  class="btn btn-primary company_license"
                  data-title="{{data["company_license_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["company_sn"]}},{{value["sn"]}}"
                  tab_sn="{{data["company_license_tab"]}}"
                  ajax_url="{{data["company_license_url"]}}">
            <i class="icon icon-ca-w"></i>
          </button>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
