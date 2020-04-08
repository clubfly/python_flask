<nav class="m-b-15 recognition-methods-button">
  <button type="button" class="btn btn-primary block-tooltip company_product"
          data_sn="{{data["service_sn"]}}"
          tab_sn="{{data["company_product_tab"]}}"
          page_sn="1"
          ajax_url="{{data["company_product_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_product_list_text"]}}</span>
  </button>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-15">{{data["service_name_text"]}}</th>
        <th class="width-20">{{data["file_text"]}}</th>
        <th class="width-15">{{data["data_total_text"]}}</th>
        <th class="width-25">{{data["ct_text"]}}</th>
        <th class="width-15">{{data["status_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange select-checkbox-wrapper tbody-tr-h-76" id="scrollDiv" onscroll="scrollInside()">
      {% for key,value in data["log_list"].items() %}
      <tr class="column">
        <td class="width-15 service_names" service="{{value["system_service_sn"]}}">
        </td>
        <td class="width-20">
          <div class="column-xs">{{data["file_text"]}}</div>
          <span>{{value["user_file_name"]}}</span>
        </td>
        <td class="width-15">
          <div class="column-xs">{{data["data_total_text"]}}</div>
          <span>{{value["data_total"]}}</span>
        </td>
        <td class="width-25">
          <div class="column-xs">{{data["ct_text"]}}</div>
          <span>{{value["ct"]}}</span>
        </td>
        <td class="width-15">
          <div class="column-xs">{{data["status_text"]}}</div>
          {% if value["enabled"] == 1 %}
            {% if value["file_manage_mark"] == 1 %}
              {% if value["error_mark"] == 1 %}
          <a href="{{data["download_product_csv_log_url"]}}?service_sn={{value["service_sn"]}}&csv={{value["sn"]}}"
             class="btn btn-sm btn-light">{{data["import_error_text"]}}</a>
              {% else %}
                {{data["success_text"]}}
              {% endif %}
            {% else %}
              {{data["processing_text"]}}
            {% endif %}
          {% else %}
            {{data["empty_data_text"]}}
          {% endif %}
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
<script>
    $(function(){
      $(".service_names").each(function(){
        var service_sn = $(this).attr("service");
        var text = eval("service_name_"+service_sn);
        $(this).text(text);
      });
    });
</script>
