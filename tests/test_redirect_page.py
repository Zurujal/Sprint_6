import allure


class TestRedirectPage:

    @allure.title("Проверка перехода с главной страницы на страницу заказа по верхней кнопке 'Заказать'")
    def test_redirect_from_main_to_order_page_upper_button(self, main_page, order_page):
        main_page.confirm_cookies()
        main_page.click_on_upper_order_button()
        assert order_page.is_order_page()

    @allure.title("Проверка перехода с главной страницы на страницу заказа по средней кнопке 'Заказать'")
    def test_redirect_from_main_to_order_page_middle_button(self, main_page, order_page):
        main_page.confirm_cookies()
        main_page.click_on_middle_order_button()
        assert order_page.is_order_page()

    @allure.title("Проверка перехода на главную страницу по клику на лого 'Самокат'")
    def test_scooter_logo_redirect_to_main_page(self, redirect_page, main_page):
        main_page.confirm_cookies()
        redirect_page.click_on_scooter_logo()
        assert redirect_page.is_successful_home_page_redirect()

    @allure.title("Проверка перехода на страницу дзена по клику на лого 'Яндекс'")
    def test_yandex_logo_redirect_to_dzen(self, redirect_page, main_page):
        main_page.confirm_cookies()
        redirect_page.click_on_yandex_logo()
        assert redirect_page.is_successful_dzen_page_redirect()
