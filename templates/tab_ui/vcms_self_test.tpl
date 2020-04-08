<nav class="m-b-15 recognition-methods-button">
  <h2 class="title m-r-15">{{data["company_product_self_test_text"]}}</h2>
  <button type="button"
          class="btn btn-primary tab-btn block-tooltip self_test_close"
          tab-href="#tab-content-3">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_company_service_list_text"]}}</span>
  </button>
  <button type="button"
          class="btn btn-primary block-tooltip recognition-methods-camera focus">
    <i class="icon icon-camera-w"></i>
    <span class="block-tooltip-top">{{data["pic_test_text"]}}</span>
  </button>
  <button type="button"
          class="btn btn-primary block-tooltip recognition-methods-upload">
    <i class="icon icon-upload-w"></i>
    <span class="block-tooltip-top">{{data["upload_test_text"]}}</span>
  </button>
</nav>
<div class="row">
  <section class="layout-10 layout-sm-10 layout-md-10 layout-lg-7 flex-height left-flex-height p-l-0">
    <div class="outer-frame-box-shadow flex-outer-frame-control">
      <div class="recognition-methods recognition-methods-1">
        <div id="videostream-RT">
          <video autoplay></video>
          <img id="source-img-RT"/>
          <svg id="contour-wrapper" xmlns="http://www.w3.org/2000/svg"></svg>
        </div>
        <div class="m-b-15 ta-c">
          <button type="button" 
                  class="btn btn-primary screenshot-button-RT" 
                  api_url="{{data["self_test_api_url"]}}" disabled>
            {{data["company_product_self_test_text"]}}
          </button>
          <button type="button" class="btn btn-primary re-checkout hidden">{{data["repeat_text"]}}</button>
        </div>
      </div>
      <div class="recognition-methods recognition-methods-2 hidden">
        <div class="upload-image-wrapper image-position-wrapper">
          <div class="draw-wrapper">
            <img src="/static/image/default_image.svg" 
                 class="upload-image position-unset" 
                 id="upload-img-RT" />
          </div>
        </div>
        <div class="form-input-group">
          <div class="p-l-0 custom-file file-single">
            <form class="self_test_image-form"
                  method="POST"
                  enctype="multipart/form-data"
                  action="{{data["self_test_api_url"]}}"
                  tab_sn="0">
              <input type="file"
                     name="thumbnail"
                     accept="image/jpeg,image/jpg,image/png,image/svg+xml" 
                     class="custom-file-input image_recongintion" />
              <label class="custom-file-label">{{data["selection_text"]}}</label>
              <span class="danger input-error"></span>
            </form>
          </div>
        </div>
        <ul class="input-remark-wrapper margin-0">
          <li>{{data["image_notice_1_text"]}}</li>
          <li>{{data["image_notice_2_text"]}}</li>
        </ul>
        <div class="m-t-15 m-b-15 ta-c">
          <button type="button" class="btn btn-primary upload-RT">{{data["company_product_self_test_text"]}}</button>
          <button type="button" class="btn btn-primary re-checkout hidden">{{data["repeat_text"]}}</button>
        </div>
      </div>
    </div>
  </section>
  <section class="layout-10 layout-sm-10 layout-md-10 layout-lg-3 flex-height right-flex-height p-r-0">
    <div class="outer-frame-box-shadow flex-outer-frame-control">
      <ul class="outer-frame-overflow-y"></ul>
    </div>
  </section>
</div>
