<nav class="m-b-15 recognition-methods-button">
  <h2 class="title m-r-15">{{data["add_system_announcement_text"]}}</h2>
  <button type="button" 
          class="btn btn-primary block-tooltip back_system_announcement"
          data_sn="0"
          tab_sn="{{data["system_announcement_tab"]}}"
          page_sn="{{data["pages"]}}"
          ajax_url="{{data["system_announcement_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_system_announcement_text"]}}</span>
  </button>
</nav>
<div>
  <form method="post" class="system_announcement-form" 
        action="{{data["upd_system_announcement_url"]}}" 
        tab_sn="{{data["system_announcement_tab"]}}">
    <div class="layout-style-1 padding-15">
      <ul class="tab_menu_button_wrapper">
        {% for k,v in data["language_support"].items() %}
        <li class="tab_menu_btn tab_menu_{{k}}" tab-content="{{k}}">{{v["name"]}}</li>
        {% endfor %}
      </ul>
      <ul class="tab_menu_content_wrapper">
        {% for k,v in data["language_support"].items() %}
        <li class="tab_menu_content" id="tab_menu_content_{{k}}">
          <div class="form-input-group">
            <input type="text" name="title[{{k}}]" 
                   class="check_announcement_value" 
                   tab-content="{{k}}"
                   value="{{data["announcement_list"][k]["titles"]}}" />
            <label class="input-label">{{data["system_announcement_title_text"]}}</label>
            <span class="danger input-error"></span>
          </div>
          <div class="form-input-group height-unset">
            <textarea rows="8" cols="50" 
                      name="contents[{{k}}]" 
                      class="check_announcement_value" 
                      tab-content="{{k}}">{{data["announcement_list"][k]["contents"]}}</textarea>
            <label class="input-label">{{data["menu_system_announcement_text"]}}</label>
            <span class="danger input-error"></span>
          </div>
          <input type="hidden" name="languages" value="{{k}}" />
        </li>
        {% endfor %}
      </ul>
      <div class="row">
        <div class="form-input-group layout-2 p-l-0 m-b-5">
          <input type="hidden" name="board_hash" value="{{data["board_hash"]}}" />
          <input type="text" id="datepicker" readonly="readonly" name="publish_time" value="{{data["publish_time"]|replace("N/A","")}}" />
          <label class="input-label">{{data["preorder_date_text"]}}</label>
          <span class="danger input-error"></span>
        </div>
        <div class="layout-8 p-l-0 align-self-center">
          <span>{{data["preorder_notice_text"]}}</span>
        </div>
      </div>
      <div class="ta-r">
        <button type="button" class="btn btn-primary submit_announcement">{{data["save_text"]}}</button>
      </div>
    </div>
  </form>
  <script>
  tab_menu_show(languages);
  $('#datepicker').datepicker({
    minDate: +1,
    dateFormat: 'yy-mm-dd',
    numberOfMonths: 1,
    showButtonPanel: true,
    closeText: 'Clear'
  });
  </script>
</div>
