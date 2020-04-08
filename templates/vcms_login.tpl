{{header_footer_data["header_html"]}}
    <div class="content-wrapper rwd-ma-15">
      <article class="row login-wrapper layout-style-1">
        <div class="layout-sm-10 layout-md-5 main-animation-wrapper">
          <div class="main-animation"></div>
          <img src="/static/image/logo-w.svg" class="main-title"/>
          <p class="main-mark">VCMS</p>
        </div>
        <div class="layout-sm-10 layout-md-5 align-self-center login-form-wrapper">
          <form id="user" method="POST" action="{{data["acc_login_url"]}}" autocomplete="off">
            <div class="form-input-group">
              <input type="text" name="account" 
                     placeholder="{{data["account_text"]}}" 
                     class="input-with-icon input-icon-account account"/>
              <label class="input-label">{{data["account_text"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <div class="form-input-group">
              <input type="password" name="password" 
                     placeholder="{{data["password_text"]}}" 
                     class="input-with-icon input-icon-password password"/>
              <label class="input-label">{{data["password_text"]}}</label>
              <span class="danger input-error"></span>
            </div>
            <button type="button" class="btn btn-primary btn-block longin-btn">{{data["login_text"]}}</button>
          </form>
        </div>
      </article>
    </div>
    <script type="text/javascript">
      LANG = {
        'ACCOUNT': '{{data["account_text"]}}',
        'PASSWORD': '{{data["password_text"]}}',
        'error_account_required_text': '{{data["error_acc_text"]}}',
        'error_password_required_text': '{{data["error_pwd_text"]}}'
      }
    </script>
{{header_footer_data["footer_html"]}}
