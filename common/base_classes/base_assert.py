import allure
import requests.models
from typing import Any


class BaseAssert:
    @staticmethod
    def are_equal(current_value: object, baseline: object) -> None:
        with allure.step(f"Assert whether current value {current_value} equals to baseline {baseline}:"):
            if type(current_value) != type(baseline):
                type_of_baseline = type(current_value)
                type_of_current_value = type(current_value)
                raise AssertionError(
                    f"Assertion Fail. Type of current value {type_of_current_value} is not equal to type of baseline {type_of_baseline}.")
            assert current_value == baseline, f"Current value {current_value} does not equal to {baseline}."

    def is_true(self, current_value: bool) -> None:
        with allure.step(f"Assert whether current value {current_value} is True:"):
            if type(current_value) is not bool:
                type_of_current_value = type(current_value)
                raise AssertionError(
                    f"Assertion Fail. Current value {current_value} is a {type_of_current_value}, not a boolean variable.")
            else:
                self.are_equal(current_value, True)

    def is_false(self, current_value: bool) -> None:
        with allure.step(f"Assert whether current value {current_value} is False:"):
            if type(current_value) is not bool:
                type_of_current_value = type(current_value)
                raise AssertionError(
                    f"Assertion Fail. Current value {current_value} is a {type_of_current_value}, not a boolean variable.")
            else:
                self.are_equal(current_value, False)

    def is_none(self, current_value: Any) -> None:
        with allure.step(f"Assert whether current value {current_value} is None:"):
            self.are_equal(current_value, None)

    @staticmethod
    def is_not_none(current_value: Any) -> None:
        with allure.step(f"Assert whether current value {current_value} is not None:"):
            if current_value is None:
                raise AssertionError(f"Assertion Fail. Current value is None.")
            else:
                allure.step(f"Current value {current_value} is not None.")

    @staticmethod
    def are_unequal(current_value: Any, baseline: Any) -> None:
        with allure.step(f"Assert whether current value {current_value} is not equal to {baseline}:"):
            if current_value == baseline:
                raise AssertionError(f"Assertion Fail. Current value is equal to {baseline}.")
            else:
                allure.step(f"Current value {current_value} is not equal to {baseline}.")



