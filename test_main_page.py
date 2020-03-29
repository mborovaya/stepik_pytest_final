from .pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(10) 
    page.go_to_login_page()
