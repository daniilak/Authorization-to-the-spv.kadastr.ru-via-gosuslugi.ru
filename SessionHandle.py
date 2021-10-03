from requests import Session
from pickle import load, dump
from config import COOKIES_FILE

def save_cookie( cookies):
    dump(cookies, open(COOKIES_FILE, "wb"))
    print("OK save cookies")

def get_cookie():
    return load(open(COOKIES_FILE, 'rb'))

def get_new_session():
    session = Session()
    cookies = get_cookie()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    return session