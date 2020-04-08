/**************************************************************************************
 *    Accordion Menu
 * 1. menu level 最多到四層, 超過不顯示
 * 2. 畫面呈現方式會依照 accordion menu 陣列內物件的順序
 * 3. openSubmenu 設置為 1, 若有 submenu 則展開, 同一層僅顯示第一筆
 * 4. parent 第一層預設為 0, 第二層之後需設置 submenu 要掛載的 parent, 若無該 parent 將不顯示
 * 5. title 字元超過則顯示..., 依照RWD做調整
 * 6. alink 設置連結若該元素還有 child, 點擊時只會展開 submenu 不會前往連結處
 **************************************************************************************/
var accordion_menu = [
  {
    'submenuList': [
      {
        'openSubmenu': 1,
        'tabContentShow': 0,
        'parent': 0,
        'title': menu_service_setting,
        'alink': '#'
      }
    ]
  },
  {
    'submenuList': [
      {
        'openSubmenu': 0,
        'tabContentShow': 1,
        'parent': 1,
        'title': menu_system_announcement,
        'alink': '#tab-content-13',
        'addClass' : 'self_test_close'
      },
      {
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 1,
        'title': menu_company,
        'alink': '#tab-content-2',
        'addClass' : 'self_test_close'
      },
      {
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 1,
        'title': menu_service_list,
        'alink': '#tab-content-3',
        'addClass' : 'self_test_close'
      },
      {
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 1,
        'title': menu_branch,
        'alink': '#tab-content-4',
        'addClass' : 'self_test_close'
      }
    ]
  }
];
$(function(){
  var event_obj = {
                   "click" : [{
                              "selector" : ".add_company_branch",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".company_branch",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".branch_account_manage",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".add_company_branch_account",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".account_password",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".company_product",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".add_company_product",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".edit_product",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".company_product_image",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".save_status",
                              "function" : multiple_status_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".save-change-self-pwd",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".change-self-pwd_form"
                              },
                              {
                              "selector" : ".save_company_profile",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".company_profile-form"
                              },
                              {
                              "selector" : ".save_company_branch",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".add_company_branch-form"
                              },
                              {
                              "selector" : ".save_company_branch_account",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".add_company_branch_account-form"
                              },
                              {
                              "selector" : ".save-change-pwd",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".change-pwd_form"
                              },
                              {
                              "selector" : ".save_company_product",
                              "function" : check_sku_data_loader,
                              "obj_selector" : ".add_company_product-form"
                              },
                              {
                              "selector" : ".upload-images",
                              "function" : ajax_file_data_loader,
                              "obj_selector" : ".add_company_product_image-form"
                              },
                              {
                              "selector" : ".save_product_image",
                              "function" : screenshot_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".upload-RT",
                              "function" : image_recognition_data_loader,
                              "obj_selector" : ".self_test_image-form"
                              },
                              {
                              "selector" : ".add_system_announcement",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".back_system_announcement",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".save_account_status",
                              "function" : single_status_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".modal_search_btn",
                              "function" : modal_search_show_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".search_products",
                              "function" : search_data_loader,
                              "obj_selector" : "#search_product_form"
                              },
                              {
                              "selector" : ".products_csv_upload",
                              "function" : products_csv_upload_data_loader,
                              "obj_selector" : "#products_csv_upload_form"
                              },
                              {
                              "selector" : ".images_csv_upload",
                              "function" : images_csv_upload_data_loader,
                              "obj_selector" : "#images_csv_upload_form"
                              },
                              {
                              "selector" : ".products_csv_download",
                              "function" : products_csv_download_data_loader,
                              "obj_selector" : "#products_csv_download_form"
                              },
                              {
                              "selector" : ".add_batch_company_product",
                              "function" : sn_data_loader,
                              "obj_selector": ""
                              },
                              {
                              "selector" : ".upload_product_log",
                              "function" : sn_data_loader,
                              "obj_selector": ""
                              },
                              {
                              "selector" : ".upload_image_log",
                              "function" : sn_data_loader,
                              "obj_selector": ""
                              }],
                    "keyup" : [{
                                "selector": ".jump-page-input",
                                "function": change_page_sn_data_loader,
                                "obj_selector": ""
                               }]
                  };
  $.each(event_obj,function(k1,v1){
    $.each(v1,function(k2,v2){
      $(document).on(k1,v2["selector"],function(){
        var obj = $(this);
        if (v2["obj_selector"] != "") {
          obj = $(v2["obj_selector"]);
        }
        v2["function"](obj);
      });
    });
  });
  $(document).on("click",".self_test",function(){
    alertMessage(pkl_update_msg,1,"",1500);
    $(this).prop("disabled",true);
    pkl_update_data_loader($(this));
  });
  $(document).on("click",".self_test_close",function(){
    webcam_controll_loader(1);
  });
  $(document).on("click",".deploy_pkl",function(){
    $(this).prop("disabled",true);
    pkl_deploy_data_loader($(this)); 
  });
});
function search_data_loader(obj){
  var data_sn = obj.attr("data_sn");
  page_sn = 1
  var tab = obj.attr("tab_sn");
  var search="";
  var product_sn = $("#product_sn").val();
  var product_name = $("#product_name").val();
  var abbreviation = $("#abbreviation").val();
  var barcode = $("#barcode").val();
  var ct_start_date = $("#ct_start_date").val();
  var ct_end_date = $("#ct_end_date").val();
  var ut_start_date = $("#ut_start_date").val();
  var ut_end_date = $("#ut_end_date").val();
  var image_cnt = $("#image_cnt").val();
  var enabled = $("#enabled").val();
  search = "product_sn="+product_sn+"&product_name="+product_name+
           "&abbreviation="+abbreviation+"&barcode="+barcode+
           "&ct_start_date="+ct_start_date+"&ct_end_date="+ct_end_date+
           "&ut_start_date="+ut_start_date+"&ut_end_date="+ut_end_date+
           "&image_cnt="+image_cnt+"&enabled="+enabled
  console.log(search); 
  var url = obj.attr("ajax_url") + "?"+"data_sn="+data_sn+"&pages="+page_sn+"&"+search;
  console.log(url);
  var ajax_obj = {
                  "url" : url,
                  "method" : "GET",
                  "data" : {}
                 };
  rs = check_session();
  if (rs == 1){
    get_tab_ajax_data(tab,ajax_obj);
  }
}
function image_recognition_data_loader(obj){
  var tab = obj.attr("tab_sn");
  var ajax_obj = {
                   "url" : obj.attr("action"),
                   "method" : "POST",
                   "data" : new FormData(obj[0])
                 }
  rs = check_session();
  if (rs == 1){
    if ($(".image_recongintion").val() != "") {
      screenshot_loading_open();
      set_ajax_file_data_to_api(tab,ajax_obj,0,1);
    }
  }
}
function webcam_controll_loader(display){
  // close = 1 , open = 0
  var webcam_data = {
                     'display': display,
                     'screenshotButton': '.screenshot-button-RT',
                     'img': '#source-img-RT',
                     'video': '#videostream-RT video',
                     'checkEnabled': 0
                    };
  webcam_data_loader(webcam_data);
}
function pkl_update_data_loader(obj){
  var tab = obj.attr("tab_sn");
  var data_sn = obj.attr("data_sn");
  var ajax_obj = {          
                   "url" : obj.attr("ajax_url"),
                   "method" : "POST",
                   "data" : {
                             "data_sn" : obj.attr("data_sn")
                            }
                 };
  rs = check_session();
  if (rs == 1){
    rs2 = set_pkl_to_test_server(tab,ajax_obj);
    if (rs2 == 1) {
      webcam_controll_loader(0);
      var api_url = self_test_url + obj.attr("data_sn");
      $(".screenshot-button-RT").attr("api_url",api_url);
      $(".self_test_image-form").attr("action",api_url);
      $(".self_test").each(function(k,v){
        $(this).prop("disabled",false);
      });
      reRecognitionTestCamera();
      reRecognitionTestUpload();
    }
  }
}
function pkl_deploy_data_loader(obj){
  var tab = obj.attr("tab_sn");
  var data_sn = obj.attr("data_sn");
  var ajax_obj = {
                   "url" : obj.attr("ajax_url"),
                   "method" : "POST",
                   "data" : {
                             "data_sn" : obj.attr("data_sn")
                            }
                 };
  rs = check_session();
  if (rs == 1){
    rs2 = set_pkl_to_test_server(tab,ajax_obj);
    if (rs2 == 1) {
      $(".deploy_pkl").each(function(k,v){
        $(this).prop("disabled",false);
      });
      alertMessage("deployment is done !",1,"",1500);
    }
  }
}
function set_pkl_to_test_server(tab_sn,ajax_obj){
  return_value = 0;
  $.ajax({
    method : ajax_obj["method"],
    url : ajax_obj["url"],
    async : false,
    cache: false,
    data : ajax_obj["data"]
  }).done(function(msg) {
    console.log(msg);
    if (parseInt(msg.code) == 0){
      // alert(msg.message);
    } else {
      return_value = 1;
      if (parseInt(tab_sn) > 0){
        $(".tab-content").hide();
        $("#tab-content-"+tab_sn).show();
      }
    }
  });
  return return_value;
}
function screenshot_data_loader(obj){
  var tab = obj.attr("tab_sn");
  var images = [] 
  $(".screenshot_pic").each(function(key,val){
    images.push($("img",this).attr("src")); 
  });
  var ajax_obj = {
                   "url" : obj.attr("ajax_url"),
                   "method" : "POST",
                   "data" : {
                             "data_sn" : obj.attr("data_sn"),
                             "thumbnail" : images
                            }
                 }
  rs = check_session();
  if (rs == 1){
    set_ajax_data_to_api(tab,ajax_obj);
    handleStop();
  }
}
function single_status_data_loader(obj){
  loadingOpen();
  var tab = obj.attr("tab_sn");
  var ajax_obj = { 
                   "url" : obj.attr("ajax_url"),
                   "method" : "POST",
                   "data" : {
                             "data_sn" : obj.attr("data_sn"),
                             "page_sn" : obj.attr("page_sn"),
                             "enabled" : obj.attr("status_sn")
                            }
                 }
  rs = check_session();
  if (rs == 1){
    set_status_data_to_api(tab,ajax_obj);
  }
}
function multiple_status_data_loader(obj){
  loadingOpen();
  var data_sn = [];
  $(".data_status").each(function(key,value){
    if ($(this).prop('checked') == true) {
      data_sn.push($(this).attr("sysid"));
    }
  });
  var tab = obj.attr("tab_sn");
  var ajax_obj = {
                   "url" : obj.attr("ajax_url"),
                   "method" : "POST",
                   "data" : {
                             "data_sn" : data_sn,
                             "page_sn" : obj.attr("page_sn"),
                             "product_sn" : obj.attr("product_sn"),
                             "enabled" : obj.attr("status_sn")
                            }
                 }
  rs = check_session();
  if (rs == 1){
    set_status_data_to_api(tab,ajax_obj);
  }
}
function set_status_data_to_api(tab_sn,ajax_obj){
  $.ajax({
    method : ajax_obj["method"],
    url : ajax_obj["url"],
    data : ajax_obj["data"]
  }).done(function(msg) {
    if (parseInt(msg.code) == 1){
      alertMessage(msg.message,1,"",1500);
      set_switch_tab(tab_sn,msg.data);
    } else {
      loadingClose();
    }
  });
}
function check_session(){
  return_value = 0;
  $.ajax({
    method : "GET",
    url : session_api,
    async : false,
    data : {}
  }).done(function(msg) {
    if (parseInt(msg.code) == 0){
      alert(msg.message);
      top.location.href=logout_api;
    } else {
      return_value = 1;
    }
  });
  return return_value;
}
function ajax_data_loader(obj){
  var tab = obj.attr("tab_sn");
  var ajax_obj = {
                   "url" : obj.attr("action"),
                   "method" : "POST",
                   "data" : obj.serialize()
                 }
  rs = check_session();
  if (rs == 1){
    set_ajax_data_to_api(tab,ajax_obj);
  }
}
function set_ajax_data_to_api(tab_sn,ajax_obj){
  $.ajax({
    method : ajax_obj["method"],
    url : ajax_obj["url"],
    data : ajax_obj["data"]
  }).done(function(msg) {
    if (parseInt(msg.code) == 1){
      alertMessage(msg.message,1,"",1500);
      if (parseInt(tab_sn) > 0) {
        set_switch_tab(tab_sn,msg.data);
      }
    } else {
      $.each(msg.data,function(key,value){
        color = 1
        if (value != "") {
          color = 0
        }
        render_input_status($("#"+key),color,value);
      });
    }
  });
}
function sn_data_loader(obj) {
  var data_sn = obj.attr("data_sn");
  var page_sn = obj.attr("page_sn");
  var search = obj.attr("search")
  if (typeof(page_sn) == "undefined"){
    page_sn = 1
  } else {
    if (parseInt(page_sn).toString() == "NaN"){
      page_sn = 1
    }
  }
  if (typeof(search) == "undefined"){
    search = "";
  }
  var tab = obj.attr("tab_sn");
  var url = obj.attr("ajax_url") + "?"+"data_sn="+data_sn+"&pages="+page_sn+"&"+search;
  var ajax_obj = {
                  "url" : url,
                  "method" : "GET",
                  "data" : {}
                 };
  rs = check_session();
  if (rs == 1){
    get_tab_ajax_data(tab,ajax_obj);
  }
}
function get_tab_ajax_data(tab_sn,ajax_obj){
  $.ajax({
    method : ajax_obj["method"],
    url : ajax_obj["url"],
    data : ajax_obj["data"]
  }).done(function(msg) {
    if (parseInt(tab_sn) > 0) {
      set_switch_tab(tab_sn,msg);
      modalClose();
    }
  });
}
function set_switch_tab(tab_sn,msg){
  $(".tab-content").hide();
  $("#tab-content-"+tab_sn).show();
  $("#tab-content-"+tab_sn).html(msg);
  scrollToAnchor();
  loadingClose();
}
function ajax_file_data_loader(obj){
  var tab = obj.attr("tab_sn");
  var ajax_obj = {
                   "url" : obj.attr("action"),
                   "method" : "POST",
                   "data" : new FormData(obj[0])
                 };
  rs = check_session();
  if (rs == 1){
    set_ajax_file_data_to_api(tab,ajax_obj,1,0);
  }
}
function set_ajax_file_data_to_api(tab_sn,ajax_obj,msg_show,recognition){
  $.ajax({
    method : ajax_obj["method"],
    url : ajax_obj["url"],
    data : ajax_obj["data"],
    processData : false,
    contentType : false,
    cache : false
  }).done(function(msg) {
    modalSecondHide();
    screenshot_loading_close();
    if (parseInt(msg.code) == 1){
      if (msg_show == 1){
        alertMessage(msg.message,1,"",1500);
      }
      if (parseInt(tab_sn) > 0) {
        set_switch_tab(tab_sn,msg.data);
      }
      $("#products_csv").val("");
      $("#images_csv").val("");
      $("#images_zip").val("");
      $(".custom-file-label").html(unselected_file);
      if (recognition == 1) {
        resultRecognitionTestDataForUpload(msg['data']['checkout']);
      }
    } else {
      $.each(msg.data,function(key,value){
        color = 1 
        if (value != "") {
          color = 0
        }
        render_input_status($("#"+key),color,value);
      });
    }
  });
}
function change_page_sn_data_loader(obj){
  $(".jump-page-btn").prop("disabled", true);
  if(check_number(obj.val())){
    $(".jump-page-btn").attr("page_sn", obj.val());
    $(".jump-page-btn").prop("disabled", false);
  }
}
function check_number(str){
  regex = /[^\d]/g;
  if(str.match(regex) || str == ""){
    return false;
  }
  return true;
}
function check_sku_data_loader(obj){
  var sku = $('#sku_error').val();
  var service_sn = $("#service_sn").val()
  get_sku_ajax_data(sku,service_sn,obj);
}
function get_sku_ajax_data(sku,service_sn,obj){
  var url = check_sku_url + sku + "?service_sn="+service_sn;
  $.ajax({
    method : 'GET',
    url : url,
    cache : false
  }).done(function(msg) {
    if (parseInt(msg.code) == 1){
      call_data_send();
    } else {
      modal_second_show_data_loader({
        'selector': '#common_modal_second',
        'modal-body': sku_dialog,
        'confirm_function': call_data_send
      });
    }
  });
}
function call_data_send(){
  var obj = $(".add_company_product-form");
  ajax_file_data_loader(obj);
}
function modal_search_show_data_loader(obj){
  var model_data = {
    'display': 1,
    'modal-element': '#modal_search',
    'modal-title': search_rule_title,
    'modal-body': ''
  };
  $("#search_product_form").attr("data_sn",obj.attr("data_sn"));
  $("#search_product_form").attr("tab_sn",obj.attr("tab_sn"));
  modal_data_loader(model_data);
}
function products_csv_upload_data_loader(obj){
  var check_input = ['#products_csv'];
  if(required_check_value(check_input)){
    var ajax_obj = {
                    "url" : obj.attr("action"),
                    "method" : "POST",
                    "data" : new FormData(obj[0])
                   };
    set_ajax_file_data_to_api(0,ajax_obj,1,0);
  }
}
function images_csv_upload_data_loader(obj){
  var check_input = ['#images_csv', '#images_zip'];
  if(required_check_value(check_input)){
    var ajax_obj = {
                    "url" : obj.attr("action"),
                    "method" : "POST",
                    "data" : new FormData(obj[0])
                   };
    set_ajax_file_data_to_api(0,ajax_obj,1,0);
  }
}
function products_csv_download_data_loader(obj){
  if(check_input_value()){
    var ajax_obj = {
                    "url" : obj.attr("action"),
                    "method" : "POST",
                    "data" : new FormData(obj[0])
                   };
    location.href=obj.attr("action")+"?"+obj.serialize();
  };
}
