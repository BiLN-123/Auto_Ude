from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

def get_csrf_token(email, password):
    # Khởi tạo trình duyệt với webdriver_manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Điều hướng đến trang đăng nhập
        driver.get('https://www.udemy.com/join/login-popup/')

        # Đăng nhập
        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        # Đợi trang tải
        time.sleep(5)

        # Lấy mã CSRF
        csrf_token = driver.execute_script("return document.querySelector('input[name=csrf_token]').value")
        print(f"CSRF Token: {csrf_token}")

        return csrf_token
    finally:
        # Đóng trình duyệt
        driver.quit()

# Sử dụng hàm
email = 'letannoc@gmail.com'
password = 'nguyenntngoc2704'
csrf_token = get_csrf_token(email, password)