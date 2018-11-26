#全家行動購
#請勿濫用，不要沒事亂DOS別人
#請安裝selenium
#請先把chrome更新至最新版，並下載chromedriver
#以下程式所有的time.sleep()都是我電腦、網路爛才需要，請使用者自行拔掉(但下一步之後的要留一下，會需要等轉場動畫)
#請記得點店鋪
from selenium import webdriver
#import datetime
import time

#輸入資訊  須訂購網址、代訂購時間、件數...等(懶的寫，自己用datetime減，然後time.sleep(相減的時間))
#booktime = ''
#number_of_pieces = ''
phoneNUM = '0987654321' #登入帳號
password = 'abcdefghijklmn' #登入密碼
name = 'WTFa' #收件人姓名(必填)
e_mail = 'WTFa@gmail.com'  #收件人信箱(必填)
web = webdriver.Chrome()
net = 'https://mart.family.com.tw/SalePage/Index/4562487'

#####################################
web.get(net)    #open chrome
'''             #注意，以下註解是訂購數量，但有多項商品無法大量訂購
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='數量'])[1]/following::input[1]").click()
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='數量'])[1]/following::input[1]").clear()
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='數量'])[1]/following::input[1]").send_keys(number_of_pieces)
'''
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='立即結帳'])").click()
#######################過場中#########################
time.sleep(5)
web.find_element_by_name("ctl00$ctl00$PageContent$PageContent$tbMobile").send_keys(phoneNUM)
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='忘記密碼'])[1]/following::ins[1]").click()
web.find_element_by_id("PageContent_PageContent_tbPassword").clear()
web.find_element_by_id("PageContent_PageContent_tbPassword").send_keys(password)
web.find_element_by_id("btn_login").click()
#######################過場中#########################
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='下一步'])").click()
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='下一步'])").click()
time.sleep(3)
web.find_element_by_id("memberStoreReceiverFullName").click()
web.find_element_by_id("memberStoreReceiverFullName").clear()
web.find_element_by_id("memberStoreReceiverFullName").send_keys(name)
web.find_element_by_id("receiverEmailForWeb").click()
web.find_element_by_id("receiverEmailForWeb").clear()
web.find_element_by_id("receiverEmailForWeb").send_keys(e_mail)

web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='請選擇取貨門市'])[1]/following::div[2]").click()
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='高雄市'])").click()
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='左營區'])").click()
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='孟子路'])").click()
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='全家高雄孟子店'])").click()
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='確定店鋪'])").click()
time.sleep(5)
#我不敢按送出，要的話把下面解除看看，理論上正確
#web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='送出'])").click()
#紀錄訂購資料
#web.get_screenshot_as_file("screenshot.png")

'''##########店名查詢#########(didnt run)
wev.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='店名查詢'])").click
web.find_element_by_id("sn1").click()
web.find_element_by_id("sn1").clear()
web.find_element_by_id("sn1").send_keys('全家高雄孟子店')
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='確定'])").click()
#web.find_element_by_class_name("StoreListM").click
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='全家高雄孟子店'])").click()
time.sleep(3)
web.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='確定店鋪'])").click()
'''
'''##########店號查詢#########
#fail search
'''