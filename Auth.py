
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from random import choice

from SessionHandle import save_cookie
from CaptchaSolver import CaptchaSolver
from config import CAPTCHA, LOGIN, PASS, PROXY, EXECUTABLE_PATH_WEBDRIVER

def get_chrome():
    print("START get_chrome")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    proxy = {'proxy': choice(PROXY)}
    d = webdriver.Chrome(executable_path=EXECUTABLE_PATH_WEBDRIVER, seleniumwire_options=proxy, options=chrome_options)
    return d


def not_found(d,quest):
    answer_auth =  d.find_element_by_css_selector('div.b-anomaly-form__title')
    f = open('log_auth.txt' , 'a')
    f.write(quest + '\n')
    f.close()
    exit()

def captcha(d):
    quest = d.find_element_by_css_selector('label.b-anomaly-form__question')
    submit = d.find_element_by_css_selector('button#button-reqinfo-submit')
    quest = quest.text.strip()
    print(quest)
    answer = ''
    if quest == 'Государственный регистрационный номер транспортного средства':
        answer = CAPTCHA['carNumber']
    if quest == 'Первые 2 цифры номера паспорта':
        answer = CAPTCHA['passport']
    if quest == 'Последние 2 цифры номера паспорта':
        answer = CAPTCHA['passportLast2']

    if quest == 'Год выдачи водительского удостоверения':
        answer = CAPTCHA['yearDriveLicense']
    if quest == 'Месяц и год вашего рождения':
        answer = CAPTCHA['birthMonthAndDay']
    if quest == 'Номер дома адреса регистрации':
        answer = CAPTCHA['num_house']
    if quest == 'Дата и месяц вашего рождения':
        answer = CAPTCHA['birthDayAndMonth']
    if quest == 'Номер дома из адреса проживания':
        answer = CAPTCHA['num_house_proj']
    if quest == 'Год выдачи российского паспорта':
        answer = CAPTCHA['year_passport']
    if quest == 'Последние 4 цифры водительского удостоверения':
        answer = CAPTCHA['last_4_DriveLicence']
    if quest == "Первые 2 цифры номера паспорта":
        answer = CAPTCHA['passportFirst2']

    answer_field =  d.find_element_by_css_selector('input#answer')
    answer_field.send_keys(answer)
    sleep(1)
    submit.click()
    sleep(1)
    if d.find_elements_by_css_selector('div.b-anomaly-form__title'):
        not_found(d, quest)
    return True


def auth():
    print("START auth")
    d = get_chrome()
    d.get('https://spv.kadastr.ru/api/v1/login')
    sleep(5)
    try:
        login_field = d.find_element_by_css_selector('input#login')
    except:
        print(d.page_source)
    pass_field = d.find_element_by_css_selector('input#password')
    submit = d.find_element_by_css_selector('.button-big')
    login_field.send_keys(LOGIN)
    pass_field.send_keys(PASS)
    sleep(2)
    submit.click()
    sleep(2)
    try:
        elem = d.find_element_by_id("epgu-captcha")
        code = d.find_element_by_id("code")
        submit_captcha = d.find_element_by_id('button-captcha-submit')
        print(elem.get_attribute("src"))
        src = elem.get_attribute("src")
        captcha_obj = CaptchaSolver(src)
        captcha_obj.create_tasks()
        res = captcha_obj.whiler()
        print(res)
        code.send_keys(res)
        sleep(1)
        submit_captcha.click()
        sleep(1)
    except:
        print("OK")
    if d.find_elements_by_css_selector('label.b-anomaly-form__question'):
        captcha(d)
    sleep(3)
    d.get('https://spv.kadastr.ru/')
    sleep(1)
    print("OK auth")
    save_cookie(d.get_cookies())
    d.quit()
