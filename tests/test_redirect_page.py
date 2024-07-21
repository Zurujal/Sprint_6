import pytest


class TestRedirectPage:

    @pytest.mark.parametrize("button_type", (1, 2))
    def test_redirect_from_main_to_order_page(self, main_page, order_page, button_type):
        main_page.confirm_cookies()
        if button_type == 1:
            main_page.click_on_upper_order_button()
        else:
            main_page.click_on_middle_order_button()
        assert order_page.is_order_page()

    def test_scooter_logo_redirect_to_main_page(self, redirect_page, main_page):
        main_page.confirm_cookies()
        redirect_page.click_on_scooter_logo()
        assert redirect_page.is_successful_home_page_redirect()

    def test_yandex_logo_redirect_to_dzen(self, redirect_page, main_page):
        main_page.confirm_cookies()
        redirect_page.click_on_yandex_logo()
        assert redirect_page.is_successful_dzen_page_redirect()
