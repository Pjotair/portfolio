from pages.home_page import HomePage


def test_page_header(driver, test_data):
    home_page = HomePage(driver)
    url = test_data["base_url"]
    driver.get(url)
    
    page_header = home_page.page_header()
    expected_page_header = test_data["home"]["page_header"]

    assert page_header == expected_page_header, \
        f'Page header should be {expected_page_header}, and is {page_header}'
    