/***********************
 *    VCMS API Object
 ***********************/
//   var api_host = '';
//   var api = {
//      'screenshot': {
//        'domain': '',
//        'url': screenshot_api,
//        'method': 'POST',
//        'data': {},
//        'callback_function': '',
//      '  error_function': ''
//      }
//   };

/**************************************************************************************
 *    Accordion Menu
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 * 2. menu level 最多到四層, 超過不顯示。
 * 3. 畫面呈現方式會依照 accordion menu 陣列內物件的順序。
 * 4. openSubmenu 設置為 1, 若有 submenu 則展開, 同一層僅顯示第一筆。
 * 5. tabContentShow 設置為 1, 顯示 alink 對應的內容。
 * 6. parent 第一層預設為 0, 第二層之後需設置 submenu 要掛載的 parent, 若無該 parent 將不顯示。
 * 7. title 字元超過則顯示..., 依照RWD做調整。
 * 8. alink 設置連結若該元素還有 child, 點擊時只會展開 submenu 不會前往連結處。
 **************************************************************************************/
// var accordion_menu_data = [
//     {
//       'submenuList': [
//         {
//           'openSubmenu': 1,
//           'tabContentShow': 0,
//           'parent': 0,
//           'title': 'Default level one',
//           'alink': ''
//         },
//       ]
//     },
//     {
//       'submenuList': [
//         {
//           'openSubmenu': 1,
//           'tabContentShow': 0,
//           'parent': 1,
//           'title': 'Default level two',
//           'alink': ''
//         },
//       ]
//     },
//     {
//       'submenuList': [
//         {
//           'openSubmenu': 1,
//           'tabContentShow': 0,
//           'parent': 1,
//           'title': 'Default level three',
//           'alink': ''
//         },
//       ]
//     },
//     {
//       'submenuList': [
//         {
//           'openSubmenu': 0,
//           'tabContentShow': 1,
//           'parent': 1,
//           'title': 'Default level four',
//           'alink': '#tab-content-1'
//         },
//       ]
//     }
//   ];
// accordion_menu_data_loader(accordion_menu_data);

/**************************************************************************************
 *    model
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 * 2. modal-element 指定 model 的 id。
 * 3. modal-title 設定 title 的內容 (限制text)。
 * 4. modal-body 設定 body 的內容 (限制text)。
 **************************************************************************************/
// var model_data = {
//     'display': 0,
//     'modal-element': '#modalCenterText',
//     'modal-title': 'Please confirm again.',
//     'modal-body': 'Are you sure you want to『enable』the item?'
//   };
// modal_data_loader(model_data);

/**************************************************************************************
 *    alert message
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 * 2. alert message 公用訊息顯示在頁面中上位置。
 * 3. status = false (0) 為紅色, status = true (1) 為綠色, 其餘為黃色。
 * 4. ajaxStatus 若使用在 ajax 可以帶入錯誤代碼。
 * 5. message 放入想顯示的 messages。
 * 6. seconds 可以設置多久後隱藏 alert 以毫秒為單位, 若為空值則不隱藏。
 **************************************************************************************/
// var alert_data = {
//   'display': 0,
//   'data': {
//     'status': 0,
//     'ajaxStatus': '',
//     'message': 'messages',
//     'seconds': ''
//   }
// }
// alert_message_data_loader(alert_data);

/**************************************************************************************
 *    input status
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 * 2. input 外框顯示顏色。
 * 3. element 設定 input 的 id 或 class。
 * 4. status = false (0) 為紅色, status = true (1) 為綠色。
 **************************************************************************************/
// var input_status_data = {
//   'display': 0,
//   'data': {
//     'element': '.barcode',
//     'status': 0,
//   }
// }
// input_status_data_loader(input_status_data);

/**************************************************************************************
 *    input message
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 * 2. 顯示在input右下的訊息。
 * 3. element 設定 input 的 id 或 class。
 * 4. status = false (0) 為不顯示, status = true (1) 為顯示。
 * 5. message 放入想顯示的 messages。
 **************************************************************************************/
