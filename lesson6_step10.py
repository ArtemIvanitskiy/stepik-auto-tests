from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Мой код, который заполняет обязательные поля
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .form-group .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".form-control.third")
    input3.send_keys("test@test.ru")
    input4 = browser.find_element_by_css_selector('input[placeholder="Input your phone:"]') # текст о вводе телефона более стабилен, чем об адресе. Потому что вероятнее, что станут точнее сообщать пояснение о формате ввода адреса, чем о формате телефона.
    input4.send_keys("+7123456723")
    input5 = browser.find_element_by_css_selector(".second_block .second_class:nth-child(2) .form-control.second") #'input[placeholder="Input your address:"]' можно и так, но все же надёжнее поиск по классам
    input5.send_keys("Angels.45")	
	
	
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
# не забываем оставить пустую строку в конце файла	