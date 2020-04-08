/*****************************
 *--    Webcam Settings    --*
 *****************************/
var captureVideoButton = document.querySelector('#capture-button');
var screenshotButton = document.querySelector('.screenshot-button');
var img = document.querySelector('#source-img');
var video = document.querySelector('#videostream video');
var canvas = document.createElement('canvas');
// Open Webcam
var video_setting = {
  '1': [1280, 720],
  '2': [1920, 1080],
  '3': [2592, 1944],
};
function captureVideoButtons(){
  var videoW = 1280;
  var videoH = 720;
  $.each(video_setting, function(key, size){
    if(videoSet == key){
      videoW = size[0];
      videoH = size[1];
    }else{
      videoW = videoW;
      videoH = videoH;
    }
  });
  const constraints = {
    video: true,
    video: {
      width: {
        ideal: videoW
      },
      height: {
        ideal: videoH
      }
    }
  };
  navigator.mediaDevices.getUserMedia(constraints).then(handleSuccess).catch(handleError);
};
function handleSuccess(stream) {
  $('.screenshot-button').prop('disabled', false);
  video.srcObject = stream;
  setTimeout(() => {
    if($(window).width() === 1080 && $('#videostream').outerHeight() > 579){
      $('.left-flex-height').css('height', '52vh');
      $('.right-flex-height').css('height', '44vh');
      $('.outer-frame-overflow-y').css('flex', '3.5 1 0%');
      $('.outer-frame-position-r').css('flex', '0.5 1 0%');
    }
  }, 2000);
};
function handleError(error) {
  console.error('Error: ', error);
};
// screenshot
function screenshot(){
	canvas.width = video.videoWidth;
	canvas.height = video.videoHeight;
  canvas.getContext('2d').drawImage(video, 0, 0);
  img.src = canvas.toDataURL('image/jpeg');
  // API
  if(api["screenshot"].domain === ''){
    api["screenshot"].domain = api_host;
  }
  var url = api["screenshot"].domain + api["screenshot"].url;
  var method = api["screenshot"].method;
  var data = {"image": canvas.toDataURL('image/jpeg'),};
  send_product_data(url, method, data, resultFunction);
};
/***************************
 *--    AJAX Function    --*
 ***************************/
function send_product_data(url, method, data, callback_function){
  // api mock product data
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
        "product_id": 1,
        "name": "ベリーウォールナットパン",
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
        render_message('messages-wrapper', 'messages', data.statusText, 400);
        render_message_status('messages-wrapper', 0);
        alertMessage(data.statusText, 0, data.status);
        $('.screenshot-button').addClass('hide hidden');
        $('.re-checkout').removeClass('hide hidden');
      }
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
            callback_function(data['data']['checkout'][0]['instance']);
          }else{
            console.log(data);
            render_message('messages-wrapper', 'messages', data['message'], 400);
            render_message_status('messages-wrapper', 0);
            alertMessage(data['message'], 0, '');
            $('.screenshot-button').addClass('hide hidden');
            $('.re-checkout').removeClass('hide hidden'); 
          }
        }
      }
    },
  });
};
/*****************************
 *--    API UI Function    --*
 *****************************/
