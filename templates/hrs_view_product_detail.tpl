{{header_footer_data["header_html"]}}
<div class="content-wrapper rwd-ma-15">
  <nav class="hrs-nav-style row">
    <div class="layout-5">
      <h2 class="title m-r-15">{{data["company_name"]}}</h2>
      <a class="btn btn-primary block-tooltip" href="{{data["hrs_view_product_url"]}}{{data["token"]}}">
        <i class="icon icon-back-w"></i>
        <span class="block-tooltip-down">返回公司列表</span>
      </a>
      <a class="btn btn-primary block-tooltip" href="{{data["hrs_view_product_detail_url"]}}{{data["token"]}}?service_sn={{data["service_sn"]}}">
        <i class="icon icon-back-w"></i>
        <span class="block-tooltip-down">返回商品清單</span>
      </a>
      <div class="input-group">
        <input type="text" class="form-control" id="search_product" placeholder="請輸入商品名稱">
        <div class="input-group-append">
          <button type="button" class="btn btn-light block-tooltip search_product">
            <i class="icon icon-search"></i>
            <span class="block-tooltip-down">搜尋</span>
          </button>
        </div>
      </div>
    </div>
    <div class="layout-5"></div>
  </nav>
  <article class="row hrs-wrapper">
    <div class="layout-style-1 table-scroll">
      <table class="table">
        <thead>
          <tr>
            <!-- <th class="width-5 position-r"></th> -->
            <th class="width-30">商品名稱</th>
            <th class="width-40">商品圖</th>
            <th class="width-30">建立時間</th>
          </tr>
        </thead>
        <tbody class="hover-orange select-checkbox-wrapper tbody-height-2" id="scrollDiv" onscroll="scrollInside()">
          {% for key,value in data["product_list"].items() %}
          <tr class="column sublayer">
            <!-- <td class="width-5 position-r"></td> -->
            <td class="width-30">
              {{value["product_name"]}}
            </td>
            <td class="width-40">
              <div class="table-img-wrapper preview" onmouseover="return imagePreview(this);">
                <img src="{{value['thumbnail']}}" class="table-img"/>
                <div class="preview-box">
                  <img src="#"/>
                </div>
              </div>
            </td>
            <td class="width-30">
              {{value["ct"]}}
            </td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </article>
  <div class="pagination-width-100 m-b-10">
    {{data["pagination"]}}
  </div>
</div>
{{header_footer_data["footer_html"]}}
<script type="text/javascript">
  $(function(){
    $(".search_product").click(function(){
      var search = $("#search_product").val();
      if ($.trim(search) != "") {
        top.location.href="{{data["hrs_view_product_detail_url"]}}{{data["token"]}}?service_sn={{data["service_sn"]}}&search="+search; 
      } else {
        alert("請輸入商品名稱!");
      }
    });
  });
  function imagePreview(element){
    thumbnail = $(element).position();
    thumbnail_w = $(element).outerWidth();
    thumbnail_h = $(element).outerHeight();
    thumbnail_url = $('.table-img', element).attr('src');
    $('.preview-box', element).css('top', '15px').css('right', '15px');
    $(".preview").mouseover(function(){
      $(".preview-box img", this).attr("src", thumbnail_url);								 
      $(".preview-box", this).show();
    }).mouseout(function(){
      $(".preview-box img", this).attr("src", "#");								 
      $(".preview-box", this).hide();
    });
  }
</script>
