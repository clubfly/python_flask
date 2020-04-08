<nav class="m-b-15 row">
  <div class="layout-md-5 layout-sm-10 layout-xs-10 padding-0 ta-l">
    <button type="button" class="btn btn-primary block-tooltip add_company_product"
            data_sn="{{data["service_sn"]}}"
            tab_sn="{{data["add_company_product_tab"]}}"
            page_sn="{{data["pages"]}}"
            ajax_url="{{data["add_company_product_url"]}}">
      <i class="icon icon-add-w"></i>
      <span class="block-tooltip-top">{{data["add_product_text"]}}</span>
    </button>
    <div class="btn-group dropdown">
      <button type="button" class="btn btn-primary dropdown-toggle block-tooltip" aria-expanded="false">
        <i class="icon icon-batch-w"></i>
        <span class="block-tooltip-top">{{data["import_text"]}}</span>
      </button>
      <div class="dropdown-menu dropdown-menu-left">
        <a class="dropdown-item add_batch_company_product"
           data_sn="{{data["service_sn"]}}"
           tab_sn="{{data["add_batch_company_product_tab"]}}"
           ajax_url="{{data["upd_batch_product_url"]}}">
           {{data["import_text"]}}
        </a>
        <a class="dropdown-item upload_product_log"
           data_sn="{{data["service_sn"]}}"
           tab_sn="{{data["product_csv_log_tab"]}}"
           page_sn="1"
           ajax_url="{{data["product_csv_log_url"]}}">
           {{data["history_text"]}}
        </a>
      </div>
    </div>
    <div class="btn-group toolbar-wrapper">
      <label for="select-checkbox-all" class="btn btn-light block-tooltip">
        <input type="checkbox" id="select-checkbox-all" class="hidden" />
        <i class="icon icon-check"></i>
        <span class="block-tooltip-top">{{data["select_all_text"]}}</span>
      </label>
      <button type="button"
              class="btn btn-light block-tooltip enable"
              ajax_url="{{data["upd_company_product_status_url"]}}"
              tab_sn="{{data["company_product_tab"]}}"
              product_sn="0"
              page_sn="{{data["pages"]}}"
              disabled>
        <i class="icon icon-enable"></i>
        <span class="block-tooltip-top">{{data["enabled_text"]}}</span>
      </button>
      <button type="button"
              class="btn btn-light block-tooltip disable"
              ajax_url="{{data["upd_company_product_status_url"]}}"
              tab_sn="{{data["company_product_tab"]}}"
              product_sn="0"
              page_sn="{{data["pages"]}}"
              disabled>
        <i class="icon icon-disable"></i>
        <span class="block-tooltip-top">{{data["disabled_text"]}}</span>
      </button>
      <button type="button"
              class="btn btn-light block-tooltip delete"
              ajax_url="{{data["del_company_product_url"]}}"
              tab_sn="{{data["company_product_tab"]}}"
              product_sn="0"
              page_sn="{{data["pages"]}}"
              disabled>
        <i class="icon icon-delete"></i>
        <span class="block-tooltip-top">{{data["delete_text"]}}</span>
      </button>
    </div>
    <button type="button" class="btn btn-light block-tooltip modal_search_btn"
            tab_sn="{{data["company_product_tab"]}}"
            data_sn="{{data["service_sn"]}}">
      <i class="icon icon-search"></i>
      <span class="block-tooltip-top">{{data["search_rule_title_text"]}}</span>
    </button>
  </div>
  <div class="layout-md-5 layout-sm-10 layout-xs-10 padding-0 ta-r">
    <h4 class="h4 m-b-5 m-t-5">
      {{data["product_total_text"]}}{{data["product_enabled_totals"]}}/{{data["product_totals"]}}, &nbsp;{{data["image_total_text"]}}：{{data["image_enabled_totals"]}}/{{data["image_totals"]}}
    </h4>
  </div>
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-4 position-r"></th>
        <th class="width-10">
          {{data["product_sn_text"]}}
          <!-- <i class="icon icon-sort-w icon-sm"></i> -->
        </th>
        <th class="width-10">
          {{data["thumbnail_text"]}}
        </th>
        <th class="width-10">
          {{data["barcode_text"]}}
        </th>
        <th class="width-25">
          {{data["product_name_text"]}}
          <!-- <i class="icon icon-sort-w icon-sm"></i> -->
        </th>
        <th class="width-13">
          {{data["abbreviation_text"]}}
          <!-- 標籤 -->
        </th>
        <th class="width-10">
          {{data["image_total_text"]}}
          <!-- <i class="icon icon-sort-w icon-sm"></i> -->
        </th>
        <th class="width-5">
          {{data["status_text"]}}
        </th>
        <th class="width-13 ta-c">
          {{data["manage_text"]}}
        </th>
      </tr>
    </thead>
    <tbody class="hover-orange select-checkbox-wrapper" id="scrollDiv" onscroll="scrollInside()">
      {% if data["product_list"].items()|length > 0 %}
      {% for key,value in data["product_list"].items() %}
      <tr class="column sublayer">
        <td class="width-4 position-r">
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
        <td class="width-25">
          <div class="column-xs">{{data["product_name_text"]}}</div>
          <div class="column-span-group">
            <span data-title="{{value["product_name"]}}" data-toggle="tooltip" data-placement="bottom">{{value["product_name"]}}</span>
          </div>
        </td>
        <td class="width-13">
          <div class="column-xs">{{data["abbreviation_text"]}}</div>
          <div class="column-span-group">
            <span data-title="{{value["abbreviation"]}}" data-toggle="tooltip" data-placement="bottom">{{value["abbreviation"]}}</span>
          </div>
        </td>
        <td class="width-10">
          <div class="column-xs">{{data["image_total_text"]}}</div>
            <span data-title="{{value["image_totals"]}}" data-toggle="tooltip" data-placement="bottom">{{value["image_totals"]}}</span>
        </td>
        <td class="width-5">
          <div class="column-xs">{{data["status_text"]}}</div>
            {% if value["enabled"] == 1 %}
              ON
            {% else %}
              OFF
            {% endif %}
        </td>
        <td class="width-13 ta-c">
          <div class="column-xs">{{data["manage_text"]}}</div>
          <button type="button" 
                  class="btn btn-light m-b-5 edit_product"
                  data-title="{{data["edit_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["add_company_product_tab"]}}" 
                  page_sn="{{data["pages"]}}" 
                  ajax_url="{{data["upd_product_url"]}}">
            <i class="icon icon-edit"></i>
          </button>
          <button type="button" 
                  class="btn btn-secondary m-b-5 company_product_image"
                  data-title="{{data["image_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["sn"]}}" 
                  tab_sn="{{data["company_product_image_tab"]}}" 
                  page_sn="{{data["pages"]}}" 
                  ajax_url="{{data["company_product_image_url"]}}">
            <i class="icon icon-picture-w"></i>
          </button>
        </td>
      </tr>
      {% endfor %}
      {% else %}
      <tr>
        <td class="padding-0">
          <div class="no-data-wrapper">
            <img src="/static/image/icon-productlist.svg"/>
            <p>{{data["empty_product_text"]}}</p>
          </div>
        </td>
      </tr>
      {% endif %}
    </tbody>
  </table>
</div>
{{data["pagination"]}}
