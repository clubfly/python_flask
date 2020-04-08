/*************************************
 *--    Catalog Main Javascript    --*
 *************************************/
// AJAX Function
function send_tags_data(url, method, data, callback_function){
  $.ajax({
    url: url,
    method: method,
    dataType: 'json',
    contentType: 'application/json',
    data: JSON.stringify(data),
    error: function(data){
      alertMessage(data.statusText, 0, data.status);
    },
    success: function(data){
      if(data['code'] == '1'){
        console.log(data);
        callback_function(data);
      }else{
        alertMessage(data.statusText, 0, data.status);
      }
    }
  });
}
function send_ajax(action, data, callback_function){
  var url = api[action].domain + api[action].url;
  var method = api[action].method;
  send_tags_data(url, method, data, callback_function);
}
function save_item_status(){
  // switch 還原取消狀態
  $(".switch").each(function(){
    if($(this).attr('checkbox-status') == 1){
      if($('input', this).prop('checked') == false){
        $('input', this).prop('checked', true);
      } else {
        $('input', this).prop('checked', false);
      }
      $(".switch").attr('checkbox-status', 0);
      modalClose();
    }
  });
}
function save_items_status(data) {
  // 批次改變成 enable/disable 狀態
  // data = {
  //   'sysid': ['00000', '00001'],
  //   'status': 1
  // };
  $.each(data['sysid'], function(k, v){
    $('.switch-'+v).prop('checked', data['status']);
  });
  modalClose();
}
function save_items_delete() {
  // 刪除後重新整理頁面
  window.location.reload();
}

