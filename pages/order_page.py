import helpers
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    @allure.step('Ввод имени')
    def enter_name(self):
        locator = OrderPageLocators.NAME_INPUT
        self.set_text_to_element(locator, helpers.generate_name())

    @allure.step('Ввод фамилии')
    def enter_surname(self):
        locator = OrderPageLocators.SURNAME_INPUT
        self.set_text_to_element(locator, helpers.generate_surname())

    @allure.step('Ввод адреса')
    def enter_address(self):
        locator = OrderPageLocators.ADDRESS_INPUT
        self.set_text_to_element(locator, helpers.generate_address())

    @allure.step('Клик на поле выбора станции')
    def click_on_station_selection(self):
        locator = OrderPageLocators.STATION_SELECTION
        self.click_on_element(locator)

    @allure.step('Выбор станции из списка')
    def choose_station_from_list(self):
        name = helpers.generate_station_name()
        locator = self.format_locator(OrderPageLocators.CHOICE_BY_TEXT, name)
        self.click_on_element(locator)

    @allure.step('Ввод номера телефона')
    def enter_phone_number(self):
        locator = OrderPageLocators.PHONE_INPUT
        self.set_text_to_element(locator, helpers.generate_phone_number())

    @allure.step('Клик на кнопку "Далее"')
    def click_on_continue_button(self):
        locator = OrderPageLocators.CONTINUE_BUTTON
        self.click_on_element(locator)

    @allure.step('Ввод даты доставки')
    def enter_delivery_date(self):
        locator = OrderPageLocators.DELIVERY_DATE_INPUT
        self.set_text_to_element(locator, helpers.generate_date())

    @allure.step('Клик на поле выбора срока аренды')
    def click_on_rent_duration(self):
        locator = OrderPageLocators.RENT_DURATION
        self.click_on_element(locator)

    @allure.step('Выбор срока аренды из выпадающего списка')
    def choose_rent_duration(self):
        duration_name = helpers.generate_duration_name()
        locator = self.format_locator(OrderPageLocators.CHOICE_BY_TEXT, duration_name)
        self.click_on_element(locator)

    @allure.step('Проставление отметки напротив цвета самоката')
    def choose_scooter_color(self):
        color = helpers.generate_scooter_color()
        locator = self.format_locator(OrderPageLocators.SCOOTER_COLOR_CHECKBOX, color)
        self.click_on_element(locator)

    @allure.step('Комментарий для курьера')
    def enter_comment(self):
        locator = OrderPageLocators.COMMENT
        self.set_text_to_element(locator, helpers.generate_text())

    @allure.step('Клик на кнопку "Заказать"')
    def order_confirmation(self):
        locator = OrderPageLocators.CONFIRM_BUTTON
        self.click_on_element(locator)

    @allure.step('Клик на кнопку "Да" во всплывающем окне подтверждения заказа')
    def additional_order_confirmation(self):
        locator = OrderPageLocators.YES_BUTTON
        self.click_on_element(locator)

    @allure.step('Заполнение всех полей формы первой страницы заказа')
    def fill_all_input_fields_on_first_page(self):
        self.enter_name()
        self.enter_surname()
        self.enter_address()
        self.click_on_station_selection()
        self.choose_station_from_list()
        self.enter_phone_number()

    @allure.step('Заполнение всех полей формы второй страницы заказа')
    def fill_all_input_fields_on_second_page(self):
        self.enter_delivery_date()
        self.click_on_rent_duration()
        self.choose_rent_duration()
        self.choose_scooter_color()
        self.enter_comment()

    @allure.step('Проверка перехода на страницу заказа')
    def is_order_page(self):
        locator = OrderPageLocators.ORDER_HEADER
        result = self.get_text_from_element(locator)
        return result == "Для кого самокат"

    @allure.step('Проверка появления всплывающего окна с подтверждением успешного заказа')
    def is_successful_order_page(self):
        locator = OrderPageLocators.SUCCESSFUL_ORDER_HEADER
        result = self.get_text_from_element(locator)
        return "Заказ оформлен" in result
