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
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 0,
        'title': menu_customer,
        'alink': '#'
      },
      {
        'openSubmenu': 1,
        'tabContentShow': 0,
        'parent': 0,
        'title': menu_system,
        'alink': '#'
      },
    ]
  },
  {
    'submenuList': [
      {
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 1,
        'title': menu_customer_service,
        'alink': '#tab-content-2'
      },
      {
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 2,
        'title': menu_service_list,
        'alink': '#tab-content-3'
      },
      {
        'openSubmenu': 1,
        'tabContentShow': 1,
        'parent': 2,
        'title': menu_system_announcement,
        'alink': '#tab-content-15'
      }
    ]
  }
];
$(function(){
  var event_obj = {
                   "click" : [{
                              "selector" : ".company_profile",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".company_service",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".company_account",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".company_license",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".add_company_service",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".add_company_account",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".account_password",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".bind_service_account",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".save-change-self-pwd",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".change-self-pwd_form"
                              },
                              {
                              "selector" : ".save_company",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".add_company-form"
                              },
                              {
                              "selector" : ".save_company_profile",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".company_profile-form"
                              },
                              {
                              "selector" : ".save_company_service",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".add_company_service-form"
                              },
                              {
                              "selector" : ".save_company_account",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".add_company_account-form"
                              },
                              {
                              "selector" : ".save-change-pwd",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".change-pwd_form"
                              },
                              {
                              "selector" : ".save-bind-service",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".bind_service-form"
                              },
                              {
                              "selector" : ".company_license_detail",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".company_license_request",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".company_license_request_detail",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".add_company_license_request",
                              "function" : sn_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".save_company_license_request",
                              "function" : ajax_data_loader,
                              "obj_selector" : ".upd_company_license_request-form"
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
                              "selector" : ".enabled_announcement",
                              "function" : sn_status_data_loader,
                              "obj_selector" : ""
                              },
                              {
                              "selector" : ".disabled_announcement",
                              "function" : sn_status_data_loader,
                              "obj_selector" : ""
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
});
function check_session(){
  var return_value = 0;
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
  if (typeof(page_sn) == "undefined"){
    page_sn = 1
  } else {
    if (parseInt(page_sn).toString() == "NaN"){
      page_sn = 1
    }
  }
  var tab = obj.attr("tab_sn");
  var url = obj.attr("ajax_url") + "?data_sn="+data_sn+"&pages="+page_sn;
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
      set_switch_tab(tab_sn,msg)
    }
  });
}
function set_switch_tab(tab_sn,msg){
  $(".tab-content").hide();
  $("#tab-content-"+tab_sn).show();
  $("#tab-content-"+tab_sn).html(msg);
  loadingClose();
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
function sn_status_data_loader(obj){
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
