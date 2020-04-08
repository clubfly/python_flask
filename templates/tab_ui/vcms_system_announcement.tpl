<nav class="m-b-15 recognition-methods-button">
  <h2 class="title m-r-15">{{data["menu_system_announcement_text"]}}</h2>
  {% if data["company_sn"] == 0 %}
  <button type="button"
          class="btn btn-primary block-tooltip add_system_announcement"
          data_sn="0"
          tab_sn="{{data["add_system_announcement_tab"]}}"
          page_sn="{{data["pages"]}}" 
          ajax_url="{{data["add_system_announcement_url"]}}">
    <i class="icon icon-add-w"></i>
    <span class="block-tooltip-top">{{data["add_system_announcement_text"]}}</span>
  </button>
  {% endif %}
</nav>
<div class="layout-style-1 table-scroll">
  <table class="table">
    <thead>
      <tr>
        <th class="width-40">{{data["system_announcement_title_text"]}}</th>
        <th class="width-10">{{data["publisher_text"]}}</th>
        <th class="width-25">{{data["publish_time_text"]}}</th>
        <th class="width-25">{{data["configure_text"]}}</th>
      </tr>
    </thead>
    <tbody class="hover-orange select-checkbox-wrapper" id="scrollDiv" onscroll="scrollInside()">
      {% if data["announcement_list"].items()|length > 0 %}
      {% for key,value in data["announcement_list"].items()%}
      <tr class="column sublayer">
        <td class="width-40">
          <div class="column-xs">{{data["system_announcement_title_text"]}}</div>
          <span>{{value["boards"][data["current_language"]]["titles"]}}</span>
        </td>
        <td class="width-10">
          <div class="column-xs">{{data["publisher_text"]}}</div>
          <span>{{value["user_name"]}}</span>
        </td>
        <td class="width-25">
          <div class="column-xs">{{data["publish_time_text"]}}</div>
          <span>{{value["publish_time"]}}</span>
        </td>
        <td class="width-25">
          {% if data["company_sn"] == 0 %}
          <div class="column-xs">{{data["configure_text"]}}</div>
            {% if value["publish_mark"] == 0 %}
          <button type="button" 
                  class="btn btn-light m-b-5 enabled_announcement"
                  data-title="{{data["confirm_announcement_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["board_hash"]}}"
                  status_sn="1"
                  tab_sn="{{data["system_announcement_tab"]}}"
                  page_sn="{{data["pages"]}}"
                  ajax_url="{{data["publish_system_announcement_url"]}}" >
            <i class="icon icon-enable"></i>
          </button>
          <button type="button" 
                  class="btn btn-light m-b-5 add_system_announcement"
                  data-title="{{data["edit_announcement_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["board_hash"]}}" 
                  tab_sn="{{data["add_system_announcement_tab"]}}"
                  page_sn="{{data["pages"]}}"
                  ajax_url="{{data["add_system_announcement_url"]}}">
            <i class="icon icon-edit"></i>
          </button>
            {% else %}
          <button type="button" 
                  class="btn btn-light m-b-5 disabled_announcement"
                  data-title="{{data["cancel_announcement_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["board_hash"]}}"
                  status_sn="0" 
                  tab_sn="{{data["system_announcement_tab"]}}"
                  page_sn="{{data["pages"]}}"
                  ajax_url="{{data["publish_system_announcement_url"]}}">
            <i class="icon icon-disable"></i>
          </button>
            {% endif %}
          {% endif %}
          <button type="button" 
                  class="btn btn-light m-b-5 add_system_announcement"
                  data-title="{{data["preview_announcement_text"]}}"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  data_sn="{{value["board_hash"]}}" 
                  tab_sn="{{data["add_system_announcement_tab"]}}"
                  page_sn="{{data["pages"]}}"
                  ajax_url="{{data["view_system_announcement_url"]}}">
            <i class="icon icon-productlist"></i>
          </button>
        </td>
      </tr>
      {% endfor %}
      {% else %}
      <tr>
        <td class="padding-0">
          <div class="no-data-wrapper">
            <img src="/static/image/icon-notification.svg"/>
            <p>{{data["empty_announcement_text"]}}</p>
          </div>
        </td>
      </tr>
      {% endif %}
    </tbody>
  </table>
</div>
{{data["pagination"]}}
