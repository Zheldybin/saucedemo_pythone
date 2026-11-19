from selenium.webdriver.common.by import By


def test_locator_id(browser):
    # By.ID
    user_name = browser.find_element(By.ID, 'user-name')
    user_name.send_keys('standard_user')

    # By.NAME
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('secret_sauce')

    # By.TAG_NAME
    submit_button = browser.find_elements(By.TAG_NAME, 'input')
    submit_button[2].click()

    # By.CLASS_NAME
    title = browser.find_element(By.CLASS_NAME, 'app_logo').text
    assert title == 'Swag Labs'

    # By.CSS #id
    burger_btn = browser.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
    burger_btn.click()

    # By.PARTIAL_LINK_TEXT
    one_menu_item = browser.find_element(By.PARTIAL_LINK_TEXT, 'Items')
    assert one_menu_item.text == 'All Items'

    # By.LINK_TEXT
    two_menu_item = browser.find_element(By.LINK_TEXT, 'About')
    assert two_menu_item.text == 'About'

    # XPath: Поиск по атрибуту
    burger_btn_exit = browser.find_element(By.XPATH, "//div[@class='bm-cross-button']/button")
    burger_btn_exit.click()

    # XPath: Поиск по атрибуту
    description_product = browser.find_element(By.XPATH, "//div[@data-test='inventory-item-desc']")
    assert description_product.text == 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.'

    # XPath: Поиск по тексту
    title_product_jacket = browser.find_element(By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")
    assert title_product_jacket.text == 'Sauce Labs Fleece Jacket'

    # XPath: Частичное совпадение атрибута
    footer_text = browser.find_element(By.XPATH, "//*[contains(@data-test, 'foo')]/div").text
    assert 'Sauce Labs. All Rights Reserved' in footer_text

    # XPath: Частичное совпадение текста
    description_product_two = browser.find_element(By.XPATH, "//*[contains(text(), 'Reinforced 3-snap bottom')]")
    assert description_product_two.text == "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel."

    # XPath: ancestor
    item_card_ancestor = browser.find_element(By.XPATH,
                                              "//button[@data-test='add-to-cart-sauce-labs-backpack']/ancestor::div[@data-test='inventory-item']")
    assert "Sauce Labs Backpack" in item_card_ancestor.text

    # XPath: descendant
    product_title_descendant = browser.find_element(By.XPATH,
                                                    "//div[@data-test='inventory-list']/descendant::div[@data-test='inventory-item-name'][1]")
    assert product_title_descendant.text == "Sauce Labs Backpack"

    # XPath: following
    description_following = browser.find_element(By.XPATH,
                                                 "//div[@data-test='inventory-item-name'][text()='Sauce Labs Backpack']/following::div[@data-test='inventory-item-desc'][1]")
    assert "carry.allTheThings()" in description_following.text

    # XPath: parent
    label_parent = browser.find_element(By.XPATH,
                                        "//div[@data-test='inventory-item-name'][text()='Sauce Labs Backpack']/parent::*")
    assert "Sauce Labs Backpack" in label_parent.text

    # XPath: preceding
    jacket_title_preceding = browser.find_element(By.XPATH,
                                                  "//button[@data-test='add-to-cart-sauce-labs-fleece-jacket']/preceding::div[@data-test='inventory-item-name'][1]")
    assert jacket_title_preceding.text == "Sauce Labs Fleece Jacket"

    # XPath: and
    add_backpack_and = browser.find_element(By.XPATH,
                                            "//button[@data-test='add-to-cart-sauce-labs-backpack' and contains(@class, 'btn_inventory')]")
    assert add_backpack_and.text == "Add to cart"

    # CSS .class
    title_css = browser.find_element(By.CSS_SELECTOR, '.app_logo')
    assert title_css.text == "Swag Labs"

    # CSS .class1 .class2
    desc_class = browser.find_element(By.CSS_SELECTOR, '.inventory_item_label .inventory_item_desc')
    assert desc_class.text == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."

    # CSS .class1.class2
    btn_class = browser.find_element(By.CSS_SELECTOR, '.btn.btn_primary.btn_small.btn_inventory')
    assert btn_class.text == "Add to cart"

    # CSS tagname
    title_css_tag = browser.find_element(By.CSS_SELECTOR, 'title')
    assert title_css.text == "Swag Labs"

    # CSS tagname.class
    title_css_tagname_class = browser.find_element(By.CSS_SELECTOR, 'span.title')
    assert title_css_tagname_class.text == "Products"
