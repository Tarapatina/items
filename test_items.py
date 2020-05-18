link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket(browser):
    browser.get(link)
    assert len(browser.find_element_by_css_selector("button.btn-add-to-basket"))>0, 'Basket not found'
