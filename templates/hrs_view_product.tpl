{{header_footer_data["header_html"]}}
<div class="content-wrapper rwd-ma-15">
  <article class="row hrs-wrapper">
    <div class="layout-style-1 table-scroll">
      <table class="table">
        <thead>
          <tr>
            <!-- <th class="width-5 position-r"></th> -->
            <th class="width-30">公司名稱</th>
            <th class="width-45">服務名稱</th>
            <th class="width-25">自我測試圖資</th>
          </tr>
        </thead>
        <tbody class="hover-orange select-checkbox-wrapper tbody-height-1" id="scrollDiv" onscroll="scrollInside()">
          {% for key,value in data["company_list"].items() %}
          <tr class="column sublayer">
            <!-- <td class="width-5 position-r"></td> -->
            <td class="width-30">{{value["company_name"]}}</td>
            <td class="width-45">
            {% for key2,value2 in value["service_list"].items() %}
              <a href="{{data['hrs_view_product_detail_url']}}{{data['token']}}?service_sn={{value2['sn']}}"
                 class="btn btn-light m-b-5"
                 data-title="{{value2['service_name']}}"
                 data-toggle="tooltip"
                 data-placement="bottom">
                <i class="icon service-icon-{{value2['service_sn']}}"></i>
              </a>
            {% endfor %}
            </td>
            <td class="width-25">
              {% if value["folder_list"] %}
              <select name="folder" class="folder" company_sn="{{key}}" token="{{data['token']}}">
                <option value="" selected="selected">- Date -</option>
                {% for row in value["folder_list"] %}
                <option value="{{row}}">{{value["image_total_list"][row]}}</option>
                {% endfor %}
              </select>
              {% endif %}
            </td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </article>
  {{data["pagination"]}}
</div>
{{header_footer_data["footer_html"]}}
<script>
$(function(){
  hrs_view_self_test_image_url = "{{data['hrs_view_self_test_image_url']}}";
  $(document).on("change",".folder",function(){
    var company_sn = $(this).attr("company_sn");
    var folder = $(this).val();
    var token = $(this).attr("token");
    url = hrs_view_self_test_image_url + token + "?company_sn="+company_sn+"&folder="+folder
    top.location.href=url;
  });
});
</script>