function accordionMenuDefault(element) {
  var menu_data = [
    {
      'menu-level': 1,
      'submenuList': []
    },
    {
      'menu-level': 2,
      'submenuList': []
    },
    {
      'menu-level': 3,
      'submenuList': []
    },
    {
      'menu-level': 4,
      'submenuList': []
    }
  ];
  var default_data = [
    {
      'submenuList': [
        {
          'openSubmenu': 0,
          'tabContentShow': 0,
          'parent': 0,
          'title': 'Default level one',
          'alink': ''
        },
      ]
    },
    {
      'submenuList': [
        {
          'openSubmenu': 0,
          'tabContentShow': 0,
          'parent': 1,
          'title': 'Default level two',
          'alink': ''
        },
      ]
    },
    {
      'submenuList': [
        {
          'openSubmenu': 0,
          'tabContentShow': 0,
          'parent': 1,
          'title': 'Default level three',
          'alink': ''
        },
      ]
    },
    {
      'submenuList': [
        {
          'openSubmenu': 0,
          'tabContentShow': 0,
          'parent': 1,
          'title': 'Default level four',
          'alink': ''
        },
      ]
    }
  ];
  var data;
  data = $.extend(true, [], menu_data, default_data);
  if(typeof(accordion_menu) != 'undefined' && typeof(accordion_menu[0]['submenuList']) == 'object' && accordion_menu[0]['submenuList'] != ''){
    data = $.extend(true, [], menu_data, accordion_menu);
  }
  for (let i = 1; i < data.length; i++) {
    drawMenuStruct(element, data[parseInt(i-1)], data[i]);
  }
}
function drawMenuStruct(element, menu_data1, menu_data2) {
  if($(element+' .accordion-menu').length == 0) {
    const menuUl = '<ul class="accordion-menu"></ul>';
    $(element).append(menuUl);
  }
  // 畫出 menu 架構
  var menuShow1 = 0;
  var menuShow2 = 0;
  var tabContent1 = 0;
  var tabContent2 = 0;
  $.each(menu_data1['submenuList'], function(k1, v1) {
    const submenuList = '<li class="menu-'+menu_data1['menu-level']+'-'+parseInt(k1+1)+'">'+
                          '<a href="#" tab-href="'+v1['alink']+'">'+
                            '<span>'+v1['title']+'</span>'+
                            '<i class="icon icon-right-w submenu-indicator"></i>'+
                          '</a>'+
                          '<ul class="submenu"></ul>'+
                        '</li>';
    if(menu_data1['menu-level'] == 1){
      $('.accordion-menu').append(submenuList);
      // 若 openSubmenu 等於 1 展開隱藏 submenu, 並將箭頭轉向
      if(v1['openSubmenu'] == 1 && menuShow1 == 0){
        $('.menu-'+menu_data1['menu-level']+'-'+parseInt(k1+1)).children('.submenu').show();
        $('.menu-'+menu_data1['menu-level']+'-'+parseInt(k1+1)).children('a').addClass('submenu-indicator-minus');
        menuShow1++;
      }
      // 若 tabContentShow 等於 1 顯示內容（僅顯示遇到的第一筆）
      if(v1['tabContentShow'] == 1 && tabContent1 == 0){
        $('.menu-'+menu_data1['menu-level']+'-'+parseInt(k1+1)).children('a').addClass('focus');
        $(v1['alink']).show();
        tabContent1++;
      }
    }
    $.each(menu_data2['submenuList'],function(k2, v2) {
      const submenuList = '<li class="menu-'+menu_data2['menu-level']+'-'+parseInt(k2+1)+'">'+
                            '<a href="#" tab-href="'+v2['alink']+'">'+
                              '<span>'+v2['title']+'</span>'+
                              '<i class="icon icon-right-w submenu-indicator"></i>'+
                            '</a>'+
                            '<ul class="submenu"></ul>'+
                          '</li>';                
      if(menu_data2['menu-level'] == parseInt(menu_data1['menu-level']+1) && parseInt(k1+1) == v2['parent']){
        $('.menu-'+menu_data1['menu-level']+'-'+v2['parent']).children('.submenu').append(submenuList);
        // 若有 children 顯示箭頭
        if($('.menu-'+menu_data1['menu-level']+'-'+v2['parent']).children('.submenu').children('li').length > 0){
          $('.menu-'+menu_data1['menu-level']+'-'+v2['parent']).children('a').children('.submenu-indicator').show();
        }
        // 若 openSubmenu 等於 1 展開隱藏 submenu, 並將箭頭轉向（僅展開遇到的第一筆）
        if(v2['openSubmenu'] == 1 && menuShow2 == 0){
          $('.menu-'+menu_data2['menu-level']+'-'+parseInt(k2+1)).children('.submenu').show();
          $('.menu-'+menu_data2['menu-level']+'-'+parseInt(k2+1)).children('a').addClass('submenu-indicator-minus');
          menuShow2++;
        }
        // 若 tabContentShow 等於 1 顯示內容（僅顯示遇到的第一筆）
        if(v2['tabContentShow'] == 1 && tabContent2 == 0){
          $('.menu-'+menu_data2['menu-level']+'-'+parseInt(k2+1)).children('a').addClass('tab-active');
          $(v2['alink']).show();
          tabContent2++;
        }
      }
    });
  });
}
function openSubmenu(e, element) {
  // 開啟 submenu 的 defaults
  var defaults = {
    speed: 300,
    showDelay: 0,
    hideDelay: 0,
    singleOpen: true,
    clickEffect: true
  };
  e.stopPropagation();
  e.preventDefault();
  if ($(element).children('.submenu').children('li').length > 0) {
    if ($(element).children('.submenu').css('display') == 'none') {
      $(element).children('.submenu').delay(defaults.showDelay).slideDown(defaults.speed);
      $(element).children('.submenu').siblings('a').addClass('submenu-indicator-minus');
      if (defaults.singleOpen) {
        $(element).siblings().children('.submenu').delay(defaults.hideDelay).slideUp(defaults.speed);
        $(element).siblings().children('.submenu').siblings('a').removeClass('submenu-indicator-minus');
      }
      return false;
    } else {
      $(element).children('.submenu').delay(defaults.hideDelay).slideUp(defaults.speed);
    }
    if ($(element).children('.submenu').siblings('a').hasClass('submenu-indicator-minus')) {
      $(element).children('.submenu').siblings('a').removeClass('submenu-indicator-minus');
    }
  }else{
    $('li a').removeClass('tab-active').removeClass('focus');
    $(element).children('a').addClass('focus');
    $(element).children('a').addClass('tab-active');
    // window.location.href = $(element).children("a").attr("tab-href");
    tabContentShow = $(element).children("a").attr("tab-href");
    $('.tab-content').hide();
    $(tabContentShow).show();
  }
}
function selectCheckboxAll(){
  $('.select-checkbox').prop('checked', false);
  if($('#select-checkbox-all').is(':checked')){
    $('.select-checkbox').prop('checked', true);
  }
}
function selectCheckboxAllStatus(){
  // 1.select-checkbox全都選, select-checkbox-all為indeterminate false, checked true
  // 2.select-checkbox有選但沒全選, select-checkbox-all為indeterminate true, checked false
  // 3.select-checkbox全都沒有選, select-checkbox-all為indeterminate false, checked false
  var check_select = 0;
  var table_size = $('tbody tr').size();
  $('.select-checkbox').each(function(){
    if($(this).is(':checked')){
      check_select++;
    }
  });
  if(check_select === table_size){
    $('#select-checkbox-all').prop('indeterminate', false);
    $('#select-checkbox-all').prop('checked', true);
  }
  if(check_select !== 0 && check_select !== table_size){
    $('#select-checkbox-all').prop('indeterminate', true);
    $('#select-checkbox-all').prop('checked', false);
  }
  if(check_select === 0){
    $('#select-checkbox-all').prop('indeterminate', false);
    $('#select-checkbox-all').prop('checked', false);
  }
}
function toolbarButtonStatus(){
  var check_select = 0;
  $('.select-checkbox').each(function(){
    if($(this).is(':checked')){
      check_select++;
    }
  });
  $('.toolbar-wrapper').addClass('hidden');
  $('.toolbar-wrapper button').prop("disabled", true);
  if(check_select > 0){
    $('.toolbar-wrapper').removeClass('hidden');
    $('.toolbar-wrapper button').prop("disabled", false);
  }
}
function dataValuePushArray(sysid, status){
  var dataValue = {
    'sysid': sysid,
    'status': status
  };
  return dataValue;
}
function alertMessage(message, status, ajaxStatus){
  $('.alert .message').html('');
  if(status){
    $('.alert .message').html(message);
    $('.alert').removeClass('alert-danger').removeClass('alert-warning').addClass('alert-success');
    $('.modal').removeClass('show').addClass('hidden');
    $('.modal-backdrop').remove();
  }else{
    $('.alert .message').html(ajaxStatus + ' ' + message);
    $('.alert').removeClass('alert-success').removeClass('alert-warning').addClass('alert-danger');
  }
  $('.alert').fadeIn();
  setTimeout(function(){
    $('.alert').fadeOut();
  }, 3000);
};
function render_input_status(input, status, message){
  input.addClass('is-invalid');
  input.next().next().html(message);
  input.next().next().show();
  if(status){
    input.removeClass('is-invalid');
    input.next().next().html('');
    input.next().next().hide();
  }
}
function tabContentBtn(element) {
  var tabID = $(element).attr('tab-href');
  $('.tab-content').hide();
  $(tabID).show();
}
function check_value(check_form) {
  var num = 0;
  $('.'+check_form).each(function() {
    $('.required', this).each(function(){
      if(rule_loader($(this).val(), '', 'required')) {
        render_input_status($(this), true, '');
      } else {
        render_input_status($(this), false, message.required);
        num++;
      };
    });
    if(num == 0){
      $('.equalTo', this).each(function(){
        if(rule_loader($('.new_password').val(), $('.confirm_new_password').val(), 'equalTo')) {
          render_input_status($(this), true, '');
        } else {
          render_input_status($(this), false, message.equalTo);
        };
      });
    }
  });
}
// 事件
$(function(){
  accordionMenuDefault('aside');
  $('.accordion-menu').children('li').click(function(e){
    openSubmenu(e, this);
  });
  $('.submenu').children('li').click(function(e){
    openSubmenu(e, this);
  });
  $('.switch').click(function() {
    $(this).attr('checkbox-status', '1');
    var model_data = {
      'modal-element': '#modalCenterText',
      'modal-title': 'Please confirm again.',
      'modal-body': 'Are you sure you want to『enable』the item?'
    };
    modalShow(model_data);
    if($('input', this).prop('checked') == true){
      var model_data = {
        'modal-element': '#modalCenterText',
        'modal-title': 'Please confirm again.',
        'modal-body': 'Are you sure you want to『disable』the item?'
      };
      modalShow(model_data);
    }
  });
  $('.enable').click(function(){
    var model_data = {
      'modal-element': '#modalCenterText',
      'modal-title': 'Please confirm again.',
      'modal-body': 'Are you sure you want to『enable』these items?'
    };
    modalShow(model_data);
  });
  $('.disable').click(function(){
    var model_data = {
      'modal-element': '#modalCenterText',
      'modal-title': 'Please confirm again.',
      'modal-body': 'Are you sure you want to『disable』these items?'
    };
    modalShow(model_data);
  });
  $('.delete').click(function(){
    var model_data = {
      'modal-element': '#modalCenterText',
      'modal-title': 'Please confirm again.',
      'modal-body': 'Are you sure you want to『delete』these items?'
    };
    modalShow(model_data);
  });
  $('.modal .close').click(function(){
    modalClose();
    save_item_status();
  });
  $('.modal .cancel').click(function(){
    modalClose();
    save_item_status();
  });
  $('.save').click(function(){
    var action = api_action;
    var data = api_data;
    send_ajax(action, data, save_items_status);
    console.log(data);
  });
  $('#select-checkbox-all').click(function(){
    selectCheckboxAll();
    toolbarButtonStatus();
  });
  $('.select-checkbox').click(function(){
    selectCheckboxAllStatus();
    toolbarButtonStatus();
  });
  $('.tab-btn').click(function(){
    tabContentBtn(this);
  });
  $('.save-change-pwd').click(function(){
    // 1. 檢查'當前密碼''新密碼''確認密碼'不為空值
    // 2. 檢查'當前密碼'與'新密碼'為不同
    // 2. 檢查'新密碼'與'確認密碼'為相同
    // 3. 傳遞 user_id, current_password, new_password, confirm_new_password
    if(check_value('change-pwd-form')){
      $(this).parents().prev().submit();
    }
  });
});