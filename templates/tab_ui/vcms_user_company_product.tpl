<nav class="m-b-15 row">
  <div class="layout-md-5 layout-sm-10 layout-xs-10 padding-0 ta-l">
    <div class="btn-group toolbar-wrapper">
      <label for="select-checkbox-all" class="btn btn-light block-tooltip">
        <input type="checkbox" id="select-checkbox-all" class="hidden" />
        <i class="icon icon-check"></i>
        <span class="block-tooltip-top">{{data["select_all_text"]}}</span>
      </label>
      <button type="button"
              class="btn btn-light block-tooltip enable"
              ajax_url="{{data["upd_company_branch_product_status_url"]}}"
              tab_sn="3"
              product_sn="0"
              page_sn="{{data["pages"]}}"
              disabled>
        <i class="icon icon-enable"></i>
        <span class="block-tooltip-top">{{data["enabled_text"]}}</span>
      </button>
      <button type="button"
              class="btn btn-light block-tooltip disable"
              ajax_url="{{data["upd_company_branch_product_status_url"]}}"
              tab_sn="3"
              product_sn="0"
              page_sn="{{data["pages"]}}"
              disabled>
        <i class="icon icon-disable"></i>
        <span class="block-tooltip-top">{{data["disabled_text"]}}</span>
      </button>
    </div>
  </div>
  <div class="layout-md-5 layout-sm-10 layout-xs-10 padding-0 ta-r">
    <h4 class="h4 m-b-5 m-t-5">
    </h4>
  </div>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-3 position-r"></th>
        <th class="width-10">{{data["product_sn_text"]}}</th>
        <th class="width-10">{{data["thumbnail_text"]}}</th>
        <th class="width-10">{{data["barcode_text"]}}</th>
        <th class="width-20">{{data["product_name_text"]}}</th>
        <th class="width-12">{{data["abbreviation_text"]}}</th>
        <th class="width-10">{{data["status_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange select-checkbox-wrapper" id="scrollDiv" onscroll="scrollInside()">
      {% if data["product_list"].items()|length > 0 %}
      {% for key,value in data["product_list"].items() %}
      <tr class="column sublayer">
        <td class="width-3 position-r">
          <div class="column-xs">#</div>
          <label for="select-1-{{value["sn"]}}" class="position-c"></label>
          <input type="checkbox"
                 name="enabled"
                 class="select-checkbox data_status"
                 sysid="{{value["sn"]}}"
                 id="select-1-{{value["sn"]}}"
                 value="1" />
          <div class="clear"></div>
        </td>
        <td class="width-10">
          <div class="column-xs">{{data["product_sn_text"]}}</div>
          <span data-title="{{value["sku"]}}" data-toggle="tooltip" data-placement="bottom">{{value["sku"]}}</span>
        </td>
        <td class="width-10">
          <div class="column-xs">{{data["thumbnail_text"]}}</div>
          <div class="table-img-wrapper">
            <img src="{{value["thumbnail"]}}"/>
          </div>
        </td>
        <td class="width-10">
          <div class="column-xs">{{data["barcode_text"]}}</div>
          <span data-title="{{value["barcode"]}}" data-toggle="tooltip" data-placement="bottom">{{value["barcode"]}}</span>
        </td>
        <td class="width-20">
          <div class="column-xs">{{data["product_name_text"]}}</div>
          <div class="column-span-group">
            <span data-title="{{value["product_name"]}}" data-toggle="tooltip" data-placement="bottom">{{value["product_name"]}}</span>
          </div>
        </td>
        <td class="width-12">
          <div class="column-xs">{{data["abbreviation_text"]}}</div>
          <div class="column-span-group">
            <span data-title="{{value["abbreviation"]}}" data-toggle="tooltip" data-placement="bottom">{{value["abbreviation"]}}</span>
          </div>
        </td>
        <td class="width-10">
          <div class="column-xs">{{data["status_text"]}}</div>
          {% if value["enabled"] == 1 %}
              ON
          {% else %}
              OFF
          {% endif %}
        </td>
      </tr>
      {% endfor %}
      {% else %}
      <tr>
        <td class="padding-0">
          <div class="no-data-wrapper">
            <img src="/static/image/icon-productlist.svg"/>
            <p>目前無資料</p>
          </div>
        </td>
      </tr>
      {% endif %}
    </tbody>
  </table>
</div>
{{data["pagination"]}}
