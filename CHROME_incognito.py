import time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Havent chrome driver
executable_path = "C:\\Users\\user\Desktop\\20181121\\Python-Practice\\chromedriver.exe"

chrome_options = Options()

# Private browsing
chrome_options.add_argument("--incognito")

# To use my default extension
#chrome_options.add_argument(r"user-data-dir=C:\Users\Mika\AppData\Local\Google\Chrome\User Data")

driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
#driver.get("http://google.com")
time.sleep(6)  # 6 seconds sleep/delay
driver.quit()
'''
from selenium import webdriver
PROXY = "proxy_host:proxy:port"
options = webdriver.ChromeOptions()
desired_capabilities = options.to_capabilities()
desired_capabilities[‘proxy‘] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}
driver = webdriver.Chrome(desired_capabilities = desired_capabilities)

chrome--incognito
'''