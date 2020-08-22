from selenium import webdriver
import time, math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    x_element = browser.find_element_by_id('num1')
    x = int(x_element.text)
	
    y_element = browser.find_element_by_id('num2')
    y = int(y_element.text)
	
    sumxy = str(x + y)
	
    select = Select(browser.find_element_by_tag_name("select")) 
    select.select_by_value(sumxy)
	
	
	
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
	

# не забываем оставить пустую строку в конце файла	