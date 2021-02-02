import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from discordwebhooksnotification import send_msg


driver = None

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })



chromedriver = "chromedirver ends with .exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver,chrome_options=opt,service_log_path='Null')
driver.get("TEAM ANMELDE SEITE")

k=0









def login():
    global driver
    usernamefield = driver.find_element_by_name("loginfmt")
    usernamefield.send_keys("EMAIL")

    sleep(2)

    angemeldetbleibenbutton = driver.find_element_by_id("idSIButton9")
    angemeldetbleibenbutton.click()

    sleep(2)

    userpasswortfield = driver.find_element_by_name("passwd")
    userpasswortfield.send_keys("PASSWORT")
    sleep(2)


    angemeldetbleibenbutton = driver.find_element_by_id("idSIButton9")
    angemeldetbleibenbutton.click()


    sleep(2)

    angemeldetbleibenbutton = driver.find_element_by_id("idSIButton9")
    angemeldetbleibenbutton.click()


def geheaufkursseite(kusrname):
    
    print("Suche nach Kursen...")
    verfügbarekurse = driver.find_elements_by_class_name("team-name-text")
    for i in verfügbarekurse:
        if kusrname.lower() in i.get_attribute('innerHTML').lower():
            
            print(i.get_attribute('innerHTML').lower())
            i.click()
            break
    sleep(5)
    joinmeeting()


def joinmeeting():
    global driver
    
    
    while(True):
        try:
            joinbtn = driver.find_element_by_class_name("ts-calling-join-button")
            joinbtn.click()
            break
        except:
            global k 
            k = k+1
            print("Meeting Button nicht gefunden. Versuche es erneut... Versuch Nr:"+str(k))
            sleep(30)
            driver.refresh()
            sleep(5)
            
			
        
          
         
    
    sleep(5)
    webcam = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
    if(webcam.get_attribute('title')=='Kamera deaktivieren'):
        webcam.click()
        sleep(1)

    microphone = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
    if(microphone.get_attribute('title')=='Mikrofon stummschalten'):
       microphone.click()

    sleep(1)
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    print("Du bist jetzt im Meeting")
    send_msg("Join Benachrichtigung","Du bist jetzt im Meeting")
    
 



sleep(5)
login()
sleep(20)
geheaufkursseite("KURS NAME")





    

    
            
	
	



