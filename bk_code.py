from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from dotenv import load_dotenv
from os import environ
import os
load_dotenv()

PESTI_UTI_CODE = 29175

def getWhopperCode():
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument("--disable-gpu")
        #chrome_options.add_argument("--disable-crash-reporter")
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument("--disable-in-process-stack-traces")
        #chrome_options.add_argument("--disable-logging")
        #chrome_options.add_argument("--disable-dev-shm-usage")
        #chrome_options.add_argument("--log-level=3")
        #chrome_options.add_argument("--output=/dev/null")
        chromedriver_path = os.path.join(os.getcwd(),environ.get("CHROMEDRIVER_PATH"))
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        wait = WebDriverWait(driver, 10)

        
        def pressNextButton():
            button =  wait.until(EC.element_to_be_clickable((By.ID, 'NextButton')))
            button.click()


        def waitUntilPageLoaded():
            sleep(3)

                
        driver.get("https://www.burgerkingelmenyem.hu/")
        driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'Home_iframe__T3nfU'))
        input_field = wait.until(EC.presence_of_element_located((By.ID, 'QR\~QID4')))
        input_field.send_keys(PESTI_UTI_CODE)
        sleep(2)
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.ENTER)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys("08")\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys("0")\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys(Keys.ARROW_DOWN)\
            .send_keys(Keys.ARROW_DOWN)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()

        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.ARROW_DOWN)\
            .send_keys(Keys.ARROW_DOWN)\
            .send_keys(Keys.SPACE)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()

        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.ARROW_DOWN)\
            .send_keys(Keys.SPACE)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
                .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
                .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
                .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
                .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
                .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()
        
        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.ARROW_DOWN)\
            .send_keys(Keys.TAB)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()

        ActionChains(driver)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .send_keys(Keys.TAB)\
            .send_keys(Keys.SPACE)\
            .perform()
        pressNextButton()
        waitUntilPageLoaded()
        for i in range(0, 24):
            ActionChains(driver)\
                .send_keys(Keys.TAB)\
                .perform()
        ActionChains(driver)\
                .send_keys(Keys.SPACE)\
                .perform()
        pressNextButton()
        waitUntilPageLoaded()
        for i in range(0, 12):
            ActionChains(driver)\
                .send_keys(Keys.TAB)\
                .perform()
        ActionChains(driver)\
                .send_keys(Keys.SPACE)\
                .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
                .send_keys(Keys.TAB)\
                .send_keys(Keys.SPACE)\
                .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
                .send_keys(Keys.TAB)\
                .send_keys(Keys.ARROW_DOWN)\
                .send_keys(Keys.SPACE)\
                .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
                .send_keys(Keys.TAB)\
                .send_keys(Keys.SPACE)\
                .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
                .send_keys(Keys.TAB)\
                .send_keys(Keys.SPACE)\
                .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
                .send_keys(Keys.TAB)\
                .send_keys(Keys.SPACE)\
                .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
                .send_keys(Keys.TAB)\
                .send_keys(Keys.SPACE)\
                .perform()
        pressNextButton()
        waitUntilPageLoaded()
        ActionChains(driver)\
                .send_keys(Keys.TAB)\
                .send_keys(Keys.ARROW_DOWN)\
                .send_keys(Keys.SPACE)\
                .perform()
        pressNextButton()
        waitUntilPageLoaded()
        pressNextButton()
        waitUntilPageLoaded()
        pressNextButton()
        waitUntilPageLoaded()
        textElement = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="EndOfSurvey"]')))
        whopperCode = textElement.text.split("kód: ")[1].split("\n")[0]
        driver.quit()
        return whopperCode
    except KeyboardInterrupt:
        driver.quit()
        return "Something went wrong"