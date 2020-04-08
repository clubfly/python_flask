<nav class="m-b-15 recognition-methods-button">
  <h2 class="title m-r-15">{{data["announcement_list"]["titles"]}}</h2>
  <button type="button"
          class="btn btn-primary block-tooltip back_system_announcement"
          data_sn="0"
          tab_sn="{{data["system_announcement_tab"]}}"
          page_sn="{{data["pages"]}}"
          ajax_url="{{data["system_announcement_url"]}}">
    <i class="icon icon-back-w"></i>
    <span class="block-tooltip-top">{{data["back_to_system_announcement_text"]}}</span>
  </button>
  <span class="date-time-text float-r">
    {{data["publish_time_text"]}}：<span>{{data["publish_time"]}}</span>
  </span>
</nav>
<div>
  <div class="layout-style-1 layout-y-scroll height-79vh">
    <p>{{data["announcement_list"]["contents"]}}</p>
  </div>
</div>
