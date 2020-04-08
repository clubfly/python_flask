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
function send_tags_data(url, method, data, callback_function){
  $.ajax({
    url: url,
    method: method,
    dataType: 'json',
    contentType: 'application/json',
    data: JSON.stringify(data),
    error: function(data){
      alertMessage(data.statusText, 0, data.status, '');
    },
    success: function(data){
      if(data['code'] == '1'){
        console.log(data);
        callback_function(data);
      }else{
        alertMessage(data.statusText, 0, data.status, '');
      }
    }
  });
}
function send_ajax(action, data, callback_function){
  var url = api[action].domain + api[action].url;
  var method = api[action].method;
  send_tags_data(url, method, data, callback_function);
}

function restoreSwitchStatus(){
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
function switchStatus(data) {
  // 批次改變成 enable/disable 狀態 OK
  $.each(data['sysid'], function(k, v){
    $('.switch-'+v).prop('checked', data['status']);
  });
  modalClose();
}
function reload() {
  // 刪除後重新整理頁面
  window.location.reload();
}

function accordionMenuDefault(accordion_menu) {
  // accordion menu 資料合併 OK
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
    drawMenuStruct(data[parseInt(i-1)], data[i]);
  }
}
function drawMenuStruct(menu_data1, menu_data2) {
  // accordion menu 繪製 OK
  if($('.accordion-menu-wrapper .accordion-menu').length == 0) {
    const menuUl = '<ul class="accordion-menu"></ul>';
    $('.accordion-menu-wrapper').append(menuUl);
  }
  // 畫出 menu 架構
  var menuShow1 = 0;
  var menuShow2 = 0;
  var tabContent1 = 0;
  var tabContent2 = 0;
  var add_class = '';
  $.each(menu_data1['submenuList'], function(k1, v1) {
    if(v1['addClass'] != undefined) {
      add_class = v1['addClass'];
    }
    const submenuList = '<li class="menu-'+menu_data1['menu-level']+'-'+parseInt(k1+1)+' '+add_class+'">'+
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
      if(v2['addClass'] != undefined) {
        add_class = v2['addClass'];
      }
      const submenuList = '<li class="menu-'+menu_data2['menu-level']+'-'+parseInt(k2+1)+' '+add_class+'">'+
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
    singleOpen: true
  };
  e.stopPropagation();
  e.preventDefault();

  if ($(element).children('.submenu').children('li').length > 0) {
    if ($(element).children('.submenu').css('display') == 'none') {
      $(element).children('.submenu').slideDown(defaults.speed);
      $(element).children('.submenu').siblings('a').addClass('submenu-indicator-minus');
      if (defaults.singleOpen) {
        $(element).siblings().children('.submenu').slideUp(defaults.speed);
        $(element).siblings().children('.submenu').siblings('a').removeClass('submenu-indicator-minus');
      }
      return false;
    } else {
      $(element).children('.submenu').slideUp(defaults.speed);
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

function selectCheckboxAll(data){
  $(data['wrapper']+' '+data['seclct_picker']).prop('checked', false);
  if($(data['select_all_picker']).is(':checked')){
    $(data['wrapper']+' '+data['seclct_picker']).prop('checked', true);
  }
}
function selectCheckboxAllStatus(data){
  // 1.select-checkbox全都選, select-checkbox-all為indeterminate false, checked true
  // 2.select-checkbox有選但沒全選, select-checkbox-all為indeterminate true, checked false
  // 3.select-checkbox全都沒有選, select-checkbox-all為indeterminate false, checked false
  var check_select = 0;
  var table_size = data['max'];
  $(data['wrapper']+' '+data['seclct_picker']).each(function(){
    if($(this).is(':checked')){
      check_select++;
    }
  });
  if(check_select == table_size){
    $(data['select_all_picker']).prop('indeterminate', false);
    $(data['select_all_picker']).prop('checked', true);
  }
  if(check_select != 0 && check_select != table_size){
    $(data['select_all_picker']).prop('indeterminate', true);
    $(data['select_all_picker']).prop('checked', false);
  }
  if(check_select == 0){
    $(data['select_all_picker']).prop('indeterminate', false);
    $(data['select_all_picker']).prop('checked', false);
  }
}
function toolbarButtonStatus(data){
  var check_select = 0;
  $(data['wrapper']+' '+data['seclct_picker']).each(function(){
    if($(this).is(':checked')){
      check_select++;
    }
  });
  $('.toolbar-hide').addClass('hidden');
  $('.toolbar-wrapper button').prop("disabled", true);
  if(check_select > 0){
    $('.toolbar-hide').removeClass('hidden');
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

function modalShow(model_data){
  // modal 純文字 OK
  title_msg = "error";
  body_msg = "Please confirm your value to modalShow.";
  if(model_data != undefined){
    title_msg = model_data['modal-title'];
    body_msg = model_data['modal-body'];
  }
  $(model_data['modal-element']+' .modal-title').text(title_msg);
  $(model_data['modal-element']+' .modal-body').children('span').text(body_msg);

  modalTemplate = '<div class="modal-backdrop fade show"></div>';
  if($(model_data['modal-element']).length > 0){
    $('.modal-backdrop').remove();
    $('body').addClass('modal-open').append(modalTemplate);
    $(model_data['modal-element']).addClass('show').slideDown(300);
  }
}
function modalSopImgShow(model_data){
  // modal sop img
  title_msg = "error";
  body_msg = "Please confirm your value to modalShow.";
  if(model_data != undefined){
    title_msg = model_data['modal-title'];
  }
  $(model_data['modal-element']+' .modal-title').text(title_msg);
  $(model_data['modal-element']+' .modal-body').html('<img src="'+vcms_config_data['sop_img_data'][model_data['language']][model_data['sop-img']]+'" class="width-100"/>');

  modalTemplate = '<div class="modal-backdrop fade show"></div>';
  if($(model_data['modal-element']).length > 0){
    $('.modal-backdrop').remove();
    $('body').addClass('modal-open').append(modalTemplate);
    $(model_data['modal-element']).addClass('show').slideDown(300);
  }
}
function modalClose(){
  $('.modal').removeClass('show').slideUp(300);
  $('.modal-backdrop').remove();
  $('body').removeClass('modal-open');
}
var fadeOutAlert;
function alertMessage(data_message, data_status, data_ajaxStatus, data_seconds){
  // alertMessage 公用訊息顯示在頁面中上位置, status = false (0) 為紅色, status = true (1) 為綠色。 OK
  const defaults = {
    class_name: ['alert-danger', 'alert-success', 'alert-warning'],
    message: 'No message.',
    status: 2,
  };
  // 清除 alert 的 class (控制顏色)
  $.each(defaults['class_name'], function(k, v){
    $('.alert').removeClass(v);
  });
  // 清除 alert message 的內容
  $('.alert .message').text('');
  // 檢查後端 data 是否有 message 的值, 若沒有跑預設顯示'No message.'
  if(data_message != '' && data_message != undefined){
    defaults.message = data_message;
  }
  // 檢查後端 data 是否有 status 的值, 若沒有跑預設顯示'alert-warning'的狀態顏色
  if(defaults['class_name'][data_status] != '' && defaults['class_name'][data_status] != undefined){
    defaults.status = data_status;
  }
  // 顯示對應的內容與顯示的狀態顏色
  $('.alert .message').text(data_ajaxStatus + ' ' + defaults.message);
  $('.alert').addClass(defaults['class_name'][defaults.status]);
  // data_status 為 true (1) 關閉 modal
  if(data_status) {
    modalClose();
  }
  // alert 顯示
  $('.alert').fadeIn();
  // 檢查後端 data 是否有 seconds 的值, 若沒有值則不會自動隱藏 alert
  if(data_seconds != '' && data_seconds != undefined){
    clearTimeout(fadeOutAlert);
    fadeOutAlert = setTimeout(function(){
      $('.alert').fadeOut();
    }, data_seconds);
  }
};
function alertMessageClose() {
  $('.alert').fadeOut();
}
function inputStatus(input, status){
  // input 外框顏色顯示, status = false (0) 為紅色, status = true (1) 為綠色。 OK
  $(input).removeClass('is-valid');
  $(input).addClass('is-invalid');
  if(status){
    $(input).removeClass('is-invalid');
    $(input).addClass('is-valid');
  }
}
function inputMessage(element, status, message){
  // error message 顯示, status = false (0) 為隱藏, status = true (1) 為顯示。OK
  $(element).text('');
  $(element).hide();
  if(status){
    $(element).text(message);
    $(element).show();
  }
}
function inputStatusClear(input){
  $(input).removeClass('is-valid');
  $(input).removeClass('is-invalid');
}
function tabContentBtn(element) {
  var tabID = $(element).attr('tab-href');
  $('.tab-content').hide();
  $(tabID).show();
}
function clearReadFile(data) {
  $(data['file_image']).attr('src', data['default_image']);
  $(data['file_image']+' li').remove();
  $(data['file_name']).text(data['default_name']);
}
function readFileURL(data) {
  $('.rect').remove();
  $('.outer-frame-overflow-y li').remove();
  $(data['file_image']).attr('src', data['default_image']);
  if(data['file_picker'].files && data['file_picker'].files[0] != undefined) {
    var reader = new FileReader();
    reader.onload = function(e){
      $(data['file_image']).attr('src', e.target.result);
    }
    reader.readAsDataURL(data['file_picker'].files[0]);
  }
}
function readFilesURL(data) {
  $(data['file_image']+' li').remove();
  var file_id = 0;
  if(data['file_picker'].files && data['file_picker'].files[0] != undefined) {
    for(var i = 0; i < data['file_picker'].files.length; i++){
      var reader = new FileReader();
      reader.onload = function(e){
        file_id++;
        var html =  '<li class="layout-3-3" upload-img="'+file_id+'">'+
                      '<div>'+
                        '<span class="sort">'+file_id+'</span>'+
                        '<img src="'+e.target.result+'"/>'+
                        '<button type="button" class="btn btn-light btn-sm upload-delete"><i class="icon icon-close"></i></button>'+
                      '</div>'+
                    '</li>';
        $(data['file_image']).append(html);
      }
      reader.readAsDataURL(data['file_picker'].files[i]);
    }
  }
}
function readFileName(data){
  $(data['file_name']).text(data['default_name']);
  if(data['file_picker'].files && data['file_picker'].files[0] != undefined) {
    var fileValue = data['file_picker'].files;
    $(data['file_name']).text(fileValue[0].name);
  }
}
function readFilesNumber(data){
  $(data['file_name']).text(data['default_name']);
  var fileSize = 0;
  if(data['file_picker'].files && data['file_picker'].files[0] != undefined) {
    var fileValue = data['file_picker'].files;
    fileSize = fileValue.length;
    $(data['file_name']).text(fileSize + ' files selected.');
  }
  $('.file-multiple').attr('file_size', fileSize);
  checkFilesSize(fileSize);
}
function returnUploadEnabled() {
  var limitation = $('#pic_total').attr('limitation');
  var total = $('#pic_total').attr('total');
  var enabled_pic = 0;
  var disabled = false;
  if(isNaN(limitation) == false && isNaN(total) == false){
    enabled_pic = parseInt(limitation - total);
  }
  if(enabled_pic <= 0) {
    disabled = true;
    alertMessage(check_limitation_message, 0, '', 1500);
  }
  $('.file-multiple .custom-file-input').prop('disabled', disabled);
  $('.upload-save').prop('disabled', disabled);
}
function checkFilesSize(fileSize) {
  var limitation = $('#upload_pic_total').attr('limitation');
  var total = $('#upload_pic_total').attr('total');
  var enabled_pic = 0;
  var disabled = false;
  var file_size = $('.file-multiple').attr('file_size');
  if(isNaN(limitation) == false && isNaN(total) == false){
    enabled_pic = parseInt(limitation - total);
  }
  if(fileSize == undefined) {
    fileSize = file_size;
  }
  if(fileSize > enabled_pic) {
    disabled = true;
    alertMessage(check_files_size_message + parseInt(fileSize-enabled_pic), 0, '', 1500);
  }
  if(fileSize == enabled_pic) {
    disabled = false;
  }
  $('#upload_enabled_pic').text(enabled_pic);
  $('.upload-save').prop('disabled', disabled);
}
function check_value(check_form) {
  var num = 0;
  $('.'+check_form).each(function() {
    $('.required', this).each(function(){
      if(rule_loader($(this).val(), '', 'required')) {
        render_input_status($(this), true, '');
        render_input_error_message($(this).siblings('.input-error'), true, '');
        alertMessage('success', 1, '');
      } else {
        render_input_status($(this), false, message.required);
        render_input_error_message($(this).siblings('.input-error'), false, message.required);
        alertMessage(message.required, 0, '');
        num++;
      };
    });
    if(num == 0){
      $('.equalTo', this).each(function(){
        if(rule_loader($('.new_password').val(), $('.confirm_new_password').val(), 'equalTo')) {
          render_input_status($(this), true, '');
          render_input_error_message($(this).siblings('.input-error'), true, '');
          alertMessage('success', 1, '');
        } else {
          render_input_status($(this), false, message.equalTo);
          render_input_error_message($(this).siblings('.input-error'), false, message.equalTo);
          alertMessage(message.equalTo, 0, '');
        };
      });
    }
  });
}

// Wcbcam
var screenshotButton = document.querySelector('.screenshot-button');
var img = document.querySelector('#videostream .source-img');
var video = document.querySelector('#videostream video');
var canvas = document.createElement('canvas');
var checkEnabled = 0;
// Open Webcam
function captureVideoButtons(data){
  screenshotButton = document.querySelector(data.screenshotButton);
  img = document.querySelector(data.img);
  video = document.querySelector(data.video);
  checkEnabled = data.checkEnabled;
  var videoW = 1920;//1280;
  var videoH = 1080;//720;
  navigator.mediaDevices.getUserMedia({
    video: {
      width: {
        ideal: videoW
      },
      height: {
        ideal: videoH
      },
      sharpness: 100
    }
  }).then(handleSuccess).catch(handleError);
}
function handleSuccess(stream) {
  $(screenshotButton).prop('disabled', false);
  if(checkEnabled == 1) {
    returnCurrentEnabled();
  }
  video.srcObject = stream;
}
function handleStop(){
  try { 
    if(video.srcObject){
      video.srcObject.getTracks().forEach(function (track) {
        track.stop();
        img.src = '';
      });
    }
  } catch (e) {
  }
}
function handleStopHoldImage(){
  if(video.srcObject){
    video.srcObject.getTracks().forEach(function (track) {
      track.stop();
   })
  }
}
function handleError(error) {
  console.error('Error: ', error);
}
// screenshot
function screenshot() {
	canvas.width = video.videoWidth;
	canvas.height = video.videoHeight;
  // var canvasContext = canvas.getContext('2d');
  //     canvasContext.translate(canvas.width, 0);
  //     canvasContext.scale(-1, 1);
  //     canvasContext.drawImage(video, 0, 0);
  canvas.getContext('2d').drawImage(video, 0, 0);
  addImageList(canvas.toDataURL('image/jpeg'));
  countCurrentEnabled(1);
}
// 增加圖片清單
function addImageList(image) {
  var html =  '<li class="layout-5">'+
                '<div class="screenshot_pic">'+
                  '<img src="'+image+'"/>'+
                  '<button type="button" class="btn btn-light btn-sm delete-img"><i class="icon icon-close"></i></button>'+
                '</div>'+
              '</li>';
  $('.screenshot-img').prepend(html);
}
// 清除圖片清單
function removeImageList(element) {
  $(element).parent().parent().remove();
}
// 圖片清單排序
function imageListSort(data) {
  $(data['file_name']).text(data['file_image_size']+' files selected.');
  var i =1;
  $(data['file_sort_picker']).each(function(){
    $(this).text(i);
    $('.file-multiple').attr('file_size', i);
    i++;
  });
  if(data['file_image_size'] <= 0) {
    var file_data = {
        'file_picker': this,
        'file_image': '.multiple-images',
        'file_name': '.custom-file-label',
        'default_image': '/static/image/default_image.svg',
        'default_name': unselected_file
    };
    clearReadFile(file_data);
  }
}
function checkLimitation() {
  var limitation = $('#upload_pic_total').attr('limitation');
  var total = $('#upload_pic_total').attr('total');
  var enabled_pic = 0;
  var disabled = false;
  if(isNaN(limitation) == false && isNaN(total) == false){
    enabled_pic = parseInt(limitation - total);
  }
  if(enabled_pic <= 0) {
    disabled = true;
    alertMessage(check_limitation_message, 0, '', 1500);
  }
  $('#upload_enabled_pic').text(enabled_pic);
  $('.file-multiple .custom-file-input').prop('disabled', disabled);
  $('.upload-save').prop('disabled', disabled);
}
function returnCurrentEnabled() {
  var limitation = $('#pic_total').attr('limitation');
  var total = $('#pic_total').attr('total');
  var enabled_pic = 0;
  var disabled = false;
  if(isNaN(limitation) == false && isNaN(total) == false){
    enabled_pic = parseInt(limitation - total);
  }
  if(enabled_pic <= 0) {
    disabled = true;
    alertMessage(check_limitation_message, 0, '', 1500);
  }
  $('.screenshot-button').prop('disabled', disabled);
  $('.save_product_image').prop('disabled', disabled);
  $('#enabled_pic').text(enabled_pic);
  $('#current_pic').text('0');
}
function countCurrentEnabled(count) {
  var current_pic = $('#current_pic').text();
  var enabled_pic = $('#enabled_pic').text();
  if(count) {
    current_pic++;
    enabled_pic--;
  } else {
    current_pic--;
    enabled_pic++;
  };
  var disabled = false;
  if(enabled_pic <= 0) {
    disabled = true;
    alertMessage(check_limitation_message, 0, '', 1500);
  }
  $('.screenshot-button').prop('disabled', disabled);
  $('#current_pic').text(current_pic);
  $('#enabled_pic').text(enabled_pic);
}

// screenshot recognition test
var mockData = 0;
function screenshotRecognitionTest() {
  screenshot_loading_open();
	canvas.width = video.videoWidth;
	canvas.height = video.videoHeight;
  // var canvasContext = canvas.getContext('2d');
  //     canvasContext.translate(canvas.width, 0);
  //     canvasContext.scale(-1, 1);
  //     canvasContext.drawImage(video, 0, 0);
  canvas.getContext('2d').drawImage(video, 0, 0);
  img.src = canvas.toDataURL('image/jpeg');
  // API
  if(api["screenshot"].domain === ''){
    api["screenshot"].domain = api_host;
  }
  var url = api["screenshot"].domain + api["screenshot"].url;
  var method = api["screenshot"].method;
  var data = {"image": canvas.toDataURL('image/jpeg'),};
  sendRecognitionTestData(url, method, data, resultRecognitionTestData);
}
function sendRecognitionTestData(url, method, data, callback_function) {
  var mock_data = {
    "code": "0001",
    "data": [
      {
        "bounding_box": {
          "h": 382,
          "w": 266,
          "x": 763,
          "y": 315
        },
        "sku": 1234567890,
        "name": "測試商品名稱",
        "price": 999,
        "score": 0,
        "thumbnail": "/static/image/test-1.jpeg",
        "symbol": "¥",
      },
      {
        "bounding_box": {
          "h": 250,
          "w": 250,
          "x": 50,
          "y": 50
        },
        "sku": 2134,
        "name": "測試背面商品",
        "price": 999,
        "score": 0,
        "thumbnail": "/static/image/test-1.jpeg",
        "symbol": "¥",
      },
    ],
    "message":"Success",
    "pass_by":null,
  };
  $.ajax({
    url: url,
    method: method,
    dataType: 'json',
    data: data,
    error: function(data){
      if(mockData == 1){
        // 若 mockData = 1 使用假資料顯示
        console.log('目前顯示資訊為mock Data');
        var data = mock_data;
        callback_function(data['data']);
      }else{
        alertMessage(data.statusText, 0, data.status, '');
      }
      $('.screenshot-button-RT').addClass('hidden');
      $('.upload-RT').addClass('hidden');
      $('.re-checkout').removeClass('hidden');
      screenshot_loading_close();
    },
    success: function(data, textStatus, jqXHR){
      if(jqXHR.status == 200){
        if(mockData == 1){
          // 若 mockData = 1 使用假資料顯示
          console.log('目前顯示資訊為mock Data');
          var data = mock_data;
          callback_function(data['data']);
        }else{
          if(data['code'] == '0001'){
            console.log(data);
            callback_function(data['data']['checkout']);
          } else {
            console.log(data);
            alertMessage(data['message'], 0, '', ''); 
          }
          $('.screenshot-button-RT').addClass('hidden');
          $('.upload-RT').addClass('hidden');
          $('.re-checkout').removeClass('hidden');
          screenshot_loading_close();
        }
      }
    },
  });
}
function resultRecognitionTestData(data) {
  $('.rect').remove();
  $('.outer-frame-overflow-y li').remove();
  organizeRecognitionTestData(data);
  processingRecognitionTestData(data);
  $(window).resize(function(){
    $('.rect').remove();
    processingRecognitionTestData(data);
  });
}
function resultRecognitionTestDataForUpload(data) {
  organizeRecognitionTestData(data);
  processingRecognitionTestDataForUpload(data);
  $(window).resize(function(){
    $('.rect').remove();
    processingRecognitionTestDataForUpload(data);
  });
}
var backOfProductId = 1;
var backOfProductIdArray = ["2134"];
function organizeRecognitionTestData(data) {
  if(backOfProductId === 1){
    $.each(data, function(key, value){
      if(typeof(value['sku']) != 'undefined'){
        backOfProductIdArray.forEach(element => {
          if(parseInt(value['sku']) === parseInt(element)){
            data.splice(key, 1);
            data.unshift({
              "bounding_box": {
                "h": value["bounding_box"]["h"],
                "w": value["bounding_box"]["w"],
                "x": value["bounding_box"]["x"],
                "y": value["bounding_box"]["y"]
              },
              "sku": value['sku'],
              "name": value['name'],
              "thumbnail": value['thumbnail']
            });
          }
        });
      }
    });
  }
  recognitionTestProductList(data);
}
function recognitionTestProductList(organizeData) {
  // 加入商品列表
  var array = [];
  var prod = [];
  var num = 0;
  var totalPrice = 0;
  var rewrite = 0;
  $.each(organizeData, function(key, value){
    num++;
    var prod_id = 'Nan_id_'+num;
    var prod_price = 0;
    if(typeof(value['sku']) != 'undefined'){
      prod_id = value['sku'];
    }
    if(typeof(value['symbol']) != 'undefined' && rewrite === 0){
      // config 的 useSymbol 設定為 0 使用模型symbol, 設定為 1 為使用樣板symbol
      if(typeof(useSymbol) === 0){
        symbol = value['symbol'];
        rewrite++;
      }
    }
    if(typeof(value['price']) != 'undefined'){
      prod_price = value['price'];
    }
    totalPrice += parseFloat(prod_price);
    var html =  '<li class="row outer-frame-border list-no-height list-'+prod_id+'" data-key="'+prod_id+'" onclick="addSelectedList(this)">'+
                  '<div class="layout-8 padding-0">'+
                    '<span class="sku-barcode-style">'+prod_id+'</span>'+
                    '<span class="sku-name-style-1 name">'+value['name']+'</span>'+
                  '</div>'+
                  '<div class="layout-2 padding-0 ta-r">'+
                    '<span class="num">x '+1+'</span>'+
                  '</div>'+
                '</li>';
    $('.outer-frame-overflow-y').append(html);
    $('.total-num').html('x '+parseInt(num));
    //$('.total').html(symbol+' '+parseFloat(totalPrice).toFixed(2));
    if(typeof(lang) != 'undefined' && lang == 'TW'){
      $('.total').html(symbol+' '+parseInt(totalPrice));
    }
    array.push(prod_id);
    prod.push({'prod_id': prod_id, 'price': prod_price});
  });
  // 計算小計
  subtotal(prod);
  // 若遇重複的商品列表做合併
  mergeList(array);
  // 選取第一個元素做效果
  if($('.outer-frame-overflow-y li').size() != 0){
    $('.outer-frame-overflow-y li:first-child').addClass('selected');
    var dataKey = $('.outer-frame-overflow-y li:first-child').attr('data-key');
    $('.list-'+dataKey).addClass('selected');
  }
}
function mergeList(array){
  // 將重複商品列表刪除保留一個, 顯示重複的數量
  var newArray = [];
  for(var i = 0; i < array.length; i++){
    if(newArray.indexOf(array[i]) === -1){
      newArray.push(array[i]);
      $('.list-'+array[i]).slice(1).remove();
      $('.list-'+array[i]+' .num').html('x '+collectionRepeat(array, array[i]));
    }
  }
};
function subtotal(prod){
  var result = {};
  prod.forEach(item => {
    if(result[item.prod_id]){
      result[item.prod_id] += parseFloat(item.price);
    }else{
      result[item.prod_id] = parseFloat(item.price);
    }
  });
  $.each(result, function(key, value){
    $('.list-'+key+' .price').html(parseFloat(value).toFixed(2));
    if(typeof(lang) != 'undefined' && lang === 'TW'){
      $('.list-'+key+' .price').html(parseInt(value));
      $('.symbol').addClass('symbol-TW');
    }
  });
};
function collectionRepeat(array, key){
  // 計算重複的次數
  var counter = {};
  array.forEach(function(x) { 
    counter[x] = (counter[x] || 0) + 1; 
  });
  var val = counter[key];
  if (key === undefined) {
    return counter;
  }
  return (val) === undefined ? 0 : val;
};
function processingRecognitionTestData(data){
  // 處理回傳Data的畫框資訊
  var currentWidth = document.getElementById('source-img-RT').width;
  var currentHeight = document.getElementById('source-img-RT').height;
  var originalWidth = document.getElementById('source-img-RT').naturalWidth;
  var originalHeight = document.getElementById('source-img-RT').naturalHeight;
  var initWidthSize = parseFloat(currentWidth/originalWidth).toFixed(2);
  var initHeightSize = parseFloat(currentHeight/originalHeight).toFixed(2);
  var num = 0;
  $.each(data, function(key, value){
    num++;
    var prod_id = 'Nan_id_'+num;
    if(typeof(value['sku']) != 'undefined'){
      prod_id = value['sku'];
    }
    // if(isFloat(value['bounding_box']['x'])){
      var x1 = parseFloat(value['bounding_box']['x']*currentWidth).toFixed(4);
          x1 = (currentWidth-parseFloat(currentWidth))/2+parseFloat(x1);
      var y1 = parseFloat(value['bounding_box']['y']*currentHeight).toFixed(4);
      var w = parseFloat(currentWidth*value['bounding_box']['w']).toFixed(4);
      var h = parseFloat(currentHeight*value['bounding_box']['h']).toFixed(4);
    // }else{
    //   var x1 = parseInt(value['bounding_box']['x']*initWidthSize);
    //   var y1 = parseInt(value['bounding_box']['y']*initHeightSize);
    //   var w = parseInt(value['bounding_box']['w']*initWidthSize);
    //   var h = parseInt(value['bounding_box']['h']*initHeightSize);
    // }
    boundingBox(prod_id, x1, y1, w, h);
  });
  if(data.length == 0){
    alertMessage(recognition_test_no_results, 0, '', 5000); 
  }
};
function processingRecognitionTestDataForUpload(data){
  // 處理回傳Data的畫框資訊
  var currentWidth = document.getElementById('upload-img-RT').width;
  var currentHeight = document.getElementById('upload-img-RT').height;
  var originalWidth = document.getElementById('upload-img-RT').naturalWidth;
  var originalHeight = document.getElementById('upload-img-RT').naturalHeight;
  var initWidthSize = parseFloat(currentWidth/originalWidth).toFixed(2);
  var initHeightSize = parseFloat(currentHeight/originalHeight).toFixed(2);
  var num = 0;
  var upload_img_position = $('#upload-img-RT').position();
  $.each(data, function(key, value){
    num++;
    var prod_id = 'Nan_id_'+num;
    if(typeof(value['sku']) != 'undefined'){
      prod_id = value['sku'];
    }
    // if(isFloat(value['bounding_box']['x'])){
      var x1 = parseFloat(value['bounding_box']['x']*currentWidth).toFixed(4);
          x1 = (currentWidth-parseFloat(currentWidth))/2+parseFloat(x1);
          x1 = parseFloat(x1 + parseFloat(upload_img_position.left)).toFixed(4);
      var y1 = parseFloat(value['bounding_box']['y']*currentHeight).toFixed(4);
      var w = parseFloat(currentWidth*value['bounding_box']['w']).toFixed(4);
      var h = parseFloat(currentHeight*value['bounding_box']['h']).toFixed(4);
    // }else{
    //   var x1 = parseInt(value['bounding_box']['x']*initWidthSize);
    //   var y1 = parseInt(value['bounding_box']['y']*initHeightSize);
    //   var w = parseInt(value['bounding_box']['w']*initWidthSize);
    //   var h = parseInt(value['bounding_box']['h']*initHeightSize);
    // }
    boundingBoxForUpload(prod_id, x1, y1, w, h);
  });
  if(data.length == 0){
    alertMessage(recognition_test_no_results, 0, '', ''); 
  }
};
function isFloat(n){
  // 判斷是否為浮點數
  return n % 1 !== 0;
};
function boundingBox(num, x1, y1, w, h){
  // 畫bounding box
  if($('.outer-frame-overflow-y li').size() != 0){
    var html = '<div class="rect rect-'+num+'" data-key="'+num+'" onclick="addSelectedRect(this)" style="left:'+x1+'px; top:'+y1+'px; width:'+w+'px; height:'+h+'px;"></div>';
    $('#videostream-RT').append(html);
    var dataKey = $('.outer-frame-overflow-y li:first-child').attr('data-key');
    $('.rect-'+dataKey).addClass('selected');
  }
  if(backOfProductId === 1){
    backOfProductIdArray.forEach(element => {
      if(num === parseInt(element)){
        $('.rect-'+num).addClass('rect-error');
      }
    });
  }
};
function boundingBoxForUpload(num, x1, y1, w, h){
  if($('.outer-frame-overflow-y li').size() != 0){
    var html = '<div class="rect rect-'+num+'" data-key="'+num+'" onclick="addSelectedRect(this)" style="left:'+x1+'px; top:'+y1+'px; width:'+w+'px; height:'+h+'px;"></div>';
    $('.draw-wrapper').append(html);
    var dataKey = $('.outer-frame-overflow-y li:first-child').attr('data-key');
    $('.rect-'+dataKey).addClass('selected');
  }
  if(backOfProductId === 1){
    backOfProductIdArray.forEach(element => {
      if(num === parseInt(element)){
        $('.rect-'+num).addClass('rect-error');
      }
    });
  }
}
function addSelectedList(even){
  var dataKey = $(even).attr('data-key');
  $('.outer-frame-overflow-y li').removeClass('selected');
  $('.rect').removeClass('selected');
  $('.rect-'+dataKey).addClass('selected');
  $('.list-'+dataKey).addClass('selected');
};
function addSelectedRect(even){
  var dataKey = $(even).attr('data-key');
  $('.outer-frame-overflow-y li').removeClass('selected');
  $('.rect').removeClass('selected');
  $('.rect-'+dataKey).addClass('selected');
  $('.list-'+dataKey).addClass('selected');
};
function reRecognitionTestCamera() {
  $('.screenshot-button-RT').removeClass('hidden');
  $('.re-checkout').addClass('hidden');
  $('.rect').remove();
  $('.outer-frame-overflow-y li').remove();
  $('#source-img-RT').attr('src', '');
}
function reRecognitionTestUpload() {
  $('.upload-RT').removeClass('hidden');
  $('.re-checkout').addClass('hidden');
  $('.upload-image').attr('src', '/static/image/default_image.svg');
  $('.upload-image li').remove();
  $('.file-single .custom-file-label').text(unselected_file);
  $('.custom-file-input').val('');
  $('.rect').remove();
  $('.outer-frame-overflow-y li').remove();
}
var posArray = [];
function scrollInside(){
  var elmnt = document.getElementById('scrollDiv');
  if(elmnt != null){
    xpos = elmnt.scrollLeft;
    ypos = elmnt.scrollTop;
    posArray = [xpos, ypos];
  }
}
function scrollToAnchor(){
  $('#scrollDiv').animate({scrollTop: posArray[1]}, 500);
}
function modalSecondShow(obj){
  $(obj['selector']).addClass('show').show();
  $(obj['selector']+' .modal-body').html(obj['modal-body']);
  $(document).on('click', obj['selector']+' .modal-confirm', function(){
    obj['confirm_function']();
  });
}
function modalSecondHide(){
  $('.modal-second').removeClass('show').hide();
}
function loadingOpen(){
  $('#lds-dual-ring-wrapper').show();
}
function loadingClose(){
  $('#lds-dual-ring-wrapper').hide();
}
function tab_menu_show(tab_menu){
  $('.tab_menu_content').hide();
  $('.tab_menu_btn').removeClass('active');
  $('.tab_menu_'+tab_menu).addClass('active');
  $('#tab_menu_content_'+tab_menu).show();
}
function change_csv_file_data_loader(data){
  $(data['file_picker']).next(data['file_name']).removeClass('check-file');
  $(data['file_picker']).next(data['file_name']).text(data['default_name']);
  if(data['file_picker'].files && data['file_picker'].files[0] != undefined) {
    var fileValue = data['file_picker'].files;
    $(data['file_picker']).next(data['file_name']).text(fileValue[0].name);
    $(data['file_picker']).next(data['file_name']).addClass('check-file');
  }
}
function screenshot_loading_open(){
  loadingOpen();
  $(screenshotButton).prop('disabled', true);
}
function screenshot_loading_close(){
  loadingClose();
  $(screenshotButton).prop('disabled', false);
}
function show_selected_file_name(data){
  var wrapper = $(data['file_picker']).parent().attr('id');
  $('#'+wrapper+' .custom-file-label').text(data['default_name']);
  if(data['file_picker'].files && data['file_picker'].files[0] != undefined) {
    var fileValue = data['file_picker'].files;
    $('#'+wrapper+' .custom-file-label').text(fileValue[0].name);
  }
}
// 即時欄位檢查 - 日期
function getDate(element) {
  var date;
  try {
    date = $.datepicker.parseDate( dateFormat, element.value );
  } catch( error ) {
    date = null;
  }
  return date;
}
function datepicker_check_date(element, check_item, data) {
  var datepicker_group_wrapper = '#'+$(element).parent().parent().attr('id');
  var datepicker = [
    {
      'start': datepicker_group_wrapper+' .start_date',
      'end': datepicker_group_wrapper+' .end_date',
    },
    {
      'start_error': datepicker_group_wrapper+' .start_date_error',
      'end_error': datepicker_group_wrapper+' .end_date_error',
    }
  ];
  var startDate = $(datepicker[0].start).datepicker('getDate');
  var endDate = $(datepicker[0].end).datepicker('getDate');
  // clear input status and messages
  $.each(datepicker[0], function(key, value){ inputStatusClear(value); });
  $.each(datepicker[1], function(key, value){ inputMessage(value, 0, ''); });
  $(datepicker_group_wrapper).attr('check', '0');
  if(!check_item){
    // difference in days. 86400 seconds in day, 1000 ms in second
    var dateDiff = (endDate - startDate)/(86400 * 1000);  
    if (endDate != null && dateDiff < 0) {
      inputStatus(datepicker[0].start, 0);
      inputMessage(datepicker[1].start_error, 1, data.error_text[0]);
      $(datepicker_group_wrapper).attr('check', '1');
      return false;
    }
    return true;
  }else{
    //difference in days. 86400 seconds in day, 1000 ms in second
    var dateDiff = (startDate - endDate)/(86400 * 1000);
    if (startDate != null && dateDiff > 0) {
      inputStatus(datepicker[0].end, 0);
      inputMessage(datepicker[1].end_error, 1, data.error_text[1]);
      $(datepicker_group_wrapper).attr('check', '1');
      return false;
    }
    return true;
  }
}
// 再次欄位檢查 - 日期
function datepicker_check_date_again(element, check_item, error_text) {
  var datepicker_group_wrapper = '#'+$(element).parent().parent().attr('id');
  var datepicker = [
    {
      'start': datepicker_group_wrapper+' .start_date',
      'end': datepicker_group_wrapper+' .end_date'
    },
    {
      'start_error': datepicker_group_wrapper+' .start_date_error',
      'end_error': datepicker_group_wrapper+' .end_date_error'
    }
  ];
  var startDate = $(datepicker[0].start).datepicker('getDate');
  var endDate = $(datepicker[0].end).datepicker('getDate');
  // clear input status and messages
  $.each(datepicker[0], function(key, value){ inputStatusClear(value); });
  $.each(datepicker[1], function(key, value){ inputMessage(value, 0, ''); });
  if(!check_item){
    // difference in days. 86400 seconds in day, 1000 ms in second
    var dateDiff = (endDate - startDate)/(86400 * 1000);  
    if (endDate != null && dateDiff < 0) {
      $.each(datepicker[0], function(key, value){ inputStatus(value, 0); });
      $.each(datepicker[1], function(key, value){ inputMessage(value, 1, error_text); });
      return false;
    }
    return true;
  }else{
    //difference in days. 86400 seconds in day, 1000 ms in second
    var dateDiff = (startDate - endDate)/(86400 * 1000);
    if (startDate != null && dateDiff > 0) {
      $.each(datepicker[0], function(key, value){ inputStatus(value, 0); });
      $.each(datepicker[1], function(key, value){ inputMessage(value, 1, error_text); });
      return false;
    }
    return true;
  }
}
// 欄位檢查 - 必填
function required_check_value(input_data){
  num = 0;
  $.each(input_data, function(k, input){
    var error_input = $(input).next().next();
    inputStatusClear(input);
    inputMessage(error_input, 0, '');
    if($(input).val() == ""){
      inputStatus(input, 0);
      inputMessage(error_input, 1, input_required_text);
      num++;
    }
  });
  if(num == 0){
    return true;
  }
  return false;
}
// 欄位檢查
function check_input_value(){
  var check_data = {
    "regex": [
              {
                "rule": /^[a-zAz0-9\-]*$/,
                "binding": [".product_sn"]
              },
              {
                "rule": /^[a-zA-Z0-9_\(\)\u4e00-\u9fa5\u0800-\u4e00\-\.#@\s\u3000]+$/,
                "binding": [".product_name"]
              },
              {
                "rule": /^[a-zA-Z0-9_\(\)\u4e00-\u9fa5\u0800-\u4e00\-\.#@\s\u3000]+$/,
                "binding": [".abbreviation"]
              },
              {
                "rule": /^[a-zAz0-9\-]*$/,
                "binding": [".barcode"]
              }
             ],
    "function": [
                  {
                    "rule": datepicker_check_date_again,
                    "binding": [".start_date", ".end_date"]
                  }
                ]
  };
  num = 0;
  $.each(check_data["regex"], function(key, value){
    var input_value = $(value["binding"][0]).val();
    var error_input = $(value["binding"][0]).next().next();
    inputStatusClear(value["binding"][0]);
    inputMessage(error_input, 0, '');
    if(input_value != ""){
      if(!input_value.match(value["rule"])){
        inputStatus(value["binding"][0], 0);
        inputMessage(error_input, 1, input_format_error_text);
        num++;
      }
    }
  });
  $.each(check_data["function"], function(key, value){
    $(value["binding"][0]).each(function(k, input){
      if(!value["rule"](input, 0, input_datepicker_error_text)){
        num++;
      }
    });
  });
  if(num == 0){
    return true;
  }
  return false;
}
