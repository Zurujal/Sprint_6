
class TestOrderPage:

    def test_successful_order(self, main_page, order_page):
        main_page.confirm_cookies()
        main_page.click_on_upper_order_button()
        order_page.fill_all_input_fields_on_first_page()
        order_page.click_on_continue_button()
        order_page.fill_all_input_fields_on_second_page()
        order_page.order_confirmation()
        order_page.additional_order_confirmation()
        assert order_page.is_successful_order_page()
