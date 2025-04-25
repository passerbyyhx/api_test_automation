from typing import Dict

import allure
import requests

from common.tool import Tool
from common.base_classes import base_assert


class BaseAPI:
    token = ""

    def __init__(self, *path_segments: str, data: Dict = None, params: Dict = None) -> None:
        self.url_path = ""
        for path_segment in path_segments:
            self.url_path += f"{path_segment}/"
        self.full_url = ""
        self.headers = {}
        self.data = data
        self.current_response = None
        self.tool = Tool()
        self.params = params
        self.base_assert = base_assert.BaseAssert()

    def get_full_url(self, domain) -> None:
        if domain[-1] == "/":
            domain = domain[:-1]
        if self.url_path.startswith("/"):
            self.url_path = self.url_path[1:]
        full_url = f"{domain}/{self.url_path}"
        params_section = ""
        if self.params is not None:
            params_section += "?"
            for key in self.params.keys():
                value = self.params[key]
                params_section += f"{key}={value}&"
            params_section = params_section[:-1]
        full_url = full_url[:-1] + params_section
        self.full_url = full_url

    @classmethod
    def set_token(cls, current_token) -> None:
        cls.token = current_token

    def set_headers(self) -> None:
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def response_status(self):
        status_code = self.current_response.status_code
        reason = self.current_response.reason
        allure.step(f"Connection Status: {status_code} - {reason}")

    def get(self):
        with allure.step(f"{self.tool.get_current_datetime()} Sending GET request to {self.full_url}"):
            if self.data is not None:
                self.current_response = requests.get(url=self.full_url, json=self.data)
            else:
                self.current_response = requests.get(url=self.full_url)
            self.response_status()
            return self.current_response

    def post(self):
        with allure.step(f"{self.tool.get_current_datetime()} Sending POST request to {self.full_url}"):
            if self.data is not None:
                self.current_response = requests.post(url=self.full_url, json=self.data)
            else:
                self.current_response = requests.post(url=self.full_url)
            self.response_status()
            return self.current_response

    def assert_success_connection(self):
        self.base_assert.are_equal(str(self.current_response.status_code), "200")
        allure.step(f"Confirmed that the connection status code is 200. Connection success.")

    def get_response_value(self, key=""):
        if self.current_response is not None:
            response_data = self.current_response.json()
            if key in response_data:
                return response_data.get(key)
            else:
                allure.step(f"Key {key} is not available.")
                raise Exception(f"Key {key} is not available.")
        else:
            allure.step("Response is empty.")
            raise Exception("Response is empty.")


class BaseDomain:
    def __init__(self, domain: str):
        self.domain = domain

    def sub_path(self, *path_segments: str, data: Dict = None, params: Dict = None) -> BaseAPI:
        current_sub_path = BaseAPI(*path_segments, data=data, params=params)
        current_sub_path.get_full_url(self.domain)
        return current_sub_path
