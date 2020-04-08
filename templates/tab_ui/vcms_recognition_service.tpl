<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-10 position-r">{{data["sn_text"]}}</th>
        <th class="width-25">{{data["service_name_text"]}}</th>
        <th class="width-25">{{data["service_type_text"]}}</th>
        <th class="width-30">{{data["ct_text"]}}</th>
        <th class="width-20 ta-c">{{data["status_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange">
      {% for key,value in data["service_list"].items() %}
      <tr class="column">
        <td class="width-10 position-r">{{value["sn"]}}</td>
        <td class="width-25">{{value["service_name"]}}</td>
        <td class="width-25">{{value["service_type"]}}</td>
        <td class="width-30">{{value["ct"]}}</td>
        <td class="width-20">
        {% if value["enabled"] == 1 %}
          {{data["enabled_text"]}}
        {% else %}
          {{data["disabled_text"]}}
        {% endif %}
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
