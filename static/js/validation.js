/********************************
 *--    Validation Functin    --*
 ********************************/

var required = function(str){
  // 檢查必填
  if(str === undefined || str === ''){
    return false;
  }else{
    return true;
  }
}

var email = function(str){
  // 檢查email格式
  rule = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z]+$/;
  if(!str.match(rule)) {
    return false;
  }
  return true;
}

var is_number = function(str){
  rule = /^[0-9]+$/;
  if(!str.match(rule) && str != '') {
    return false;
  }
  return true;
}

var is_english_number = function(str){
  rule = /^[A-Za-z0-9]+$/;
  if(!str.match(rule) && str != '') {
    return false;
  }
  return true;
}

var same_value = function(){
  // 檢查input value值相同
  var str1;
  var str2;
  $('.same_value').each(function(){
    if($(this).attr('check-same') == 1){
      str1 = $(this).val();
    }else{
      str2 = $(this).val();
    }
  });
  if(str1 != str2){
    return false;
  }else{
    return true;
  }
}

var different_value = function(){
  // 檢查input value值不同
  var str1;
  var str2;
  $('.different_value').each(function(){
    if($(this).attr('check-different') == 1){
      str1 = $(this).val();
    }else{
      str2 = $(this).val();
    }
  });
  console.log(str1);
  if(str1 == str2){
    return false;
  }else{
    return true;
  }
}

function string_length(str){ 
  // 檢查字串的長度是否符合限制的長度
  var rule = str.match(/[^ -~]/g);
  var strLength = str.length + (rule ? rule.length : 0);
  var limitLength = 0;
  $('.string_length').each(function(){
    limitLength = $(this).attr('check-length');
  });
  if(parseInt(strLength) < 0 || parseInt(strLength) > parseInt(limitLength)){
    return false;
  }else{
    return true;
  }
}