// var input_message_data = {
//   'display': 0,
//   'data': {
//     'element': '.input-error',
//     'status': 1,
//     'message': 'Error Message'
//   }
// }
// input_message_data_loader(input_message_data);

/**************************************************************************************
 *    switch status
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 * 2. 滑動式的 checkbox。
 * 3. html switch 的 input 添加 class = "switch- + 1~n"。
 * 4. sysid 放入對應的 1~n。
 * 5. status = false (0) 為灰色, status = true (1) 為綠色。
 **************************************************************************************/
// var switch_data = {
//   'display': 0,
//   'data': {
//     'sysid': ['00000', '00001'],
//     'status': 0
//   }
// };
// switch_status_data_loader(switch_data);

/**************************************************************************************
 *    webcam
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 **************************************************************************************/
// var webcam_data = {
//   'display': 0,
//   'data': {}
// }
// webcam_data_loader(webcam_data);

/**************************************************************************************
 *    change file
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 * 2. multiple 設定 false (0) 為單選預覽, true (1) 為多選預覽。
 * 3. file_picker 放入當前事件的 this。
 * 4. file_image 選擇後圖片需顯示區塊的 id / class。
 * 5. file_name 選擇後檔案名稱需顯示的 id / class。
 * 6. default_image 預設的圖片路徑。
 * 7. default_name 預設的input顯示的字樣。
 **************************************************************************************/
// var file_data = {
//   'display': 0,
//   'multiple': 0,
//   'data': {
//     'file_picker': this,
//     'file_image': '.upload-image',
//     'file_name': '.custom-file-label',
//     'default_image': '/image/default_image.svg',
//     'default_name': '尚未選擇檔案'
//   }
// }
// change_file_data_loader(file_data);

/**************************************************************************************
 *    select checkbox all
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 * 2. select_all false (0) 為一般 checkbox, true (1) 為選取所有 checkbox。
 * 3. wrapper 選取 checkbox 的 wrapper。
 * 4. select_all_picker 選取全部 checkbox 的 id / class。
 * 5. seclct_picker 被全部選取的 checkbox 的 class。
 * 6. max 設定邊界。
 **************************************************************************************/
// var select_checkbox_data = {
//   'display': 0,
//   'select_all': 0,
//   'data': {
//     'wrapper': '.select-checkbox-wrapper',
//     'select_all_picker': '#select-checkbox-all',
//     'seclct_picker': '.select-checkbox',
//     'max': $('.select-checkbox-wrapper .sublayer').size()
//   }
// }
// select_checkbox_data_loader(select_checkbox_data);

/**************************************************************************************
 *    validation
 * 1. display false (0) 為隱藏, true (1) 為顯示。
 **************************************************************************************/
// var validation_data = {
//   'display': 1,
//   'data': {
//     'required': ['.barcode', '.item_local_name', '.custom-file-input'],
//     'number': ['.barcode']
//   }
// }
// validation_data_loader(validation_data);

/***********************
 *    Event
 ***********************/
