/***************************
 *--    Ready Functin    --*
 ***************************/
$(function(){
  // login enter
  $("form input").keypress(function (e) {
    if ((e.which && e.which == 13) || (e.keyCode && e.keyCode == 13)) {
      $('.longin-btn').click();
      return false;
    }
  });
  $('.longin-btn').click(function(){
      // Check Account Value
      var form_type = $(this).parents().attr('id');
      check_value(form_type);
  });
});
/******************************
 *--    Non-API Function    --*
 ******************************/
function check_value(form_type) {
  //default init value
  var obj_login = {
      "user" : {
          "account" : {
              "input_values" : ".account",
              "check_input_values" : {
                'required':{
                  "rule": required,
                  "error-message": LANG.error_account_required_text,
                },
              },
          },
          "password" : {
              "input_values" : ".password",
              "check_input_values" : {
                'required':{
                  "rule": required,
                  "error-message": LANG.error_password_required_text,
                },
              },
          }
      }
  }
  var check_item = 0;
  $.each(obj_login[form_type], function(key, value){
    if(value['check_input_values']['required']['rule'] != ""){
      if(value['check_input_values']['required']['rule']($("#"+form_type+" "+value["input_values"]).val())){
        render_input_status(key, true, '');
        check_item++;
      }else{
        render_input_status(key, false, value['check_input_values']['required']["error-message"]);
        return;
      }
    }
  });
  if (check_item === 2){
    $("#"+form_type).submit();
  }
}
function render_input_status(input, status, message){
  $('.'+input).addClass('is-invalid');
  $('.'+input).next().next().html(message);
  $('.'+input).next().next().show();
  if(status){
    $('.'+input).removeClass('is-invalid');
    $('.'+input).next().next().html('');
    $('.'+input).next().next().hide();
  }
}
// check-item
function required(str){
  if(str === undefined || str === ""){
    return false;
  }else{
    return true;
  }
}