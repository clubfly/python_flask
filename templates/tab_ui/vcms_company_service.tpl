<nav class="m-b-15">
  <button type="button" class="btn btn-primary add_company_service" 
          data_sn="{{data["company_sn"]}}" tab_sn="9" ajax_url="{{data["add_company_service_url"]}}">
    <i class="icon icon-add-w"></i>{{data["add_company_service_text"]}}
  </button>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-10 position-r">{{data["company_name_text"]}}</th>
        <th class="width-10">{{data["service_name_text"]}}</th>
        <th class="width-10">{{data["service_type_text"]}}</th>
        <th class="width-15">{{data["per_product_image_cnt_text"]}}</th>
        <th class="width-15">{{data["max_product_cnt_text"]}}</th>
        <th class="width-12">{{data["min_training_cnt_text"]}}</th>
        <th class="width-10" ta-c>{{data["status_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange">
      {% for key,value in data["service_list"].items() %}
      <tr class="column">
        <td class="width-10 position-r">{{value["company_name"]}}</td>
        <td class="width-10">{{value["service_name"]}}</td>
        <td class="width-10">{{value["service_type"]}}</td>
        <td class="width-15">{{value["per_product_image_cnt"]}}</td>
        <td class="width-15">{{value["max_product_cnt"]}}</td>
        <td class="width-12">{{value["min_training_cnt"]}}</td>
        <td class="width-10">
        {% if value["enabled"] == 1 %}
          {{data["enabled_text"]}}
        {% else %}
          {{data["disabeld_text"]}}
        {% endif %}
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
