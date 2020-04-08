<nav class="m-t-15">
  <ul class="pagination justify-content-center pagination-left">
    {% if data["left_show"] == 1 %}
    <li class="page-item">
      <a class="page-link {{data["bind_class"]}}" ajax_url="{{data["base_url"]}}" 
         data_sn="{{data["data_sn"]}}" tab_sn="{{data["tab_sn"]}}" page_sn="1" search="{{data["search"]}}">
        <i class="icon icon-firstpage"></i>
      </a>
    </li>
    <li class="page-item">
      <a class="page-link {{data["bind_class"]}}" ajax_url="{{data["base_url"]}}" 
         data_sn="{{data["data_sn"]}}" tab_sn="{{data["tab_sn"]}}" page_sn="{{data["reduce"]}}" search="{{data["search"]}}">
        <i class="icon icon-left"></i>
      </a>
    </li>
    {% endif %}
    {% for page,page_value in data["bar"].items() %}
    <li class="page-item {{page_value["active"]}}">
      <a class="page-link {{data["bind_class"]}}" ajax_url="{{data["base_url"]}}" 
         data_sn="{{data["data_sn"]}}" tab_sn="{{data["tab_sn"]}}" page_sn="{{page_value["name"]}}" search="{{data["search"]}}">{{page_value["name"]}}
      </a>
    </li>
    {% endfor %}
    {% if data["right_show"] == 1 %}
    <li class="page-item">
      <a class="page-link {{data["bind_class"]}}" ajax_url="{{data["base_url"]}}" 
         data_sn="{{data["data_sn"]}}" tab_sn="{{data["tab_sn"]}}" page_sn="{{data["add"]}}" search="{{data["search"]}}">
        <i class="icon icon-right"></i>
      </a>
    </li>
    <li class="page-item">
      <a class="page-link {{data["bind_class"]}}" ajax_url="{{data["base_url"]}}" 
         data_sn="{{data["data_sn"]}}" tab_sn="{{data["tab_sn"]}}" page_sn="{{data["max_page"]}}" search="{{data["search"]}}">
        <i class="icon icon-lastpage"></i>
      </a>
    </li>
    {% endif %}
  </ul>
  <ul class="pagination-right">
    <li>
      <input type="text" class="jump-page-input"/>
      <button type="button" 
              class="btn btn-primary {{data["bind_class"]}} jump-page-btn" 
              ajax_url="{{data["base_url"]}}"
              data_sn="{{data["data_sn"]}}" 
              tab_sn="{{data["tab_sn"]}}"
              page_sn=""
              disabled>
        {{data["go_text"]}}
      </button>
    </li>
  </ul>
</nav>
