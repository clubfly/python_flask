{{header_footer_data["header_html"]}}
    <div class="modal fade" id="modalCenterCamera" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-1200">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title"></h5>
            <button type="button" class="close webcam-stop">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body row">
            <div class="layout-5-5">
              <div id="videostream">
                <video autoplay></video>
                <img id="source-img"/>
              </div>
              <div class="width-100 ta-c p-t-20">
                <button type="button" 
                        class="btn btn-secondary btn-lg screenshot-button" disabled>
                  <i class="icon icon-camera-w"></i>{{data["screenshot_text"]}}
                </button>
              </div>
            </div>
            <div class="layout-4-5">
              <div class="width-100">
                <h4 class="h4">
                {{data["image_total_text"]}}<span id="pic_total" limitation="0" total="0">0</span>{{data["unit_text"]}}，
                {{data["screenshoted_text"]}}<span id="current_pic">0</span>{{data["unit_text"]}}，
                {{data["screenshoting_text"]}}<span id="enabled_pic">0</span>{{data["unit_text"]}}
                </h4>
              </div>
              <ul class="screenshot-img row"></ul>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-light webcam-stop cancel">{{data["cancel_text"]}}</button>
            <button type="button" class="btn btn-primary save_product_image" 
                    data_sn="" ajax_url="" tab_sn="">{{data["save_text"]}}
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="content-wrapper rwd-ma-15 margin-15 row">
      <div id="lds-dual-ring-wrapper">
        <div class="lds-dual-ring"></div>
        <span class="lds-span">Loading</span>
      </div>
      <div class="alert alert-dismissible">
        <span class="message"></span>
        <button type="button" class="close">
          <span>&times;</span>
        </button>
      </div>
      <div class="modal fade" id="modalCenterText" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title"></h5>
              <button type="button" class="close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <span></span>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-light cancel">{{data["cancel_text"]}}</button>
              <button type="button" class="btn btn-primary save_status" 
                      data_sn="" 
                      status_sn="" 
                      ajax_url="" 
                      tab_sn="0"
                      product_sn="0">{{data["save_text"]}}</button>
            </div>
          </div>
        </div>
      </div>
      <div class="modal fade" id="modalCenterImage" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-1200">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title"></h5>
              <button type="button" class="close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body"></div>
          </div>
        </div>
      </div>
      <div class="modal-second fade" id="modalSecond">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-second-content">
            <div class="modal-body">
              請注意, 您目前有選擇的檔案, 若再次選擇檔案將清除並以新選擇的檔案做覆蓋。
            </div>
            <div class="modal-footer">
              <button type="button" 
                      class="btn btn-light cancel">
                      {{data["cancel_text"]}}
              </button>
              <button type="button" 
                      class="btn btn-primary confirm-select-file">
                      確認更換檔案
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-second fade" id="common_modal_second">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-second-content">
            <div class="modal-body"></div>
            <div class="modal-footer">
              <button type="button" 
                      class="btn btn-light cancel">
                      {{data["cancel_text"]}}
              </button>
              <button type="button" 
                      class="btn btn-primary modal-confirm">
                      {{data["confirm_text"]}}
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="modal fade" id="modal_search" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title"></h5>
              <button type="button" class="close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form id="search_product_form" method="get" data_sn="" tab_sn="" 
                    ajax_url="{{data["company_product_url"]}}">
                <div class="row">
                  <div class="form-input-group layout-5">
                    <input type="text"
                           name="product_sn" 
                           id="product_sn" />
                    <label class="input-label">{{data["search_product_sn_text"]}}</label>
                    <span class="danger input-error"></span>
                  </div>
                  <div class="form-input-group layout-5">
                    <input type="text"
                           name="product_name"
                           id="product_name" />
                    <label class="input-label">{{data["search_product_name_text"]}}</label>
                    <span class="danger input-error"></span>
                  </div>
                  <div class="form-input-group layout-5">
                    <input type="text"
                           name="abbreviation"
                           id="abbreviation" />
                    <label class="input-label">{{data["search_abbreviation_text"]}}</label>
                    <span class="danger input-error"></span>
                  </div>
                  <div class="form-input-group layout-5">
                    <input type="text"
                           name="barcode"
                           id="barcode" />
                    <label class="input-label">{{data["search_barcode_text"]}}</label>
                    <span class="danger input-error"></span>
                  </div>
                  <div class="layout-10">
                    <div class="form-input-group-wrapper">
                      <p class="input-title">{{data["search_product_create_time_text"]}}</p>
                      <div class="row" id="datepicker-group-1">
                        <div class="form-input-group layout-4-5">
                          <input type="text"
                                 readonly="readonly"
                                 name="ct_start_date"
                                 class="datepicker start_date"
                                 id="ct_start_date" />
                          <label class="input-label">{{data["search_start_day_text"]}}</label>
                          <span class="danger input-error start_date_error"></span>
                        </div>
                        <div class="form-input-group layout-1">
                          ~
                        </div>
                        <div class="form-input-group layout-4-5">
                          <input type="text"
                                 readonly="readonly"
                                 name="ct_end_date"
                                 class="datepicker end_date"
                                 id="ct_end_date" />
                          <label class="input-label">{{data["search_end_day_text"]}}</label>
                          <span class="danger input-error end_date_error"></span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="layout-10">
                    <div class="form-input-group-wrapper">
                      <p class="input-title">{{data["search_product_update_time_text"]}}</p>
                      <div class="row" id="datepicker-group-2">
                        <div class="form-input-group layout-4-5">
                          <input type="text"
                                 readonly="readonly"
                                 name="ut_start_date"
                                 class="datepicker start_date"
                                 id="ut_start_date" />
                          <label class="input-label">{{data["search_start_day_text"]}}</label>
                          <span class="danger input-error start_date_error"></span>
                        </div>
                        <div class="form-input-group layout-1">
                          ~
                        </div>
                        <div class="form-input-group layout-4-5">
                          <input type="text"
                                 readonly="readonly"
                                 name="ut_end_date"
                                 class="datepicker end_date"
                                 id="ut_end_date" />
                          <label class="input-label">{{data["search_end_day_text"]}}</label>
                          <span class="danger input-error end_date_error"></span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="form-input-group layout-5">
                    <select name="image_cnt" id="image_cnt">
                      <option value="">{{data["search_all_text"]}}</option>
                      <option value="1">{{data["search_yes_text"]}}</option>
                      <option value="0">{{data["search_no_text"]}}</option>
                    </select>
                    <label class="input-label">{{data["search_image_cnt_text"]}}</label>
                    <span class="danger input-error"></span>
                  </div>
                  <div class="form-input-group layout-5">
                    <select name="enabled" id="enabled">
                      <option value="">{{data["search_all_text"]}}</option>
                      <option value="1">{{data["enabled_text"]}}</option>
                      <option value="0">{{data["disabled_text"]}}</option>
                    </select>
                    <label class="input-label">{{data["search_product_status_text"]}}</label>
                    <span class="danger input-error"></span>
                  </div>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-light cancel">{{data["cancel_text"]}}</button>
              <button type="button" class="btn btn-primary search_products">{{data["search_text"]}}</button>
            </div>
          </div>
        </div>
      </div>
      <aside class="layout-2 padding-0 p-r-15 accordion-menu-wrapper">
        <button type="button" class="btn btn-light m-b-15 test-btn hidden">
          <i class="icon icon-menu"></i>
        </button>
      </aside>
      <section class="layout-8 padding-0 main-content">
        {% for row in data["tab_ui"] %}
        <article class="tab-content" id="tab-content-{{loop.index}}">
        {{row}}
        </article>
        {% endfor %}
      </section>
    </div>
{{header_footer_data["footer_html"]}}
