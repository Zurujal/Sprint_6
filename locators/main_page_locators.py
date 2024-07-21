from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER = By.XPATH, '//*[@id="accordion__panel-{}"]'
    COOKIE_CONFIRMATION = By.XPATH, '//*[@id="rcc-confirm-button"]'
    UPPER_ORDER_BUTTON = By.XPATH, '//*[@class="Button_Button__ra12g"]'
    MIDDLE_ORDER_BUTTON = By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
