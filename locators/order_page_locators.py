from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = By.XPATH, '//*[@placeholder="* Имя"]'
    SURNAME_INPUT = By.XPATH, '//*[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]'
    STATION_SELECTION = By.XPATH, '//*[@placeholder="* Станция метро"]'
    PHONE_INPUT = By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]'
    CHOICE_BY_TEXT = By.XPATH, '//*[text()="{}"]'
    CONTINUE_BUTTON = By.XPATH, '//*[text()="Далее"]'
    ORDER_HEADER = By.XPATH, '//*[@class="Order_Header__BZXOb"]'
    DELIVERY_DATE_INPUT = By.XPATH, '//*[@placeholder="* Когда привезти самокат"]'
    RENT_DURATION = By.XPATH, '//*[@class="Dropdown-arrow"]'
    SCOOTER_COLOR_CHECKBOX = By.XPATH, '//*[@for="{}"]'
    COMMENT = By.XPATH, '//*[@placeholder="Комментарий для курьера"]'
    CONFIRM_BUTTON = By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    YES_BUTTON = By.XPATH, '//*[text()="Да"]'
    SUCCESSFUL_ORDER_HEADER = By.XPATH, '//*[@class="Order_ModalHeader__3FDaJ"]'
