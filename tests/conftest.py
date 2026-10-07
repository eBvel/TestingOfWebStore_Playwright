from typing import Any, Generator

import pytest
from playwright.sync_api import BrowserContext, Page, Playwright

from config.logging_config import get_logger
from pages.auth_page import AuthPage

logger = get_logger(__name__)
logger.info('---------------------------------------------------------------')


@pytest.fixture(scope='session')
def context(playwright: Playwright) -> Generator[BrowserContext, Any, None]:
    browser = playwright.chromium.launch(headless=False,
                                         args=["--start-maximized"])
    logger.debug(f'Initialized browser: "{repr(browser)}".')
    context = browser.new_context(no_viewport=True)
    logger.debug(f'Initialized context: "{repr(context)}".')

    yield context

    browser.close()
    logger.debug('Browser closed')


@pytest.fixture
def page(context: BrowserContext) -> Page:
    new_page = context.new_page()
    logger.debug(f'Initialized new_page: "{repr(page)}".')

    logger.debug(f'Return new_page: {repr(page)}')
    return new_page


@pytest.fixture
def auth_page(page: Page) -> AuthPage:
    logger.info(f'Created AuthPage. Fixture: {repr(auth_page)}')
    return AuthPage(page)
