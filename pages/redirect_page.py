import allure

from pages.base_page import BasePage
from locators.redirect_page_locators import RedirectPageLocators


class RedirectPage(BasePage):

    @allure.step('Клик на лого "Самокат"')
    def click_on_scooter_logo(self):
        locator = RedirectPageLocators.SCOOTER_LOGO
        self.click_on_element(locator)

    @allure.step('Клик на лого "Яндекс"')
    def click_on_yandex_logo(self):
        locator = RedirectPageLocators.YANDEX_LOGO
        self.click_on_element(locator)

    @allure.step('Проверка перехода на главную')
    def is_successful_home_page_redirect(self):
        locator = RedirectPageLocators.HOME_PAGE_MARKER
        result = self.get_text_from_element(locator)
        return "Самокат" in result

    @allure.step('Проверка перехода на вкладку с дзеном')
    def is_successful_dzen_page_redirect(self):
        locator = RedirectPageLocators.DZEN_PAGE_MARKER
        self.switch_to_another_tab()
        result = self.get_text_from_element(locator)
        return "Темы в Дзене" in result
