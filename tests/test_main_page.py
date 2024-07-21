from data import Answers
import pytest


class TestMainPage:

    @pytest.mark.parametrize(
        "q_num,expected_result",
        [
            (0, Answers.ANSWER_1),
            (1, Answers.ANSWER_2),
            (2, Answers.ANSWER_3),
            (3, Answers.ANSWER_4),
            (4, Answers.ANSWER_5),
            (5, Answers.ANSWER_6),
            (6, Answers.ANSWER_7),
            (7, Answers.ANSWER_8)
        ]
    )
    def test_questions(self, main_page, q_num, expected_result):
        main_page.confirm_cookies()
        result = main_page.click_on_question_and_get_answer_text(q_num)
        assert result == expected_result
