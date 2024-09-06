import time
import pytest
from .pages.product_page import PageProduct
params = list(map(str, range(10)))
@pytest.mark.parametrize('param', [
    x if x != 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7'
    else pytest.param(x, marks=pytest.mark.xfail)
    for x in params
])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_" \
           f"207/?promo=offer{param}"
    page = PageProduct(browser, link)
    page.open()
    page.should_be_product_page()