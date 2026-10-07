import allure
from playwright.sync_api import Locator, Page
from typing_extensions import Self

from config.links import Links
from config.logging_config import get_logger

logger = get_logger(__name__)


class BasePage:
    url = Links.BASE_URL

    def __init__(self, page: Page):
        logger.info('Constructor BasePage')
        logger.debug(
            f'Constructor of {self.__class__.__name__}, '
            f'args: ({repr(self)}, {repr(page)})'
        )
        self.page = page

    def open(self) -> Self:
        logger.info(f'Open {self.__class__.__name__}')
        logger.debug(f'Page URL: {self.url}')
        with allure.step('Открытие страницы по ссылке: {url}'):
            self.page.goto(self.url)
        return self

    def get_element(self, locator: str) -> Locator:
        logger.info(f'Find element of {self.__class__.__name__}')
        logger.debug(f'Page: {repr(self)}, Element locator: {locator}')
        with allure.step('Поиск элемента по локатору: "{locator}"'):
            return self.page.locator(locator)
