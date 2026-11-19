from selenium.webdriver.common.by import By


def test_autorization(browser):
    standard_user = 'standard_user'
    password = 'secret_sauce'

    input_username = browser.find_element(By.CSS_SELECTOR, '[data-test="username"]')
    input_password = browser.find_element(By.CSS_SELECTOR, '[data-test="password"]')
    login_button = browser.find_element(By.CSS_SELECTOR, '[data-test="login-button"]')

    input_username.send_keys(standard_user)
    input_password.send_keys(password)
    login_button.click()
    assert browser.find_element(By.CSS_SELECTOR, '[data-test="title"]').text == 'Products'

    add_t_shirt = browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')

    add_t_shirt.click()
    assert browser.find_element(By.CSS_SELECTOR, '[data-test="remove-sauce-labs-bolt-t-shirt"]').text == 'Remove'

    shopping_cart_link = browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    shopping_cart_link.click()
    assert browser.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-name"]').text == 'Sauce Labs Bolt T-Shirt'
    assert browser.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-price"]').text == '$15.99'