from typing_extensions import Self

from config.links import Links
from config.locators import AuthLocators as locator
from config.logging_config import get_logger
from pages.base_page import BasePage

logger = get_logger(__name__)


class AuthPage(BasePage):
    url = Links.AUTH_PAGE_URL

    def enter_login(self, login: str) -> Self:
        self.get_element(locator.LOGIN_FIELD).fill(login)
        return self

    def enter_password(self, password: str) -> Self:
        self.get_element(locator.PASSWORD_FIELD).fill(password)
        return self

    def click_login_button(self) -> None:
        self.get_element(locator.LOGIN_BUTTON).click()

    def login(self, login: str, password: str) -> None:
        (
            self
            .enter_login(login)
            .enter_password(password)
            .click_login_button()
        )
