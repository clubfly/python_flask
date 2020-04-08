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
  // canvas.getContext('2d').drawImage(video, 0, 0);
  // img.src = canvas.toDataURL('image/jpeg');
  var canvasContext = canvas.getContext('2d');
  canvasContext.translate(canvas.width, 0);
  canvasContext.scale(-1, 1);
  canvasContext.drawImage(video, 0, 0);
  // API
  // if(api["screenshot"].domain === ''){
  //   api["screenshot"].domain = api_host;
  // }
  // var url = api["screenshot"].domain + api["screenshot"].url;
  // var method = api["screenshot"].method;
  // var data = {"image": canvas.toDataURL('image/jpeg'),};
  // send_product_data(url, method, data, resultFunction);
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
          "y": 315,
        },
        "contour": [[431,225,451,285,391,285,431,225],[451,285,451,235,341,235,451,285]],
        "product_id": 1,
        "name": "CJ_003",
        "price": 1,
        "score": 0,
        "thumbnail": "/static/image/test-1.jpeg",
        "symbol": "¥",
      },
      {
        "bounding_box": {
          "h": 132,
          "w": 116,
          "x": 613,
          "y": 165,
        },
        "contour": [[420,196,340,109,310,109,420,196]],
        "product_id": 2,
        "name": "CJ_004",
        "price": 2,
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
            callback_function(data['data']);
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
/***************************
 *--    Ready Functin    --*
 ***************************/
$(function(){
  // 開啟Webcam
  captureVideoButtons();
  // 使用Webcam
  $('.face-rect').click(function(){
    screenshot();
  });
  // 隱藏訊息框
  $('.alert .close').click(function(){
    $('.alert').fadeOut();
  });
});