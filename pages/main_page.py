from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Подтверждение cookies')
    def confirm_cookies(self):
        locator = MainPageLocators.COOKIE_CONFIRMATION
        self.click_on_element(locator)

    @allure.step('Клик на вопрос')
    def click_on_question(self, num):
        locator = self.format_locator(MainPageLocators.QUESTION, num)
        self.click_on_element(locator)

    @allure.step('Получение текста ответа')
    def get_text_from_answer(self, num):
        locator = self.format_locator(MainPageLocators.ANSWER, num)
        return self.get_text_from_element(locator)

    @allure.step('Клик на вопрос и получение текста ответа')
    def click_on_question_and_get_answer_text(self, num):
        self.click_on_question(num)
        return self.get_text_from_answer(num)

    @allure.step('Клик на кнопку "Заказать" в верхней части страницы')
    def click_on_upper_order_button(self):
        locator = MainPageLocators.UPPER_ORDER_BUTTON
        self.click_on_element(locator)

    @allure.step('Клик на кнопку "Заказать" в середине страницы')
    def click_on_middle_order_button(self):
        locator = MainPageLocators.MIDDLE_ORDER_BUTTON
        self.click_on_element(locator)
