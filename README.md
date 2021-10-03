# Авторизация на сайт spv.kadastr.ru через gosuslugi.ru

# Требования
1. python > 3.5
2. pip: pybase64, selenium

## Настройка config.py

1. В EXECUTABLE_PATH_WEBDRIVER должен быть путь до драйвера хрома. Скачать можно здесь: https://chromedriver.chromium.org/downloads
2. COOKIES_FILE - название pickle файла, в котором будут хранится кукис сайта
3. CAPTCHA - параметры для прохождения вопросов об аккаунте в госуслугах
4. LOGIN - логин к госуслугам
5. PASS - пароль к госуслугам
6. CAPTCHA_API_KEY - ключ к прохождения буквенной капчи
7. PROXY - логин/пароль/ip/port (no_proxy - не нужно изменять)
