import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestGuestLoginUploadPhoto(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8080/#/")

    def test_guest_login_upload_photo(self):
        # Нажимаем на кнопку "Гостевой вход"
        guest_button = self.driver.find_element(By.XPATH, "//a[contains(@href, '#/loading')]")
        guest_button.click()

        # Нажимаем на кнопку "Загрузить фото"
        upload_photo_button = self.driver.find_element(By.XPATH, "//button[@class='upload-button']")
        upload_photo_button.click()

        # Загружаем фото
        file_path = os.path.join(os.path.dirname(__file__), 'sample.png')
        file_input = self.driver.find_element(By.XPATH, "//input[@type='file' and @id='upload-input']")
        file_input.send_keys(file_path)

        load_photo_button = self.driver.find_element(By.XPATH, "//button[@id='result-button']")
        load_photo_button.click()

        expected_url = "http://localhost:8080/#/result"
        try:
            WebDriverWait(self.driver, 20).until(EC.url_to_be(expected_url))
            print("Правильный URL: {}".format(self.driver.current_url))
        except TimeoutException:
            print("Тайм-аут. Правильный URL не был достигнут.")

        # Проверяем содержимое контейнера с результатом
        container_content = self.driver.find_element(By.XPATH, "//span[@class='number']")
        self.assertTrue(1 <= int(container_content.text) <= 10, "Содержимое контейнера не является числом от 1 до 10")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
