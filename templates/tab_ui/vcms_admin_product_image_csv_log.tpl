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
        <th class="width-30">{{data["file_text"]}}</th>
        <th class="width-15">{{data["data_total_text"]}}</th>
        <th class="width-15">{{data["ct_text"]}}</th>
        <th class="width-15" ta-c>{{data["status_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange select-checkbox-wrapper" id="scrollDiv" onscroll="scrollInside()">
      {% for key,value in data["log_list"].items() %}
      <tr class="column">
        <td class="width-15">{{value["service_name"]}}</td>
        <td class="width-30">{{value["user_file_name"]}}</td>
        <td class="width-15">{{value["data_total"]}}</td>
        <td class="width-15">{{value["ct"]}}</td>
        <td class="width-15 ta-c">{{value["status"]}}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
