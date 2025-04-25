from typing import Any

import allure
from behave import when, then

from common.api_auto import APIAuto
from common.base_classes import base_assert
from datetime import datetime, timedelta

api_auto = APIAuto()
step_base_assert = base_assert.BaseAssert()


@allure.step("I access the API for 9 day weather")
@when("I access the API for 9 day weather")
def step_impl(context: Any) -> None:
    api_auto.weather_open_api.nine_day_weather.get()


@allure.step("I should see the status is OK")
@then("I should see the status is OK")
def step_impl(context: Any) -> None:
    api_auto.weather_open_api.nine_day_weather.assert_success_connection()


@allure.step("I should see the relative humidity data for the day after tomorrow")
@then("I should see the relative humidity data for the day after tomorrow")
def step_impl(context: Any) -> None:
    today = datetime.today()
    the_day_after_tomorrow = today + timedelta(days=2)
    the_day_after_tomorrow_string = the_day_after_tomorrow.strftime("%Y%m%d")
    for data in api_auto.weather_open_api.nine_day_weather.current_response.json()["weatherForecast"]:
        if data["forecastDate"] == the_day_after_tomorrow_string:
            step_base_assert.is_not_none(data["forecastMaxrh"])
            step_base_assert.is_not_none(data["forecastMinrh"])
            step_base_assert.are_unequal(data["forecastMaxrh"]["value"], "")
            step_base_assert.are_unequal(data["forecastMaxrh"]["unit"], "")
            step_base_assert.are_unequal(data["forecastMinrh"]["value"], "")
            step_base_assert.are_unequal(data["forecastMinrh"]["unit"], "")
            break



