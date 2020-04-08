{{header_footer_data["header_html"]}}
<div class="modal fade" id="modalHrsImage" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-1200">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title"></h5>
        <button type="button" class="close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body ta-c"></div>
    </div>
  </div>
</div>
<div class="content-wrapper rwd-ma-15">
  <nav class="hrs-nav-style row">
    <div class="layout-6-5">
      <h2 class="title m-r-15">{{data["company_name"]}}</h2>
      <a class="btn btn-primary block-tooltip" href="{{data['hrs_view_product_url']}}{{data['token']}}">
        <i class="icon icon-back-w"></i>
        <span class="block-tooltip-down">返回公司列表</span>
      </a>
    </div>
    <div class="layout-3-5">
      <h2 class="h4 ta-r m-b-5 m-t-5">{{data["forder"]}} ({{data["image_total"]}})</h2>
    </div>
  </nav>
  <article class="row hrs-wrapper">
    <ul class="layout-style-1 layout-y-scroll row hrs-image-list-wrapper">
      {% for row in data["image_list"] %}
      <li class="layout-lg-3-3 layout-md-5 layout-sm-10 hrs-image-list">
        <img src="data:image/jpg;base64,{{row['b64']}}"/>
        <p class="file-name">{{row["file_name"]}}</p>
      </li>
      {% endfor %}
    </ul>
  </article>
  {{data["pagination"]}}
</div>
{{header_footer_data["footer_html"]}}
<script>
$(function(){
  $(document).on("click", ".hrs-image-list img", function(){
    var model_data = {
      'display': 1,
      'modal-element': '#modalHrsImage',
      'modal-title': '',
      'img-url': $(this).attr('src')
    };
    modal_hrs_img_data_loader(model_data);
  });
  function modal_hrs_img_data_loader(data){
    if(data['display'] == 0) {
      modalClose();
    }
    if(data['display'] == 1) {
      modalHrsImgShow(data);
    }
  }
  function modalHrsImgShow(model_data){
    // modal hrs img
    title_msg = "error";
    body_msg = "Please confirm your value to modalShow.";
    if(model_data != undefined){
      title_msg = model_data['modal-title'];
    }
    $(model_data['modal-element']+' .modal-title').text(title_msg);
    $(model_data['modal-element']+' .modal-body').html('<img src="'+model_data['img-url']+'" class="hrs-model-img"/>');
  
    modalTemplate = '<div class="modal-backdrop fade show"></div>';
    if($(model_data['modal-element']).length > 0){
      $('.modal-backdrop').remove();
      $('body').addClass('modal-open').append(modalTemplate);
      $(model_data['modal-element']).addClass('show').slideDown(300);
    }
  }
});
</script>
