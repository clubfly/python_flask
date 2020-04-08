<div class="modal fade" id="modalCenterUpload" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title"></h5>
        <button type="button" class="close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <h4 class="h4 p-l-15 m-b-5">
        {{data["image_total_text"]}}<span id="upload_pic_total" 
                                          limitation="{{data["image_limit"]}}" 
                                          total="{{data["db_data_cnt"]}}">{{data["db_data_cnt"]}}</span>{{data["unit_text"]}}，
        {{data["uploading_text"]}}<span id="upload_enabled_pic">0</span>{{data["unit_text"]}}
        </h4>
        <form class="row add_company_product_image-form" 
              action="{{data["upload_product_image_url"]}}" 
              enctype="multipart/form-data" method="POST"
              tab_sn="{{data["company_product_image_tab"]}}">
          <div class="form-input-group layout-5">
            <div class="p-l-0 custom-file file-multiple">
              <input type="hidden" name="product_sn" value="{{data["product_sn"]}}" />
              <input type="file" name="thumbnail" 
                     accept="image/jpeg,image/jpg,image/png,image/svg+xml" 
                     class="custom-file-input" multiple 
                     id="thumbnail_error" />
              <label class="custom-file-label">{{data["selection_text"]}}</label>
              <span class="danger input-error"></span>
            </div>
          </div>
          <ul class="input-remark-wrapper layout-5 margin-0 m-t-15">
            <li>{{data["image_notice_1_text"]}}</li>
            <li>{{data["image_notice_2_text"]}}</li>
          </ul>
        </form>
        <ul class="multiple-images row"></ul>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-light cancel">{{data["cancel_text"]}}</button>
        <button type="button" class="btn btn-primary upload-images">{{data["save_text"]}}</button>
      </div>
    </div>
  </div>
</div>
<nav class="m-b-15">
  <button type="button" 
          class="btn btn-primary block-tooltip company_product"
          data_sn="{{data["service_sn"]}}"
          tab_sn="{{data["company_product_tab"]}}"
          page_sn="1"
          ajax_url="{{data["company_product_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_product_list_text"]}}</span>
  </button>
  {% if data["image_lock"] == 0 %}
    {% if data["product_enabled"] == 1 %}
  <button type="button" class="btn btn-primary block-tooltip upload">
    <i class="icon icon-upload-w"></i>
    <span class="block-tooltip-top">{{data["file_upload_text"]}}</span>
  </button>
  <button type="button" 
          class="btn btn-primary block-tooltip camera"
          data_sn="{{data["product_sn"]}}"
          ajax_url="{{data["upload_camera_image_url"]}}"
          tab_sn="{{data["company_product_image_tab"]}}"
          current_image_total="{{data["db_data_cnt"]}}"
          image_limit="{{data["image_limit"]}}">
    <i class="icon icon-camera-w"></i>
    <span class="block-tooltip-top">{{data["photo_text"]}}</span>
  </button>
    {% endif %}
  {% endif %}
  <div class="btn-group toolbar-wrapper">
    <label for="select-checkbox-all" class="btn btn-light block-tooltip">
      <input type="checkbox" id="select-checkbox-all" class="hidden" />
      <i class="icon icon-check"></i>
      <span class="block-tooltip-top">{{data["select_all_text"]}}</span>
    </label>
    <button type="button" 
            class="btn btn-light block-tooltip enable" 
            ajax_url="{{data["upd_company_product_image_status_url"]}}" 
            tab_sn="{{data["company_product_image_tab"]}}"
            product_sn="{{data["product_sn"]}}"
            page_sn="{{data["pages"]}}"
            disabled>
      <i class="icon icon-enable"></i>
      <span class="block-tooltip-top">{{data["enabled_text"]}}</span>
    </button>
    <button type="button" 
            class="btn btn-light block-tooltip disable" 
            ajax_url="{{data["upd_company_product_image_status_url"]}}" 
            tab_sn="{{data["company_product_image_tab"]}}"
            product_sn="{{data["product_sn"]}}"
            page_sn="{{data["pages"]}}"
            disabled>
      <i class="icon icon-disable"></i>
      <span class="block-tooltip-top">{{data["disabled_text"]}}</span>
    </button>
    <button type="button" 
            class="btn btn-light block-tooltip delete" 
            ajax_url="{{data["del_company_product_image_url"]}}" 
            tab_sn="{{data["company_product_image_tab"]}}"
            product_sn="{{data["product_sn"]}}"
            page_sn="{{data["pages"]}}"
            disabled>
      <i class="icon icon-delete"></i>
      <span class="block-tooltip-top">{{data["delete_text"]}}</span>
    </button>
  </div>
  <h4 class="h4 float-r m-t-15 m-b-5">
    {{data["product_name_text"]}}{{data["product_name"]}}，{{data["image_total_text"]}}
    <span>{{data["db_data_cnt"]}}</span>{{data["unit_text"]}}，{{data["uploading_text"]}}
    <span>{{data["image_limit"] - data["db_data_cnt"]}}</span>{{data["unit_text"]}}
  </h4>
</nav>
<div class="layout-style-1 layout-y-scroll">
  <ul class="images-list select-checkbox-wrapper row">
  {% if data["image_list"].items()|length > 0 %}
  {% for key,value in data["image_list"].items() %}
    <li class="layout-2-5 sublayer" id="del_{{value["sn"]}}">
      {% if value["enabled"] == 1 %}
      <div class="select-img-wrapper is-valid">
      {% else %}
      <div class="select-img-wrapper is-invalid">
      {% endif %}
        <label for="select-1-{{value["sn"]}}">
          <div>
            <input type="checkbox"
                   name="enabled"
                   class="select-checkbox data_status"
                   sysid="{{value["sn"]}}"
                   id="select-1-{{value["sn"]}}"
                   value="1" />
            <img src="{{value["thumbnail"]}}"/>
          </div>
        </label>
      </div>
    </li>
    {% endfor %}
  {% else %}
    <li>
      <div class="no-data-wrapper">
        <img src="/static/image/icon-picture.svg"/>
        <p>{{data["empty_product_text"]}}</p>
      </div>
    </li>
  {% endif %}
  </ul>
</div>
{{data["pagination"]}}
