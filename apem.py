import speech_recognition as sr
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
class Apem(object): 
    def __init__(self, npm, paswd):
        self.npm = npm
        self.paswd = paswd
    def masuk(self): 
        self.opsi = Options()
       #penyelesaian issue 40
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver= webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/')

    def login(self): 
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver= webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()

    def speak(self):
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("SAY SOMETHING, PLEASE")
            audio = r.listen(source)
        try:
            print("TEXT : "+r.recognize_google(audio, language='id-ID'))
            x = "siap"
            y = "login siap"
            if (r.recognize_google(audio, language='id-ID')) == x:
                self.masuk()
            if (r.recognize_google(audio, language='id-ID')) == y:
                self.login()
        except Exception as e:
            print(e)
            print("error")
 
        print("Time is over, thanks") 