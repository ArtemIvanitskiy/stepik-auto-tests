from selenium import webdriver
import time, math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
	
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
			
    y = calc(x)
	
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
	

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()	
	
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()
	
	
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
# не забываем оставить пустую строку в конце файла	