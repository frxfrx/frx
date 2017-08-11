from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://accounts.douban.com/register'
driver.get(url)
driver.implicitly_wait(10)
# 点击输入邮箱
driver.find_element_by_id('email').click()
driver.find_element_by_id('email').send_keys('652195552@qq.com')
time.sleep(1)
# 点击输入密码
driver.find_element_by_id('password').click()
driver.find_element_by_id('password').send_keys('652195552.')
time.sleep(1)
# 点击输入名号
driver.find_element_by_id('name').click()
driver.find_element_by_id('name').send_keys('略略')
time.sleep(1)
driver.find_element_by_id('edloc').click()
driver.find_element_by_id('108288').click()
# 点击输入手机号
driver.find_element_by_id('verify_phone_num').click()
driver.find_element_by_id('verify_phone_num').send_keys('17610097217')
time.sleep(1)
# 点击获取验证码
driver.find_element_by_id('request-phone-code-btn').click()
# 点击验证码框
driver.find_element_by_id('captcha').click()
time.sleep(10)
# 点击确定
driver.find_element_by_id('captcha_dialog-bn-1').click()
time.sleep(1)
# 点击输入验证码
driver.find_element_by_id('code').click()
time.sleep(10)
# 点击同意
driver.find_element_by_id('agreement').click()
# 点击注册
driver.find_element_by_id('button').click()
time.sleep(1)
driver.quit()
