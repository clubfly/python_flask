/***************************************
 *--    Templates Main Javascript    --*
 ***************************************/
$(function(){
  history.pushState(null, null, document.URL);
  window.addEventListener('popstate', function () {
    history.pushState(null, null, document.URL);
  });
  $(document).on("click",".change_language",function(){
    var language = $(this).attr("language");
    var api = language_api + language
    $.get(api, function(result){
      console.log(result["code"])
      if (parseInt(result["code"]) == 1) {
          location.reload();
      }
    });
  });
  // tooltip
  var toggleTemplate = '<div class="tooltip" role="tooltip">'+
                        '<div class="arrow"></div>'+
                        '<div class="tooltip-inner"></div>'+
                       '</div>';
  $(document).on("mouseover",'[data-toggle="tooltip"]',function(){
    $(this).append(toggleTemplate);
    $('.tooltip-inner').html($(this).attr('data-title'));
    var placement = $(this).attr('data-placement');
    $('.tooltip').addClass('tooltip-'+placement);
    $('.tooltip').addClass('bs-tooltip-'+placement);
    tooltip(this);
    $('.tooltip').addClass('show');
  });
  $(document).on("mouseout",'[data-toggle="tooltip"]',function(){
    $('.tooltip').remove();
  });
  // input-with-icon
  $(document).on('focus', '.input-with-icon', function(){
    $(this).attr('placeholder', '');
  });
  $(document).on('blur', '.input-with-icon', function(){
    $(this).attr('placeholder', $(this).next('.input-label').html());
  });
  // dropdown
  const $menu = $('.dropdown-toggle').parent();
  $(document).on('mouseup', function(e){
    if (!$menu.is(e.target) // if the target of the click isn't the container...
    && $menu.has(e.target).length === 0) // ... nor a descendant of the container
    {
      $('.dropdown-toggle').attr('aria-expanded', 'false');
      $menu.removeClass('show');
      $('.dropdown-menu').hide();
    }
  });
  $(document).on('click', '.dropdown-toggle', function(e){
    if($(this).attr('aria-expanded') == 'false'){
      $('.dropdown-toggle').attr('aria-expanded', 'false');
      $('.dropdown-toggle').parent().removeClass('show');
      $('.dropdown-menu').hide();
    }
    $(this).attr('aria-expanded', function(index, attr){
      return attr == 'false' ? 'true' : 'false';
    });
    $(this).parent().toggleClass('show');
    $(this).next().toggle();
  });
  $(document).on('click', '.dropdown-btn', function(){
    if($(this).attr('aria-expanded') == 'false'){
      $('.dropdown-toggle').attr('aria-expanded', 'false');
      $('.dropdown-toggle').parent().removeClass('show');
      $('.dropdown-menu').hide();
    }
    $(this).attr('aria-expanded', function(index, attr){
      return attr == 'false' ? 'true' : 'false';
    });
    $(this).toggleClass('show');
    $('.dropdown-menu', this).toggle();
  });
  // modal
  $(document).on('click', '[data-toggle="modal"]', function(){
    var modalTemplate = '<div class="modal-backdrop fade show"></div>';
    var modal = $(this).attr('data-target');
    var modalTitle = $(this).attr('data-whatever');
    if(modal != undefined && modal != ''){
      $('.modal-backdrop').remove();
      $('body').addClass('modal-open').append(modalTemplate);
      $(modal).addClass('show').removeClass('hidden').slideDown(300);
      if(modalTitle != undefined && modalTitle != ''){
        $('.modal-title').html(modalTitle);
      }
    }
  });
  $(document).on('click', '.modal .close', function(){
    modalClose();
  });
  $(document).on('click', '.modal .cancel', function(){
    modalClose();
  });
  // multiple select
  $(document).on('click', '.multiple-select', function(){
    var multipleArray = [];
    $('.dropdown-menu .dropdown-input-group input[type="checkbox"]', this).each(function(){
      if($(this).is(':checked')){
        multipleArray.push($(this).val());
      }
    });
    $('.multiple_value', this).val(multipleArray);
    if(multipleArray != ''){
      $('.dropdown-toggle', this).text(multipleArray.join());
      if(multipleArray.length > 4){
        $('.dropdown-toggle', this).text('Select '+ multipleArray.length +' Values');
      }
    }else{
      $('.dropdown-toggle', this).text('Category');
    }
  });
});
function tooltip(element){
  var tooltip = $(element).find('.tooltip').position();
  var obj = {
    'top': function(p, w, h){
      return [parseInt(p.top) - parseInt(h), parseInt(p.left) - parseInt($('.tooltip .tooltip-inner').width()/5)];
    },
    'right': function(p, w, h){
      return [parseInt(p.top), parseInt(p.left) + parseInt(w + 5)];
    },
    'bottom': function(p, w, h){
      return [parseInt(p.top) + parseInt(h), parseInt(tooltip.left - ($(element).find('.tooltip').outerWidth()/2) + (w/4))];
    },
    'left': function(p, w, h){
      return [parseInt(p.top), parseInt(p.left) - parseInt(w)];
    }
  };
  $.each(obj, function(k, v){
    $('.tooltip-'+k).each(function(){
      var position = $(element).position();
      var width = $(element).outerWidth();
      var height = $(element).outerHeight();
      $('.tooltip-'+k).css('top', v(position, width, height)[0]).css('left', v(position, width, height)[1]);
    });
  });
}