function resultFunction(data){
  organizeData(data);
  processingData(data);
  qrcode(data);
  printList(data);
  $('.screenshot-button').addClass('hide hidden');
  $('.re-checkout').removeClass('hide hidden');
  $('.confirm-checkout').removeClass('hide hidden');
  $('.mock-confirm-checkout').removeClass('hide hidden');
  $('.print').removeClass('hide hidden');
  $(window).resize(function(){
    $('.rect').remove();
    processingData(data);
  });
};
function organizeData(data){
  // 1.確認需要提示的錯誤擺放的id
  // 2.和resultData比對product_id
  // 3.product_id無錯誤擺放的id就加入新的物件
  if(backOfProductId === 1){
    $.each(data, function(key, value){
      if(typeof(value['product_id']) != 'undefined'){
        backOfProductIdArray.forEach(element => {
          if(parseInt(value['product_id']) === parseInt(element)){
            $('.confirm-checkout').hide();
            $('.mock-confirm-checkout').hide();
            $('.print').hide();
            data.splice(key, 1);
            data.unshift({
              "bounding_box": {
                "h": value["bounding_box"]["h"],
                "w": value["bounding_box"]["w"],
                "x": value["bounding_box"]["x"],
                "y": value["bounding_box"]["y"]
              },
              "product_id": value['product_id'],
              "name": value['name'],
              "price": value['price'],
              "score": value['score'],
              "thumbnail": value['thumbnail'],
              "symbol": value['symbol'],
            });
          }
        });
      }
    });
  }
  productList(data);
};
function productList(organizeData){
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
    if(typeof(value['product_id']) != 'undefined'){
      prod_id = value['product_id'];
    }
    if(typeof(value['symbol']) != 'undefined' && rewrite === 0){
      // config 的 useSymbol 設定為 0 使用模型symbol, 設定為 1 為使用樣板symbol
      if(useSymbol === 0){
        symbol = value['symbol'];
        rewrite++;
      }
    }
    if(typeof(value['price']) != 'undefined'){
      prod_price = value['price'];
    }
    totalPrice += parseFloat(prod_price);
    if(value['thumbnail'] === '' || value['thumbnail'] === undefined){
      var html =  '<li class="row outer-frame-border list-'+prod_id+'" data-key="'+prod_id+'" onclick="addSelectedList(this)">'+
                    '<div class="col-7 layout-6-5 padding-0">'+
                      '<h3 class="sku-name-style name">'+value['name']+'</h3>'+
                    '</div>'+
                    '<div class="col-2 layout-1 padding-0 ta-r">'+
                      '<span class="num">x '+1+'</span><br>'+
                    '</div>'+
                    '<div class="col-3 layout-2-5 padding-0 ta-r">'+
                      '<span class="sku-price-style symbol">'+symbol+' '+'</span>'+
                      '<span class="sku-price-style price">'+prod_price+'</span>'+
                    '</div>'+
                  '</li>';
    }else{
      var html =  '<li class="row outer-frame-border list-'+prod_id+'" data-key="'+prod_id+'" onclick="addSelectedList(this)">'+
                    '<div class="col-3 layout-2-5 padding-0">'+
                      '<img src="'+value['thumbnail']+'" class="sku-image-style"/>'+
                    '</div>'+
                    '<div class="col-6 layout-5 padding-0">'+
                      '<h3 class="sku-name-style name">'+value['name']+'</h3>'+
                    '</div>'+
                    '<div class="col-3 layout-2-5 padding-0 ta-r">'+
                      '<span class="num">x '+1+'</span><br>'+
                      '<span class="sku-price-style symbol">'+symbol+' '+'</span>'+
                      '<span class="sku-price-style price">'+prod_price+'</span>'+
                    '</div>'+
                  '</li>';
    }
    $('.outer-frame-overflow-y').append(html);
    $('.total-num').html('x '+parseInt(num));
    $('.total').html(symbol+' '+parseFloat(totalPrice).toFixed(2));
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
};
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
function processingData(data){
  // 處理回傳Data的畫框資訊
  var currentWidth = document.getElementById('source-img').width;
  var currentHeight = document.getElementById('source-img').height;
  var originalWidth = document.getElementById('source-img').naturalWidth;
  var originalHeight = document.getElementById('source-img').naturalHeight;
  var initWidthSize = parseFloat(currentWidth/originalWidth).toFixed(2);
  var initHeightSize = parseFloat(currentHeight/originalHeight).toFixed(2);
  var num = 0;
  $.each(data, function(key, value){
    num++;
    var prod_id = 'Nan_id_'+num;
    if(typeof(value['product_id']) != 'undefined'){
      prod_id = value['product_id'];
    }
    if(isFloat(value['bounding_box']['x'])){
      var x1 = parseFloat(value['bounding_box']['x']*currentWidth).toFixed(4);
          x1 = (currentWidth-parseFloat(currentWidth))/2+parseFloat(x1);
      var y1 = parseFloat(value['bounding_box']['y']*currentHeight).toFixed(4);
      var w = parseFloat(currentWidth*value['bounding_box']['w']).toFixed(4);
      var h = parseFloat(currentHeight*value['bounding_box']['h']).toFixed(4);
    }else{
      var x1 = parseInt(value['bounding_box']['x']*initWidthSize);
      var y1 = parseInt(value['bounding_box']['y']*initHeightSize);
      var w = parseInt(value['bounding_box']['w']*initWidthSize);
      var h = parseInt(value['bounding_box']['h']*initHeightSize);
    }
    boundingBox(prod_id, x1, y1, w, h);
  });
};
function isFloat(n){
  // 判斷是否為浮點數
  return n % 1 !== 0;
};
function boundingBox(num, x1, y1, w, h){
  // 畫bounding box
  if($('.outer-frame-overflow-y li').size() != 0){
    var html = '<div class="rect rect-'+num+'" data-key="'+num+'" onclick="addSelectedRect(this)" style="left:'+x1+'px; top:'+y1+'px; width:'+w+'px; height:'+h+'px;"></div>';
    $('#videostream').append(html);
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
function qrcode(data){
  // 顯示qrcode
  var product_item = [];
  var total = 0;
  var num = 0;
  $.each(data, function(key, value){
    num++;
    var prod_id = 'Nan_id_'+num;
    if(typeof(value['product_id']) != 'undefined'){
      prod_id = value['product_id'];
    }
    total += value['price'];
    product_item.push({'product_id': prod_id, 'product_name': value['name'], 'num': parseInt($('.list-'+prod_id+' .num').html().replace('x ', '')), 'unit_price': value['price'], 'subtotal': parseInt($('.list-'+prod_id+' .subtotal').html())});
  });
  var qrcodeChl = JSON.stringify({'total_price': total, 'product_item': removeDuplicates(product_item, 'product_id')});
  var qrcode = 'https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl='+qrcodeChl;
  $('.qrcode-img').attr('src', qrcode);
};
function removeDuplicates(originalArray, prop) {
  var newArray = [];
  var lookupObject  = {};
  for(var i in originalArray) {
    lookupObject[originalArray[i][prop]] = originalArray[i];
  }
  for(i in lookupObject) {
    newArray.push(lookupObject[i]);
  }
  return newArray;
};
function printList(data){
  var array = [];
  var num = 0;
  $.each(data, function(key, value){
    num++;
    var prod_id = 'Nan_id_'+num;
    if(typeof(value['product_id']) != 'undefined'){
      prod_id = value['product_id'];
    }
    array.push(prod_id);
  });
  // 加入商品列表
  var newArray1 = [];
  for(var i = 0; i < array.length; i++){
    if(newArray1.indexOf(array[i]) === -1){
      newArray1.push(array[i]);
      var html =  '<li>'+
                    '<div class="row">'+
                      '<span class="col-7 layout-6 padding-0">'+$('.list-'+array[i]+' .name').html()+'</span>'+
                      '<span class="col-2 layout-1 padding-0 ta-r">'+$('.list-'+array[i]+' .num').html()+'</span>'+
                      '<span class="col-3 layout-3 padding-0 ta-r">'+$('.list-'+array[i]+' .symbol').html()+$('.list-'+array[i]+' .price').html()+'</span>'+
                    '</div>'+
                  '</li>';
      $('.shopping-list').append(html);
    }
  }
  // 顯示當前年月日時分
  var today = new Date();
  var currentDateTime = today.getFullYear()+'/'+(today.getMonth()+1)+'/'+today.getDate()+' '+today.getHours()+':'+today.getMinutes();
  $('.date').html(currentDateTime);
};
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
var time;
function startTimeout(){
  time = setTimeout(function(){
    try {
      // bootstrap
      $('#modalICcard').modal('hide');
      $('#modalQRcode').modal('hide');
      $('#modalSuccess').modal('show');
    } catch (error) {
      // not bootstrap
      $('#modalICcard').removeClass('show').addClass('hidden');
      $('#modalQRcode').removeClass('show').addClass('hidden');
      $('.modal-backdrop').remove();
      $('body').removeClass('modal-open');
      $('#modalSuccess').addClass('show').removeClass('hidden'); 
    }
  }, 5000);
};
function stopTimeout()	{
  clearTimeout(time);
};
function render_message(msg_wrapper, msg_tsxt, msg, millisecond){
  $('.'+msg_tsxt).html(msg);
  $('.'+msg_wrapper).fadeIn(millisecond);
}
function render_message_status(msg_wrapper, status){
  $('.'+msg_wrapper).removeClass('is-valid');
  $('.'+msg_wrapper).removeClass('is-invalid');
  if(status){
    $('.'+msg_wrapper).addClass('is-valid');
  }else{
    $('.'+msg_wrapper).addClass('is-invalid');
  }
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
var startSetTimeout;
function serverSetTimeout(){
  startSetTimeout = setTimeout(() => {
    if(websocketReadyState === 1){
      // 開通後等待10秒, 未回傳訊息, 顯示『尚未感應到卡片, 請再嘗試!』
      render_message('messages-wrapper', 'messages', 'Try the card again.', 400);
      render_message_status('messages-wrapper', 0);
      alertMessage('Try the card again.', 0, '');
    }else if(websocketReadyState === 3){
      // 未開通等待10秒, 顯示『伺服器連接關閉, 請重啟伺服器!』
      render_message('messages-wrapper', 'messages', 'Websocket server is off.', 400);
      render_message_status('messages-wrapper', 0);
      alertMessage('Websocket server is off.', 0, '');
    }
  }, 10000);
};
var websocketReadyState = 0;
function startWebsocket(action, device, data, fn, errMessage){
  if ("WebSocket" in window) {
    var wsc = new WebSocket(wsc_url);
    wsc.onopen = function() {
      console.log("websocket open");
      websocketReadyState = 1;
      $('.messages-wrapper').hide();
      $('.alert').fadeOut();
      // websocket連接成功, send data
      wsc.send(JSON.stringify({action: action, device: device, data: data}));
    };
    wsc.onmessage = function(message) {
      console.log(message);
      websocketReadyState = 2;
      // 接收websocket的message, 顯示成功頁面或訊息
      var data = JSON.parse(message.data);
      if(data.code == '0000'){
        clearTimeout(startSetTimeout);
        if(fn === 'checkout'){
          setTimeout(() => {
            try {
              // bootstrap
              $('#modalQRcode').modal('hide');
              $('#modalICcard').modal('hide');
              $('#modalSuccess').modal('show');
              $('.messages-wrapper').hide();
            } catch (error) {
              // not bootstrap
              $('#modalQRcode').removeClass('show').addClass('hidden');
              $('#modalICcard').removeClass('show').addClass('hidden');
              $('#modalSuccess').addClass('show').removeClass('hidden');
              $('.alert').fadeOut(); 
            }
          }, 1300);
        }else{
          setTimeout(() => {
            render_message('messages-wrapper', 'messages', '列印成功!', 400);
            render_message_status('messages-wrapper', 1);
            alertMessage('列印成功!', 1);
          }, 1300);
        }
      }
    };
    wsc.onclose = function() {
      console.log("websocket closed");
      websocketReadyState = 3;
    };
    wsc.onerror = function(e) {
      console.log(e);
      websocketReadyState = 4;
      // websocket連接失敗, 顯示錯誤訊息
      render_message('messages-wrapper', 'messages', errMessage, 400);
      render_message_status('messages-wrapper', 0);
      alertMessage(errMessage, 0, '');
    };
    if(fn === 'checkout'){
      serverSetTimeout();
    }
  }
};
/***************************
 *--    Ready Functin    --*
 ***************************/
$(function(){
  // websocket button = 1 (show), mock confirm checkout button = 0 (hide)
  if(confirmCheckoutBtn == 1){
    mockConfirmCheckoutBtn = 0;
  }
  if(mockConfirmCheckoutBtn == 1){
    $('.iccard').addClass('mock-iccard');
    $('.mock-iccard').removeClass('iccard');
    $('.qrcode').addClass('mock-qrcode');
    $('.mock-qrcode').removeClass('qrcode');
  }
  var show_btn = {
    'button1': [confirmCheckoutBtn, '.confirm-checkout'],
    'button2': [mockConfirmCheckoutBtn, '.mock-confirm-checkout'],
    'button3': [printBtn, '.print'],
    'button4': [iccardBtn, '.iccard'],
    'button5': [qrcodeBtn, '.qrcode'],
    'button6': [iccardBtn, '.mock-iccard'],
    'button7': [qrcodeBtn, '.mock-qrcode'],
  }
  // 按鈕設定不等於 1 隱藏
  $.each(show_btn, function(key, button){
    if(button[0] != 1){
      $(button[1]).hide();
    }
  });
  // 開啟Webcam
  captureVideoButtons();
  // 使用Webcam
  $('.screenshot-button').click(function(){
    $('.messages-wrapper').hide();
    $('.alert').fadeOut();
    screenshot();
  });
  // 隱藏訊息框
  $('.alert .close').click(function(){
    $('.alert').fadeOut();
  });
  $('.link-hide').click(function(){
    $('.messages-wrapper').hide();
    $('.alert').fadeOut();
  });
  // websocket模擬結帳
  // $('.confirm-checkout').click(function(){
  //   // startWebsocket( action, device, data, function, error message );
  //   // Action: {identify, payment, print}
  //   // Device: {scanner, reader, printer} 
  //   $('.messages-wrapper').hide();
  //   $('.alert').fadeOut();
  //   startWebsocket('payment', 'reader', '', 'checkout', 'Websocket server is off.');
  // });
  // websocket模擬結帳(有選擇付款方式時使用)
  $('.iccard').click(function(){
    // startWebsocket( action, device, data, function, error message );
    // Action: {identify, payment, print}
    // Device: {scanner, reader, printer}
    try {
      // bootstrap
      $('.messages-wrapper').hide();
      $('#exampleModalCenter').modal('hide');
    } catch (error) {
      // not bootstrap
      $('.alert').fadeOut();
      $('#exampleModalCenter').removeClass('show').addClass('hidden');
    }
    startWebsocket('payment', 'reader', '', 'checkout', 'Websocket server is off.');
  });
  // qrcode模擬結帳(有選擇付款方式時使用)
  $('.qrcode').click(function(){
    try {
      // bootstrap
      $('.messages-wrapper').hide();
      $('#exampleModalCenter').modal('hide');
    } catch (error) {
      // not bootstrap
      $('.alert').fadeOut();
      $('#exampleModalCenter').removeClass('show').addClass('hidden');
      $('#confirm-input').focus(); 
    }
  });
  $('#modalQRcode').on('shown.bs.modal', function () {
    $('#confirm-input').focus();
  });
  $('#confirm-input').on('keyup', function(){
    if($(this).val() != ''){
      try {
        // bootstrap
        $('#modalQRcode').modal('hide');
        $('#modalSuccess').modal('show');
      } catch (error) {
        // not bootstrap
        $('#modalQRcode').removeClass('show').addClass('hidden');
        $('#modalSuccess').addClass('show').removeClass('hidden').slideDown(300);
      }
    }
  });
  // websocket列印
  $('#websocket-print').click(function(){
    $('.messages-wrapper').hide();
    $('.alert').fadeOut();
    html2canvas(document.querySelector("#print-wrapper")).then(canvas => {
      var image = canvas.toDataURL('image/jpeg');
      // startWebsocket( action, device, data, function, error message );
      // Action: {identify, payment, print}
      // Device: {scanner, reader, printer} 
      startWebsocket('print', 'printer', image.replace(/data:image\/.*;base64,/,''), 'print', 'Websocket server is off.');
    });
  });
  // 拍攝模擬結帳5秒跳選成功 iccard / qrcode
  $('.mock-iccard').click(function(){
    try {
      // bootstrap
      $('.messages-wrapper').hide();
      $('#exampleModalCenter').modal('hide');
    } catch (error) {
      // not bootstrap
      $('.alert').fadeOut();
      $('#exampleModalCenter').removeClass('show').addClass('hidden'); 
    }
    startTimeout();
  });
  $('.mock-qrcode').click(function(){
    try {
      // bootstrap
      $('.messages-wrapper').hide();
      $('#exampleModalCenter').modal('hide');
    } catch (error) {
      // not bootstrap
      $('.alert').fadeOut();
      $('#exampleModalCenter').removeClass('show').addClass('hidden');
    }
    startTimeout();
  });
  $('#modalICcard').click(function(){
    clearTimeout(startSetTimeout);
    $('.messages-wrapper').hide();
    $('.alert').fadeOut();
  });
  $('#modalICcard .close').click(function(){
    clearTimeout(startSetTimeout);
    $('.messages-wrapper').hide();
    $('.alert').fadeOut();
    if(mockConfirmCheckoutBtn == 1){
      try {
        // bootstrap
        $('#exampleModalCenter').modal('show');
      } catch (error) {
        // not bootstrap
        $('#exampleModalCenter').removeClass('show').addClass('hidden');
      }
      stopTimeout();
    }
  });
  $('#modalQRcode').click(function(){
    clearTimeout(startSetTimeout);
    $('.messages-wrapper').hide();
    $('.alert').fadeOut();
  });
  $('#modalQRcode .close').click(function(){
    clearTimeout(startSetTimeout);
    $('.messages-wrapper').hide();
    $('.alert').fadeOut();
    if(mockConfirmCheckoutBtn == 1){
      try {
        // bootstrap
        $('#exampleModalCenter').modal('show');
      } catch (error) {
        // not bootstrap
        $('#exampleModalCenter').removeClass('show').addClass('hidden'); 
      }
      stopTimeout();
    }
  });
});
