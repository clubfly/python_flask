/***********************
 *    VCMS API Object
 ***********************/
var api_host = '';
var api = {
  'save_items_status': {
    'domain': '',
    'url': '',
    'method': 'POST',
    'data': {},
    'callback_function': '',
    'error_function': ''
  },
}

/**************************************************************************************
 *    Accordion Menu
 * 1. menu level 最多到四層, 超過不顯示
 * 2. 畫面呈現方式會依照 accordion menu 陣列內物件的順序
 * 3. openSubmenu 設置為 1, 若有 submenu 則展開, 同一層僅顯示第一筆
 * 4. parent 第一層預設為 0, 第二層之後需設置 submenu 要掛載的 parent, 若無該 parent 將不顯示
 * 5. title 字元超過則顯示..., 依照RWD做調整
 * 6. alink 設置連結若該元素還有 child, 點擊時只會展開 submenu 不會前往連結處
 **************************************************************************************/
