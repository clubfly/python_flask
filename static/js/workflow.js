function accordion_menu_data_loader(data){
  accordionMenuDefault(data);
}
function modal_data_loader(data){
  if(data['display'] == 0) {
    modalClose();
  }
  if(data['display'] == 1) {
    modalShow(data);
  }
}
function modal_sop_img_data_loader(data){
  if(data['display'] == 0) {
    modalClose();
  }
  if(data['display'] == 1) {
    modalSopImgShow(data);
  }
}
function alert_message_data_loader(data) {
  if(data['display'] == 0) {
    alertMessageClose();
  }
  if(data['display'] == 1) {
    alertMessage(data.message, data.status, data.ajaxStatus, data.seconds);
  }
};
function input_status_data_loader(data) {
  inputStatus(data['element'], data['status']);
}
function input_message_data_loader(data){
  inputMessage(data['element'], data['status'], data['message']);
}
function switch_status_data_loader(data) {
  switchStatus(data);
}
function webcam_data_loader(data) {
  if(data['display'] == 0) {
    captureVideoButtons(data);
  }
  if(data['display'] == 1) {
    handleStop(data);
  }
}
function change_file_data_loader(data) {
  if(data['display'] == 0) {
    clearReadFile(data);
  }
  if(data['display'] == 1) {
    if(data['multiple'] == 0) {
      readFileURL(data);
      readFileName(data);
    }
    if(data['multiple'] == 1) {
      readFilesURL(data)
      readFilesNumber(data);
    }
  }
}
function select_checkbox_data_loader(data) {
    if(data['select_all'] == 0){
      selectCheckboxAllStatus(data);
    }
    if(data['select_all'] == 1){
      selectCheckboxAll(data);
    }
    toolbarButtonStatus(data);
}
function validation_data_loader(data) {
  if(data['display'] == 1) {
    $.each(data['required'], function(key, value){
     console.log($(value).val());
    });
  }
}
function modal_second_show_data_loader(data){
  modalSecondShow(data);
}
function datepicker_check_date_data_loader(element, data){
  if($(element).hasClass('start_date')){
    datepicker_check_date(element, 0, data);
  }
  if($(element).hasClass('end_date')){
    datepicker_check_date(element, 1, data);
  }
}
function show_selected_file_name_data_loader(data){
  show_selected_file_name(data);
}