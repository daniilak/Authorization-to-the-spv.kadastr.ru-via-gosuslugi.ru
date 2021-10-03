from base64 import b64encode
from urllib.request import urlopen
from time import sleep

from SessionHandle import get_new_session
from config import CAPTCHA_API_KEY

class CaptchaSolver:
    
    def __init__(self, url) -> None:
        if self.save_image_captcha(url):
            print("OK save_image_captcha")
        img = open('img.jpg', 'rb')
        self.img_str = b64encode(img.read()).decode('ascii')
        img.close()
    
        
    def save_image_captcha(self, url):
        try:
            img = urlopen(url).read()
        except Exception as e:
            print("error img urlopen requerst", str(e))
            exit()
        out = open("img.jpg", "wb")
        out.write(img)
        out.close()
        return True
    
    def create_tasks(self):
        el_json = {
            'clientKey':CAPTCHA_API_KEY,
            'languagePool':'rn',
            'task': {
                "type":"ImageToTextTask",
                "body":self.img_str,
                "phrase":False,
                "case":False,
                "numeric":0,
                "math":False,
                "minLength":0,
                "maxLength":0
            }
        }
        self.session = get_new_session()
        task = self.session.post("https://api.anti-captcha.com/createTask", json=el_json)
        task = task.json()
        self.taskID = task['taskId']
        return self.taskID

    def get_task_result(self):
        el_json = {
            'clientKey':CAPTCHA_API_KEY,
            'taskId':str(self.taskID),
        }
        task = self.session.post("https://api.anti-captcha.com/getTaskResult", json=el_json)
        return task.json()
    
    def whiler(self):
        while True:
            sleep(5)
            answer_task = self.get_task_result()
            if answer_task['status'] == 'ready':
                return answer_task['solution']['text']