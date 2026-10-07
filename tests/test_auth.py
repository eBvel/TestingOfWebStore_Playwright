import allure
from playwright.sync_api import expect

from pages.auth_page import AuthPage


@allure.suite("АВТОРИЗАЦИЯ")
class TestAuth:

    @allure.title("Тест: Авторизация с валидными данными.")
    def test_login(self, auth_page: AuthPage) -> None:
        auth_page.open()
        auth_page.login('покупатель', 'покупатель')
        expect(auth_page.page).to_have_url("http://91.197.96.80/")
        # TODO: to add assert by title of catalog.
