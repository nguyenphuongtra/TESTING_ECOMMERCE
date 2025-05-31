import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'http://localhost:3000'

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# TC01: Đăng nhập thành công
def test_TC01_login_success(driver):
    driver.get(f"{BASE_URL}/signin")
    driver.find_element(By.NAME, "email").send_keys("superadmin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, '[data-testid="signin-btn"]').click()
    WebDriverWait(driver, 10).until(EC.url_to_be(f"{BASE_URL}/"))
    assert "login" not in driver.current_url

# TC02: Email sai định dạng
def test_TC02_login_invalid_email(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "email").send_keys("superadmingmail.com")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, '[data-testid="signin-btn"]').click()
    error = driver.find_element(By.CLASS_NAME, "error").text
    assert "@" in error or "không hợp lệ" in error.lower()

# TC03: Mật khẩu trống
def test_TC03_login_empty_password(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "email").send_keys("superadmin@gmail.com")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.CSS_SELECTOR, '[data-testid="signin-btn"]').click()
    error = driver.find_element(By.CLASS_NAME, "error").text
    assert "mật khẩu" in error.lower()

# TC04: Đăng ký thành công
def test_TC04_register_success(driver):
    driver.get(f"{BASE_URL}/signup")
    driver.find_element(By.NAME, "email").send_keys("user3@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("user123")
    driver.find_element(By.NAME, "passwordConfirm").send_keys("user123")
    signup_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    signup_btn.click()
    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    assert "login" in driver.current_url or "signin" in driver.current_url

# TC05: Mật khẩu không khớp
def test_TC05_register_password_mismatch(driver):
    driver.get(f"{BASE_URL}/signup")
    driver.find_element(By.NAME, "email").send_keys("user2@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("pass123")
    driver.find_element(By.NAME, "passwordConfirm").send_keys("pass456")
    signup_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    signup_btn.click()
    error = driver.find_element(By.CLASS_NAME, "error").text
    assert "không khớp" in error.lower()

# TC06: Email trống
def test_TC06_register_empty_email(driver):
    driver.get(f"{BASE_URL}/signup")
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "password").send_keys("pass123")
    driver.find_element(By.NAME, "passwordConfirm").send_keys("pass123")
    signup_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    signup_btn.click()
    error = driver.find_element(By.CLASS_NAME, "error").text
    assert "email" in error.lower()

# TC07: Quên mật khẩu không nhập email
def test_TC07_forgot_password_empty_email(driver):
    driver.get(f"{BASE_URL}/forgot-password")
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.XPATH, "//button[contains(text(),'Send Instructions') or contains(text(),'Reset')]").click()
    error = driver.find_element(By.CLASS_NAME, "error").text
    assert "email" in error.lower() or "vui lòng" in error.lower()

# TC08: Thêm sản phẩm vào giỏ
def test_TC08_add_to_basket(driver):
    driver.get(f"{BASE_URL}/")
    add_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="add-to-basket-btn"]'))
    )
    add_btn.click()
    remove_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="remove-from-basket-btn"]'))
    )
    assert remove_btn.is_displayed()

# TC09: Thêm sản phẩm vào cart
def test_TC09_add_to_cart(driver):
    driver.get(f"{BASE_URL}/")
    add_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
    add_btn.click()
    remove_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Remove from Cart')]")
    assert remove_btn.is_displayed()

# TC10: Xoá sản phẩm khỏi giỏ
def test_TC10_remove_from_basket(driver):
    driver.get(f"{BASE_URL}/basket")
    remove_btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="remove-from-basket-btn"]')
    remove_btn.click()
    add_btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="add-to-basket-btn"]')
    assert add_btn.is_displayed()
