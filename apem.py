import speech_recognition as sr
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
class Apem(object): 
    def __init__(self, npm, paswd):
        self.npm = npm
        self.paswd = paswd
    def masuk(self): 
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver= webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/')
    def ceknilai1(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[5]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr/td[3]/select/option[5]').click()
        self.driver.find_element_by_class_name('button').click()
    def ceknilai2(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[5]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr/td[3]/select/option[4]').click()
        self.driver.find_element_by_class_name('button').click()
    def ceknilai3(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[5]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr/td[3]/select/option[2]').click()
        self.driver.find_element_by_class_name('button').click()
    def ceknilaipendek(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[5]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr/td[3]/select/option[3]').click()
        self.driver.find_element_by_class_name('button').click()
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
    def kalenderganjil2019(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[6]').click()
        self.driver.find_element_by_class_name('textbox').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[2]/td[2]/select/option[1]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[4]/td[2]/select/option[2]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[5]/td/input').click()
    def kalendergenap2019(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[6]').click()
        self.driver.find_element_by_class_name('textbox').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[2]/td[2]/select/option[2]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[4]/td[2]/select/option[2]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[5]/td/input').click()
    def kalendergenap2018(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[6]').click()
        self.driver.find_element_by_class_name('textbox').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[2]/td[2]/select/option[3]').click() #issue 58
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[4]/td[2]/select/option[2]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[5]/td/input').click()
    def kalenderganjil2018(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[6]').click()
        self.driver.find_element_by_class_name('textbox').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[2]/td[2]/select/option[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[4]/td[2]/select/option[2]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[5]/td/input').click()
    def kalendergenap2017(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[6]').click()
        self.driver.find_element_by_class_name('textbox').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[2]/td[2]/select/option[5]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[4]/td[2]/select/option[2]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[5]/td/input').click()
    def kalenderganjil2017(self):
        self.opsi = Options()
        self.opsi.headless = False
        self.cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
        self.cap['marionette'] = True
        self.driver = webdriver.Firefox()
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys(self.paswd)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/a[6]').click()
        self.driver.find_element_by_class_name('textbox').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[2]/td[2]/select/option[6]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[4]/td[2]/select/option[2]').click()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[5]/td/input').click()
    def speak(self):
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("SAY SOMETHING, PLEASE")
            audio = r.listen(source)
        try:
            print("TEXT : "+r.recognize_google(audio, language='id-ID'))
            x = "siap"
            y = "login siap"
            z = "Cek nilai semester 1"
            a = "Cek nilai semester 2"
            b = "Cek nilai semester 3"
            c = "Cek nilai semester pendek"
            d = "kalender akademik ganjil 2017"
            e = "kalender akademik ganjil 2018"
            f = "kalender akademik ganjil 2019"
            g = "kalender akademik genap 2017"
            h = "kalender akademik genap 2018"
            i = "kalender akademik genap 2019"
            if (r.recognize_google(audio, language='id-ID')) == x:
                self.masuk()
            if (r.recognize_google(audio, language='id-ID')) == y:
                self.login()
            if (r.recognize_google(audio, language='id-ID')) == z:
                self.ceknilai1()
            if (r.recognize_google(audio, language='id-ID')) == a:
                self.ceknilai2()
            if (r.recognize_google(audio, language='id-ID')) == b:
                self.ceknilai3()
            if (r.recognize_google(audio, language='id-ID')) == c:
                self.ceknilaipendek()
            if (r.recognize_google(audio, language='id-ID')) == d:
                self.kalenderganjil2017()
            if (r.recognize_google(audio, language='id-ID')) == e:
                self.kalenderganjil2018()
            if (r.recognize_google(audio, language='id-ID')) == f:
                self.kalenderganjil2019()
            if (r.recognize_google(audio, language='id-ID')) == g:
                self.kalendergenap2017()
            if (r.recognize_google(audio, language='id-ID')) == h:
                self.kalendergenap2018()
            if (r.recognize_google(audio, language='id-ID')) == i:
                self.kalendergenap2019()
        except Exception as e:
            print(e)
            print("error")
 
        print("Time is over, thanks") 