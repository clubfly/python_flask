/***********************
 *--    JS Config    --*
 ***********************/
var api_host = '';
var api = {
  'screenshot': {
    'domain': '',
    'url': screenshot_api,
    'method': 'POST',
    'data': {},
    'callback_function': '',
    'error_function': ''
  },
  'face_screenshot': {
    'domain': '',
    'url': '',
    'method': 'POST',
    'data': {},
    'callback_function': '',
    'error_function': ''
  },
  'save_items_status': {
    'domain': '',
    'url': '',
    'method': 'POST',
    'data': {},
    'callback_function': '',
    'error_function': ''
  },
}
// websocket url
var wsc_url = 'ws://127.0.0.1:1506/server';
// 開啟webcam尺寸, 設定 1 為 1280x720, 設定 2 為 1920x1080, 設定 3 為 2592x1944, 不在範圍內預設 1280x720
var videoSet = 1;
// confirmCheckoutBtn 設定 0 為隱藏confirm-checkout按鈕, 設定 1 為顯示按鈕
var confirmCheckoutBtn = 0;
// mockConfirmCheckoutBtn 設定 0 為隱藏mock-confirm-checkout按鈕, 設定 1 為顯示按鈕, 若confirmCheckoutBtn已經設定為顯示, 則mockConfirmCheckoutBtn預設為隱藏
var mockConfirmCheckoutBtn = 0;
// printBtn 設定 0 為隱藏print按鈕, 設定 1 為顯示按鈕
var printBtn = 0;
// iccardBtn 設定 0 為隱藏iccard按鈕, 設定 1 為顯示按鈕
var iccardBtn = 0;
// qrcodeBtn 設定 0 為隱藏qrcode按鈕, 設定 1 為顯示按鈕
var qrcodeBtn = 0;
// mockData 設定 0 為使用正式資料, 設定 1 為使用假資料
var mockData = 0;
// backOfProductId 設定 0 為product_id無商品背面處理, 設定 1 為遇到特殊product_id為背面時, 則無法列印及確認結帳
var backOfProductId = 1;
// backOfProductIdArray 設定商品為背面的product_id
var backOfProductIdArray = ["2134"];
// useSymbol 設定 0 為使用模型symbol, 設定為 1 為使用樣板symbol
var useSymbol = 0;

/**************************************************************************************
 *    Accordion Menu
 * 1. menu level 最多到四層, 超過不顯示
 * 2. 畫面呈現方式會依照 accordion menu 陣列內物件的順序
 * 3. openSubmenu 設置為 1, 若有 submenu 則展開, 同一層僅顯示第一筆
 * 4. parent 第一層預設為 0, 第二層之後需設置 submenu 要掛載的 parent, 若無該 parent 將不顯示
 * 5. title 字元超過則顯示..., 依照RWD做調整
 * 6. alink 設置連結若該元素還有 child, 點擊時只會展開 submenu 不會前往連結處
 **************************************************************************************/
var accordion_menu = [
  {
    'submenuList': [
      {
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 0,
        'title': 'Default level one',
        'alink': ''
      },
    ]
  },
  {
    'submenuList': [
      {
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 1,
        'title': 'Default level two',
        'alink': ''
      },
    ]
  },
  {
    'submenuList': [
      {
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 1,
        'title': 'Default level three',
        'alink': ''
      },
    ]
  },
  {
    'submenuList': [
      {
        'openSubmenu': 0,
        'tabContentShow': 0,
        'parent': 1,
        'title': 'Default level four',
        'alink': '#tab-content-1'
      },
    ]
  }
];