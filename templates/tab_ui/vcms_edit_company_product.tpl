<nav class="m-b-15">
  <button type="button" class="btn btn-primary block-tooltip company_product"
          data_sn="{{data["service_sn"]}}" 
          tab_sn="{{data["company_product_tab"]}}" 
          page_sn="{{data["pages"]}}" 
          ajax_url="{{data["company_product_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_product_list_text"]}}</span>
  </button>
</nav>
<div>
  <form class="add_company_product-form layout-style-1 padding-15 row" 
        method="POST" 
        enctype="multipart/form-data" 
        action="{{data["upd_company_product_url"]}}" 
        tab_sn="{{data["company_product_tab"]}}">
    <div class="layout-4-5">
      <div class="upload-image-wrapper">
        {% if data["product_sn"] == 0 %}
        <img src="/static/image/default_image.svg" class="upload-image" />
        {% else %}
        <img src="{{data["thumbnail"]}}" class="upload-image" />
        {% endif %}
        <span class="input-label">{{data["thumbnail_text"]}}</span>
      </div>
      <div class="ta-c padding-15">
        <div class="form-input-group">
          <div class="p-l-0 custom-file file-single">
            <input type="hidden" name="service_sn" id="service_sn" value="{{data["service_sn"]}}" />
            <input type="hidden" name="product_sn" value="{{data["product_sn"]}}" />
            <input type="hidden" name="pages" value="{{data["pages"]}}" />
            <input type="file" name="thumbnail" 
                   accept="image/jpeg,image/jpg,image/png,image/svg+xml" 
                   class="custom-file-input" 
                   id="thumbnail_error"/>
            <label class="custom-file-label">{{data["selection_text"]}}</label>
            <span class="danger input-error"></span>
          </div>
        </div>
        <ul class="input-remark-wrapper margin-0">
          <li>{{data["image_notice_1_text"]}}</li>
          <li>{{data["image_notice_2_text"]}}</li>
        </ul>
      </div>
    </div>
    <div class="layout-5-5 row">
      <div class="form-input-group layout-10">
        <input type="text" name="sku" id="sku_error" value="{{data["sku"]}}" />
        <label class="input-label">{{data["product_sn_text"]}}{{data["required_text"]}}</label>
        <span class="danger input-error"></span>
      </div>
      <div class="form-input-group layout-10">
        <input type="text" name="product_name" id="product_name_error" value="{{data["product_name"]}}" />
        <label class="input-label">{{data["product_name_text"]}}{{data["required_text"]}}</label>
        <span class="danger input-error"></span>
      </div>
      <div class="form-input-group layout-10">
        <input type="text" name="abbreviation" id="abbreviation_error" value="{{data["abbreviation"]}}" />
        <label class="input-label">{{data["abbreviation_text"]}}</label>
        <span class="danger input-error"></span>
      </div>
      <div class="form-input-group layout-10">
        <input type="text" name="barcode" id="barcode_error" value="{{data["barcode"]}}" />
        <label class="input-label">{{data["barcode_text"]}}</label>
        <span class="danger input-error"></span>
      </div>
      {% if data["system_service_sn"] == 9 %}
      <div class="form-input-group layout-10">
        <select name="category" id="select-category" class="select-input" placeholder="{{data["select_category_text"]}}"></select>
        <label class="input-label">{{data["category_text"]}}</label>
        <span class="danger input-error"></span>
      </div>
      {% else %}
        <input type="hidden" name="category" value="0" />
      {% endif %}
    </div>
    <div class="width-100 ta-r">
      <button type="button" class="btn btn-primary save_company_product">{{data["save_text"]}}</button>
    </div>
  </form>
</div>
{% if data["system_service_sn"] == 9 %}
<script>
$(function(){
  var options = {
              "en" : [
                      { class: service_name_9, value: '', name:'{{data["search_all_text"]}}'},
                      { class: service_name_9, value: '1', name:'Plain white rice' },
                      { class: service_name_9, value: '2', name:'Brown rice' }
                     ],
              "ja" : [
                      { class: service_name_9, value: '', name:'{{data["search_all_text"]}}'},
                      { class: service_name_9, value:'1', name:'ごはん' },
                      { class: service_name_9, value:'2', name:'健康米' }
                     ],
              "zh" : [
                      { class: service_name_9, value: '', name:'{{data["search_all_text"]}}'},
                      { class: service_name_9, value:'1', name:'白飯' },
                      { class: service_name_9, value:'2', name:'糙米飯' }
                     ]
             };
  $('#select-category').selectize({
    options: options[language_symbol],
    optgroupField: 'class',
    labelField: 'name',
    searchField: ['name'],
    render: {
      optgroup_header: function(data, escape) {
        return '<div class="optgroup-header">' + escape(data.label) + ' <span class="scientific">' + escape(data.label_scientific) + '</span></div>';
      }
    }
  });
  {% if data["category"] is none %}
  $('#select-category')[0].selectize.setValue('');
  {% else %}
  $('#select-category')[0].selectize.setValue('{{data["category"]}}');
  {% endif %}
});
</script>
{% endif %}
