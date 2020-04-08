<nav class="m-t-15">
  <ul class="pagination justify-content-center pagination-left">
    {% if data["left_show"] == 1 %}
    <li class="page-item">
      <a class="page-link" href="{{data["base_url"]}}?service_sn={{data["service_sn"]}}" page_sn="1">
        <i class="icon icon-firstpage"></i>
      </a>
    </li>
    <li class="page-item">
      <a class="page-link" href="{{data["base_url"]}}?service_sn={{data["service_sn"]}}&pages={{data["reduce"]}}" page_sn="{{data["reduce"]}}">
        <i class="icon icon-left"></i>
      </a>
    </li>
    {% endif %}
    {% for page,page_value in data["bar"].items() %}
    <li class="page-item {{page_value["active"]}}">
      <a class="page-link" href="{{data["base_url"]}}?service_sn={{data["service_sn"]}}&pages={{page_value["name"]}}" page_sn="{{page_value["name"]}}">{{page_value["name"]}}</a>
    </li>
    {% endfor %}
    {% if data["right_show"] == 1 %}
    <li class="page-item">
      <a class="page-link" href="{{data["base_url"]}}?service_sn={{data["service_sn"]}}&pages={{data["add"]}}" page_sn="{{data["add"]}}">
        <i class="icon icon-right"></i>
      </a>
    </li>
    <li class="page-item">
      <a class="page-link" href="{{data["base_url"]}}?service_sn={{data["service_sn"]}}&pages={{data["max_page"]}}" page_sn="{{data["max_page"]}}">
        <i class="icon icon-lastpage"></i>
      </a>
    </li>
    {% endif %}
  </ul>
</nav>