$(function(){
  if(typeof(accordion_menu) != 'undefined'){
    accordion_menu_data_loader(accordion_menu);
  }
  $('.accordion-menu').children('li').click(function(e) {
    openSubmenu(e, this);
  });
  $('.submenu').children('li').click(function(e) {
    openSubmenu(e, this);
    var webcam_data = {
        'display': 1,
        'screenshotButton': '.screenshot-button-RT',
        'img': '#source-img-RT',
        'video': '#videostream-RT video',
        'checkEnabled': 0
    }
    webcam_data_loader(webcam_data);
  });
  $(document).on('click', '.switch', function() {
    var model_data = {
        'display': 1,
        'modal-element': '#modalCenterText',
        'modal-title': confirm_title,
        'modal-body': disabled_dialog
      };
    // modal_data_loader(model_data);
  });
  $(document).on('click', '.enable', function(){
    var model_data = {
        'display': 1,
        'modal-element': '#modalCenterText',
        'modal-title': confirm_title,
        'modal-body': enabled_dialog
    };
    enabled = 1
    $(".save_status").attr("data_sn",0);
    $(".save_status").attr("status_sn",enabled);
    $(".save_status").attr("ajax_url",$(this).attr("ajax_url"));
    $(".save_status").attr("product_sn",$(this).attr("product_sn"));
    $(".save_status").attr("tab_sn",$(this).attr("tab_sn"));
    modal_data_loader(model_data);
  });
  $(document).on('click', '.disable', function(){
    var model_data = {
        'display': 1,
        'modal-element': '#modalCenterText',
        'modal-title': confirm_title,
        'modal-body': disabled_dialog
      };
    enabled = 0
    $(".save_status").attr("data_sn",0);
    $(".save_status").attr("status_sn",enabled);
    $(".save_status").attr("ajax_url",$(this).attr("ajax_url"));
    $(".save_status").attr("product_sn",$(this).attr("product_sn"));
    $(".save_status").attr("tab_sn",$(this).attr("tab_sn"));
    modal_data_loader(model_data);
  });
  $(document).on('click', '.delete', function(){
    var model_data = {
        'display': 1,
        'modal-element': '#modalCenterText',
        'modal-title': confirm_title,
        'modal-body': delete_dialog
      };
    enabled = -1
    $(".save_status").attr("data_sn",0);
    $(".save_status").attr("status_sn",enabled);
    $(".save_status").attr("ajax_url",$(this).attr("ajax_url"));
    $(".save_status").attr("product_sn",$(this).attr("product_sn"));
    $(".save_status").attr("tab_sn",$(this).attr("tab_sn"));
    modal_data_loader(model_data);
  });
  $(document).on('click', '.alert .close', function(){
    var alert_data = {
        'display': 0,
        'status': 0,
        'ajaxStatus': '',
        'message': 'messages',
        'seconds': ''
      };
    alert_message_data_loader(alert_data);
  });
  $(document).on('click', '.modal .close', function(){
    var model_data = {
      'display': 0
    };
    modal_data_loader(model_data);
    restoreSwitchStatus();
    $('.upload').prop('disabled', false);
    $('.camera').prop('disabled', false);
  });
  $(document).on('click', '.modal .cancel', function(){
    var model_data = {
      'display': 0
    };
    modal_data_loader(model_data);
    restoreSwitchStatus();
    $('.upload').prop('disabled', false);
    $('.camera').prop('disabled', false);
  });
  $(document).on('click', '#select-checkbox-all', function(){
    var select_checkbox_data = {
        'display': 1,
        'select_all': 1,
        'wrapper': '.select-checkbox-wrapper',
        'select_all_picker': '#select-checkbox-all',
        'seclct_picker': '.select-checkbox',
        'max': ''
      };
    select_checkbox_data_loader(select_checkbox_data);
  });
  $(document).on('click', '.select-checkbox', function(){
    var select_checkbox_data = {
        'display': 1,
        'select_all': 0,
        'wrapper': '.select-checkbox-wrapper',
        'select_all_picker': '#select-checkbox-all',
        'seclct_picker': '.select-checkbox',
        'max': $('.select-checkbox-wrapper .sublayer').size()
      };
    select_checkbox_data_loader(select_checkbox_data);
  });
  $(document).on('click', '#select-checkbox-all-1', function(){
    var select_checkbox_data = {
        'display': 1,
        'select_all': 1,
        'wrapper': '.select-checkbox-wrapper-1',
        'select_all_picker': '#select-checkbox-all-1',
        'seclct_picker': '.select-checkbox-1',
        'max': ''
      };
    select_checkbox_data_loader(select_checkbox_data);
  });
  $(document).on('click', '.select-checkbox-1', function(){
    var select_checkbox_data = {
        'display': 1,
        'select_all': 0,
        'wrapper': '.select-checkbox-wrapper-1',
        'select_all_picker': '#select-checkbox-all-1',
        'seclct_picker': '.select-checkbox-1',
        'max': $('.select-checkbox-wrapper-1 .sublayer').size()
      };
    select_checkbox_data_loader(select_checkbox_data);
  });
  $(document).on('click', '.tab-btn', function(){
    tabContentBtn(this);
  });
  $(document).on('click', '.add-product', function(){
    var validation_data = {
        'display': 1,
        'required': ['.barcode', '.item_local_name', '.custom-file-input'],
        'number': ['.barcode']
      };
    validation_data_loader(validation_data);
  });
  $(document).on('click', '.save-change-pwd', function(){
    // 1. 檢查'當前密碼''新密碼''確認密碼'不為空值
    // 2. 檢查'當前密碼'與'新密碼'為不同
    // 2. 檢查'新密碼'與'確認密碼'為相同
    // 3. 傳遞 user_id, current_password, new_password, confirm_new_password
    if(check_value('change-pwd-form')){
      $(this).parents().prev().submit();
    }
  });
  $(document).on('click', '.add-item', function(){
    var file_data = {
        'display': 0,
        'multiple': 0,
        'file_picker': this,
        'file_image': '.upload-image',
        'file_name': '.custom-file-label',
        'default_image': '/static/image/default_image.svg',
        'default_name': unselected_file
      };
    change_file_data_loader(file_data);
  });
  $(document).on('click', '.upload', function(){
    $('.upload').prop('disabled', true);
    $('.camera').prop('disabled', true);
    checkLimitation();
    var file_data = {
        'display': 0,
        'multiple': 1,
        'file_picker': this,
        'file_image': '.multiple-images',
        'file_name': '.custom-file-label',
        'default_image': '/static/image/default_image.svg',
        'default_name': unselected_file
      };
    change_file_data_loader(file_data);
    var model_data = {
        'display': 1,
        'modal-element': '#modalCenterUpload',
        'modal-title': modal_title_upload,
        'modal-body': ''
      };
    modal_data_loader(model_data);
  });
  $(document).on('click', '.upload-save', function(){
    var action = 'save_items_status';
    var data = '';
    send_ajax(action, data, switchStatus);
  });
  $(document).on('click', '.upload-delete', function(){
    removeImageList(this);
    var images_sort_data = {
      'file_image_size': $('.multiple-images li').size(),
      'file_name': '.custom-file-label',
      'file_sort_picker': '.multiple-images .sort',
    }
    imageListSort(images_sort_data);
    checkFilesSize();
  });
  $(document).on('click', '.camera', function(){
    $('.upload').prop('disabled', true);
    $('.camera').prop('disabled', true);
    $('.screenshot-img li').remove();
    var webcam_data = {
      'display': 0,
      'screenshotButton': '.screenshot-button',
      'img': '#source-img',
      'video': '#videostream video',
      'checkEnabled': 1
    }
    webcam_data_loader(webcam_data);
    var model_data = {
        'display': 1,
        'modal-element': '#modalCenterCamera',
        'modal-title': modal_title_camera,
        'modal-body': ''
      };
    modal_data_loader(model_data);
    $(".save_product_image").attr("data_sn",$(this).attr("data_sn"));
    $(".save_product_image").attr("tab_sn",$(this).attr("tab_sn"));
    $(".save_product_image").attr("ajax_url",$(this).attr("ajax_url"));
    $("#pic_total").attr("limitation",$(this).attr("image_limit"));
    $("#pic_total").attr("total",$(this).attr("current_image_total"));
    $("#pic_total").text($(this).attr("current_image_total"));

    returnCurrentEnabled();
  });
  $(document).on('click', '.webcam-open', function() {
    var webcam_data = {
      'display': 0,
      'screenshotButton': '.screenshot-button',
      'img': '#source-img',
      'video': '#videostream video',
      'checkEnabled': 0
    }
    webcam_data_loader(webcam_data);
  });
  $(document).on('click', '.webcam-stop', function(){
    var webcam_data = {
      'display': 1,
      'screenshotButton': '.screenshot-button',
      'img': '#source-img',
      'video': '#videostream video',
      'checkEnabled': 0
    }
    webcam_data_loader(webcam_data);
  });
  $(document).on('click', '.self-webcam-open', function(){
    
  });
  $(document).on('click', '.screenshot-button', function(){
    screenshot();
  });
  $(document).on('click', '.delete-img', function(){
    removeImageList(this);
    countCurrentEnabled(0);
  });
  $(document).on('change', '.file-single .custom-file-input', function(){
    var file_data = {
        'display': 1,
        'multiple': 0,
        'file_picker': this,
        'file_image': '.upload-image',
        'file_name': '.file-single .custom-file-label',
        'default_image': '/static/image/default_image.svg',
        'default_name': unselected_file
      };
    change_file_data_loader(file_data);
  });
  $(document).on('click', '.file-multiple .custom-file-input', function(e){
    if($('.multiple-images li').size() != 0){
      e.preventDefault();
      $('#modalSecond').addClass('show').show();
    }else{
      var file_data = {
        'display': 0,
        'multiple': 1,
        'file_picker': this,
        'file_image': '.multiple-images',
        'file_name': '.file-multiple .custom-file-label',
        'default_image': '/static/image/default_image.svg',
        'default_name': unselected_file
      };
      change_file_data_loader(file_data);
      $(this).val('');
    }
  });
  $(document).on('click', '.confirm-select-file', function(){
    var file_data = {
      'display': 0,
      'multiple': 1,
      'file_picker': $('#thumbnail_error'),
      'file_image': '.multiple-images',
      'file_name': '.file-multiple .custom-file-label',
      'default_image': '/static/image/default_image.svg',
      'default_name': unselected_file
    };
    change_file_data_loader(file_data);
    $('#thumbnail_error').val('');
    modalSecondHide();
    $('.file-multiple .custom-file-input').click();
  });
  $(document).on('click', '.modal-second .cancel', function(){
    modalSecondHide();
  });
  $(document).on('change', '.file-multiple .custom-file-input', function(){
    var file_data = {
        'display': 1,
        'multiple': 1,
        'file_picker': this,
        'file_image': '.multiple-images',
        'file_name': '.file-multiple .custom-file-label',
        'default_image': '/static/image/default_image.svg',
        'default_name': unselected_file
      };
    change_file_data_loader(file_data);
  });
  $(document).on('click', '.recognition-methods-camera', function(){
    reRecognitionTestCamera();
    $('.recognition-methods-button button').removeClass('focus');
    $(this).addClass('focus');
    $('.recognition-methods').addClass('hidden');
    $('.recognition-methods-1').removeClass('hidden');
  });
  $(document).on('click', '.recognition-methods-upload', function(){
    reRecognitionTestUpload();
    $('.recognition-methods-button button').removeClass('focus');
    $(this).addClass('focus');
    $('.recognition-methods').addClass('hidden');
    $('.recognition-methods-2').removeClass('hidden');
  });
  $(document).on('click', '.screenshot-button-RT', function(){
    var screenshot_api = $(this).attr("api_url");
    console.log(screenshot_api);
    api_host = '';
    api = {
      'screenshot': {
        'domain': '',
        'url': screenshot_api,
        'method': 'POST',
        'data': {},
        'callback_function': '',
        'error_function': ''
      }
    };
    rs = check_session();
    if (rs == 1){
      screenshotRecognitionTest();
    }
  });
  $(document).on('click', '.re-checkout', function(){
    rs = check_session();
    if (rs == 1){
      reRecognitionTestCamera();
    }
  });
  $(document).on('click', '.sop-btn', function(){
    var model_data = {
      'display': 1,
      'modal-element': '#modalCenterImage',
      'modal-title': '',
      'language': $(this).attr('language'),
      'sop-img': $(this).attr('img')
    };
    modal_sop_img_data_loader(model_data);
  });
  var campany_profile_data = [];
  $(document).on('click', '.edit_company_profile', function(){
    $('.company_profile-form input').each(function(k, v){
      $(this).prop('disabled', false);
      list = {
        'id': $(v).attr('id'),
        'value': $(v).val() 
      };
      campany_profile_data.push(list);
    });
    $('.company_profile-form input:first').prop('disabled', true);
    $(this).addClass('hidden');
    $('.cancel_company_profile').removeClass('hidden');
    $('.save_company_profile').removeClass('hidden');
  });
  $(document).on('click', '.cancel_company_profile', function(){
    $.each(campany_profile_data, function(k, v){
      $('#'+v['id'], document).val(v['value']);
    });
    $('.company_profile-form input').each(function(k, v){
      $(this).prop('disabled', true);
    });
    $(this).addClass('hidden');
    $('.save_company_profile').addClass('hidden');
    $('.edit_company_profile').removeClass('hidden');
  });
  $(document).on('click', '.test-btn', function(){
    $('.accordion-menu-wrapper').css('max-width', '5%');
    $('.accordion-menu').css('display', 'none');
    $('.main-content').css('max-width', '95%').css('flex', '0 0 95%');
  });
  $('#datepicker', document).datepicker({
    minDate: +1,
    dateFormat: 'yy-mm-dd',
    numberOfMonths: 1,
    showButtonPanel: true,
    closeText: 'Clear'
  });
  $(document).on('click', '.ui-datepicker-close', function(){
    $('#datepicker', document).val('');
  });
  $(document).on('click', '.tab_menu_btn', function(){
    var tab_content = $(this).attr('tab-content');
    tab_menu_show(tab_content);
  });
  $(document).on('click', '.submit_announcement', function(){
    var num = 0;
    $('.input-error').hide();
    $('.tab_menu_content_wrapper .check_announcement_value', document).each(function(){
      if($(this).val() == ''){
        if(num == 0){
          var tab_content = $(this).attr('tab-content');
          tab_menu_show(tab_content);
        }
        $(this).next().next().text(input_required_text);
        $(this).next().next().show();
        alertMessage(check_required_message, 0, "", 1500);
        num++;
      }
    });
    if (num == 0){
      var obj = $(".system_announcement-form");
      ajax_data_loader(obj);      
    } 
  });
  $(document).on('change', '#csv_product_error', function(){
    var file_data = {
      'file_picker': this,
      'file_image': '.custom-file-label-1',
      'file_name': '.custom-file-label-1',
      'default_image': 'url("../image/icon-upload.svg")',
      'default_name': unselected_file,
      'confirm_image': 'url("../image/icon-success.svg")'
    };
    change_csv_file_data_loader(file_data);
  });
  $(document).on('change', '#csv_images_error', function(){
    var file_data = {
      'file_picker': this,
      'file_image': '.custom-file-label-1',
      'file_name': '.custom-file-label-1',
      'default_image': 'url("../image/icon-upload.svg")',
      'default_name': unselected_file,
      'confirm_success_image': 'url("../image/icon-success.svg")'
    };
    change_csv_file_data_loader(file_data);
  });
  // datepicker-search
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
  $(document).on('click', '.datepicker', function(){
    var clear_input = $(this).attr('id');
    $('.ui-datepicker-close').attr('clear-input', '');
    $('.ui-datepicker-close').attr('clear-input', '#'+clear_input);
  });
  $(document).on('click', '.ui-datepicker-close', function(){
    var clear_input = $('.ui-datepicker-close').attr('clear-input');
    var clear_input_wrapper = $(clear_input).parents().parents().attr('id');
    inputStatusClear('#'+clear_input_wrapper+' .datepicker');
    inputMessage('#'+clear_input_wrapper+' .input-error', 0, '');
    $(clear_input, document).val('');
  });
  // csv
  $(document).on('change', '.custom-file-input', function(){
    var data = {
      'multiple': 0,
      'file_picker': this,
      'default_name': unselected_file
    };
    show_selected_file_name_data_loader(data);
  });
  $("#tabs", document).tabs();
});