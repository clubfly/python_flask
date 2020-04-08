<nav class="m-b-15">
  <button type="button" class="btn btn-primary block-tooltip company_product"
          data_sn="{{data["service_sn"]}}"
          tab_sn="{{data["company_product_tab"]}}"
          page_sn="1"
          ajax_url="{{data["company_product_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_product_list_text"]}}</span>
  </button>
  <button type="button" class="btn btn-primary block-tooltip upload_product_log"
          data_sn="{{data["service_sn"]}}"
          tab_sn="{{data["product_csv_log_tab"]}}"
          page_sn="1"
          ajax_url="{{data["product_csv_log_url"]}}">
    <i class="icon icon-productlist-w"></i>
    <span class="block-tooltip-top">{{data["history_text"]}}</span>
  </button>
</nav>
<div id="tabs" class="layout-style-1">
  <ul>
    <li><a href="#sub_tabs-1">{{data["tab_title_1_text"]}}</a></li>
    <!--<li><a href="#sub_tabs-2">{{data["tab_title_2_text"]}}</a></li>-->
  </ul>
  <div id="sub_tabs-1">
    <div class="row tabs-content-wrapper">
      <div class="layout-5 border-r">
        <span class="title m-b-15">{{data["product_upload_text"]}}</span>
        <div class="p-b-20">
          <h4 class="h4 m-b-5">{{data["step_text"]}}：</h4>
          <ol class="list-style-decimal">
            <li>
              {{data["step_1_text"]}}：
              <a class="link-style" href="{{data["download_product_sample_csv_url"]}}">
                {{data["sample_download_text"]}}
              </a>
            </li>
            <li>{{data["step_2_text"]}}</li>
            <li>{{data["step_3_text"]}}</li>
            <li>{{data["step_4_text"]}}</li>
          </ol>           
        </div>
        <form id="products_csv_upload_form" class="ta-r"
              method="POST"
              enctype="multipart/form-data"
              action="{{data["upload_company_product_csv_url"]}}"
              tab_sn="0">
          <div class="form-input-remark-wrapper">
            <input type="hidden" name="service_sn" value="{{data["service_sn"]}}" />
            <div class="form-input-group" id="file-single-csv-products">
              <span class="input-title">{{data["product_csv_text"]}}</span>
              <input type="file" name="csv_products" 
                     accept=".csv" 
                     class="custom-file-input"
                     id="products_csv" />
              <label class="custom-file-label">{{data["unselected_file"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <ul class="input-remark-wrapper">
              <li>{{data["csv_only_text"]}}</li>
            </ul>
          </div>
          <button type="button" class="btn btn-primary products_csv_upload">{{data["upload_text"]}}</button>
        </form>
      </div>
      <div class="layout-5">
        <span class="title">{{data["product_info_download_text"]}}</span>
        <form id="products_csv_download_form" class="m-t-10 m-b-10 ta-r"
              method="POST"
              action="{{data["download_product_csv_url"]}}"
              tab_sn="0">
          <input type="hidden" name="service_sn" value="{{data["service_sn"]}}" />
          <div class="row">
            <div class="form-input-group-sm layout-5">
              <input type="text"
                     name="product_sn"
                     class="product_sn"  />
              <label class="input-label">{{data["search_product_sn_text"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <div class="form-input-group-sm layout-5">
              <input type="text"
                     name="product_name"
                     class="product_name" />
              <label class="input-label">{{data["search_product_name_text"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <div class="form-input-group-sm layout-5">
              <input type="text"
                     name="abbreviation"
                     class="abbreviation" />
              <label class="input-label">{{data["search_abbreviation_text"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <div class="form-input-group-sm layout-5">
              <input type="text"
                     name="barcode"
                     class="barcode" />
              <label class="input-label">{{data["search_barcode_text"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <div class="layout-10">
              <div class="form-input-group-wrapper">
                <p class="input-title">{{data["search_product_create_time_text"]}}</p>
                <div class="row" id="datepicker-group-3">
                  <div class="form-input-group-sm layout-4-5">
                    <input type="text"
                           readonly="readonly"
                           name="ct_start_date"
                           class="datepicker start_date ct_start_date" />
                    <label class="input-label">{{data["search_start_day_text"]}}</label>
                    <span class="danger input-error start_date_error"></span>
                  </div>
                  <div class="form-input-group-sm layout-1"> ~ </div>
                  <div class="form-input-group-sm layout-4-5">
                    <input type="text"
                           readonly="readonly"
                           name="ct_end_date"
                           class="datepicker end_date ct_end_date" />
                    <label class="input-label">{{data["search_end_day_text"]}}</label>
                    <span class="danger input-error end_date_error"></span>
                  </div>
                </div>
              </div>
            </div>
            <div class="layout-10">
              <div class="form-input-group-wrapper">
                <p class="input-title">{{data["search_product_update_time_text"]}}</p>
                <div class="row" id="datepicker-group-4">
                  <div class="form-input-group-sm layout-4-5">
                    <input type="text"
                           readonly="readonly"
                           name="ut_start_date"
                           class="datepicker start_date ut_start_date" />
                    <label class="input-label">{{data["search_start_day_text"]}}</label>
                    <span class="danger input-error start_date_error"></span>
                  </div>
                  <div class="form-input-group-sm layout-1"> ~ </div>
                  <div class="form-input-group-sm layout-4-5">
                    <input type="text"
                           readonly="readonly"
                           name="ut_end_date"
                           class="datepicker end_date ut_end_date" />
                    <label class="input-label">{{data["search_end_day_text"]}}</label>
                    <span class="danger input-error end_date_error"></span>
                  </div>
                </div>
              </div>
            </div>
            <div class="form-input-group-sm layout-5">
              <select name="image_cnt" class="image_cnt">
                <option value="">{{data["search_all_text"]}}</option>
                <option value="1">{{data["search_yes_text"]}}</option>
                <option value="0">{{data["search_no_text"]}}</option>
              </select>
              <label class="input-label">{{data["search_image_cnt_text"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <div class="form-input-group-sm layout-5">
              <select name="enabled" class="enabled">
                <option value="">{{data["search_all_text"]}}</option>
                <option value="1">{{data["enabled_text"]}}</option>
                <option value="0">{{data["disabled_text"]}}</option>
              </select>
              <label class="input-label">{{data["search_product_status_text"]}}</label>
              <span class="danger input-error"></span>
            </div>
          </div>
          <button type="button" class="btn btn-primary float-r products_csv_download">{{data["download_text"]}}</button>
        </form>
      </div>
    </div>
  </div>
  <!--<div id="sub_tabs-2">
    <div class="row tabs-content-wrapper">
      <div class="layout-5 border-r">
        <span class="title m-b-15">{{data["image_upload_text"]}}</span>
        <button type="button" class="btn btn-primary block-tooltip upload_image_log"
                data_sn="{{data["service_sn"]}}"
                tab_sn="{{data["product_image_csv_log_tab"]}}"
                page_sn="1"
                ajax_url="{{data["product_image_csv_log_url"]}}">
          <i class="icon icon-productlist-w"></i>
          <span class="block-tooltip-top">{{data["history_text"]}}</span>
        </button>
        <form id="images_csv_upload_form" class="ta-r"
              method="POST"
              enctype="multipart/form-data"
              action="{{data["upload_company_product_image_csv_url"]}}"
              tab_sn="0">
          <input type="hidden" name="service_sn" value="{{data["service_sn"]}}" />
          <div>
            <div class="form-input-group" id="file-single-csv-images">
              <span class="input-title">{{data["product_csv_text"]}}</span>
              <input type="file" name="csv_images" 
                     accept=".csv" 
                     class="custom-file-input"
                     id="images_csv" />
              <label class="custom-file-label">{{data["unselected_file"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <ul class="input-remark-wrapper">
              <li>{{data["csv_only_text"]}}</li>
            </ul>
            <div class="form-input-group" id="file-single-zip-images">
              <span class="input-title">{{data["product_zip_text"]}}</span>
              <input type="file" name="zip_images" 
                     accept="application/zip,application/x-zip,application/x-zip-compressed,application/octet-stream" 
                     class="custom-file-input"
                     id="images_zip" />
              <label class="custom-file-label">{{data["unselected_file"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <ul class="input-remark-wrapper">
              <li>{{data["zip_only_text"]}}</li>
            </ul>
          </div>
          <a href="{{data["download_product_image_sample_csv_url"]}}" 
             download="product_image_sample.csv" class="btn btn-light">{{data["sample_download_text"]}}</a>
          <button type="button" class="btn btn-primary images_csv_upload">{{data["upload_text"]}}</button>
        </form>
      </div>
      <div class="layout-5"></div>
    </div>
  </div>-->
</div>
<script>
$(function(){
  $("#tabs").tabs();
  $(".datepicker", document).datepicker({
    maxDate: "0D",
    dateFormat: 'yy-mm-dd',
    numberOfMonths: 1,
    showButtonPanel: true,
    closeText: 'Clear',
    onSelect: function() {
      var data = {
        'error_text': [input_start_date_error_text, input_end_date_error_text]
      };
      datepicker_check_date_data_loader(this, data);
    }
  });
});
</script>
