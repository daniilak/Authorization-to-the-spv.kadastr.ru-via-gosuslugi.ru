COOKIES_FILE = 'cookies.pkl'
EXECUTABLE_PATH_WEBDRIVER = '/usr/bin/chromedriver'


CAPTCHA = {
        "carNumber": "А123БВ456",
        "yearDriveLicense": "2021",
        "birthMonthAndDay": "01.2021",
        "birthDayAndMonth": "01.01",
        "passport": "12",
        "num_house": "1", 
        "num_house_proj": "1",
        "year_passport": "2021",
        "last_4_DriveLicence": "1234",
        "passportLast2":"34",
        "passportFirst2": "12"
}

LOGIN = ''
PASS = ''

CAPTCHA_API_KEY = ''

PROXY = [
    {
        'http': 'http://login:pass@192.168.0.1:8000', 
        'https': 'https://login:pass@192.168.0.1:8000',
        'no_proxy': 'localhost,127.0.0.1'
    },
    {
        'http': 'http://login:pass@192.168.0.1:8000', 
        'https': 'https://login:pass@192.168.0.1:8000',
        'no_proxy': 'localhost,127.0.0.1'
    },
]
