<nav class="m-b-15">
  <div class="title">{{data["company_service_text"]}}</div>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-20 position-r">{{data["company_name_text"]}}</th>
        <th class="width-20">{{data["service_name_text"]}}</th>
        <th class="width-20">{{data["max_product_cnt_text"]}}</th>
        <th class="width-40">{{data["manage_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange">
      {% for key,value in data["service_list"].items() %}
        {% if value["deprecated"] == 0 %}
      <tr class="column">
        <td class="width-20 position-r">
          <div class="column-xs">{{data["company_name_text"]}}</div>
          {{value["company_name"]}}
        </td>
        <td class="width-20">
          <div class="column-xs">{{data["service_name_text"]}}</div>
          <script>document.write(service_name_{{value["service_sn"]}});</script>
        </td>
        <td class="width-20">
          <div class="column-xs">{{data["max_product_cnt_text"]}}</div>
          {{value["max_product_cnt"]}}
        </td>
        <td class="width-40">
          <div class="column-xs">{{data["manage_text"]}}</div>
          <button type="button" 
                  class="btn btn-primary company_product"
                  data-title="{{data["company_product_list_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["company_product_tab"]}}" 
                  ajax_url="{{data["company_product_url"]}}">
            <i class="icon icon-productlist-w"></i>
          </button>
        {% if data["company_sn"] != 14 %}
          <button type="button"
                  class="btn btn-primary self_test"
                  data-title="{{data["company_product_self_test_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}"
                  tab_sn="{{data["self_test_tab"]}}"
                  ajax_url="{{data["upd_pkl_file_url"]}}{{value["sn"]}}">
            <i class="icon icon-focus-w"></i>
          </button>
          {% if data["publish_pkl"] == 1 %}
            {% if value["sn"] != 14 and value["pkl_update_api"] != "" and value["pkl_update_api"] is not none %}
          <button type="button"
                  class="btn btn-primary deploy_pkl"
                  data-title="{{data["pkl_deployment_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}"
                  tab_sn="0"
                  ajax_url="{{data["deploy_pkl_url"]}}{{value["sn"]}}">
            <i class="icon icon-deploy-w"></i>
          </button>
            {% endif %}
          {% endif %}
        {% endif %}
        </td>
      </tr>
        {% endif %}
      {% endfor %}
    </tbody>
  </table>
</div>
