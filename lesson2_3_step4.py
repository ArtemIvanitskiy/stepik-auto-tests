from selenium import webdriver
import time, math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    button = browser.find_element_by_css_selector("button")
    button.click()
	
    alert = browser.switch_to.alert
    alert.accept()
	
	
    time.sleep(2)
	
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
	
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
			
    y = calc(x)
	
	
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

	
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
# не забываем оставить пустую строку в конце файла	