from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    driver_path = "/path/to/chromedriver"
    brave_options = uc.ChromeOptions()
    brave_options.add_argument('no-sandbox')
    brave_options.add_argument('--headless') # it is currently truned off headless method . 
    brave_options.binary_location = "/usr/bin/brave-browser" # put your browser path here .
    driver = uc.Chrome(executable_path=driver_path, options=brave_options)
    driver.get("https://example.com")


# Do your stuffs here ........       

    driver.close()
    driver.quit()
except Exception as e:
    print("Error couldn't run the following . :", e)



