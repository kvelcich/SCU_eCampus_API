from values.config import *
from values.values import *
import time
from twilio.rest import TwilioRestClient
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

#Enables headless browsing
def headlessBrowsing():
    display = Display(visible=0, size=(800, 600))
    display.start()

#Load webpage in Firefox driver. returns the driver
def loadPage(url):
    print "Loading web page"
    driver = webdriver.Firefox()
    driver.get(url)
    return driver

#Function that logs into eCampus
def login(driver):
    print "Logging in"
    driver.find_element_by_id("userid").send_keys(actId)
    pwd = driver.find_element_by_id("pwd")
    pwd.send_keys(actPwd)
    pwd.send_keys(Keys.ENTER)

#Function that navigates to the enroll form from the ecampus home page.
def gotoEnroll(driver):
    print "Navigating to enrollment"
    attempts = 0
    while True:
        sleep(SLEEP_TIME_LONG)
        try:
            driver.find_element_by_id("DERIVED_SSS_SCR_SSS_LINK_ANCHOR2").click()
            return True
        except:
            print "Retrying..."
            attempts += 1
            if attempts == 10:
                return False

#Function that navigates to the swap form from the ecampus home page.
def gotoSwap(driver):
    print "Selecting swap"
    attempts = 0
    while True:
        sleep(SLEEP_TIME_LONG)
        try:
            select = Select(driver.find_element_by_name("DERIVED_SSS_SCL_SSS_MORE_ACADEMICS"))
            select.select_by_value("1015")
            driver.find_element_by_id("DERIVED_SSS_SCL_SSS_GO_1").click()
            return True
        except:
            print "Retrying..."
            attempts += 1
            if attempts == 10:
                return False

#Function that switches selenium frame
def switchFrame(driver, frame):
    print "Changing frames"
    attempts = 0
    while True:
         sleep(SLEEP_TIME_SHORT)
         try:
             driver.switch_to.frame(driver.find_element_by_id(frame))
             return True
         except:
             print "Retrying..."
             attempts += 1
             if attempts == 10:
                return False

#Function that selects which quarter/session to check
def selectSession(driver, session):
    print "Selecting quarter"
    attemps = 0
    while True:
        sleep(SLEEP_TIME_SHORT)
        try:
            driver.find_element_by_id(session).click()
            driver.find_element_by_id("DERIVED_SSS_SCT_SSR_PB_GO").click()
            return True
        except Exception:
            print "Retrying..."
            attempts += 1
            if attempts == 10:
                return False

#Function that enters, and searches a class to search for from the enroll screen.
def enrollSearch(driver, courseIn):
    print "Entering class number"
    attempts = 0
    while True:
        sleep(SLEEP_TIME_SHORT)
        try:
            driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR").send_keys(courseIn)
            driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$").click()
            return True
        except:
            print "Retrying..."
            attempts += 1
            if attempts == 10:
                return False

#Function that sets up to swap two classes passed in
def swapSetup(driver, courseIn, courseOut):
    print "Selecting courses to swap"
    attempts = 0
    while True:
        sleep(SLEEP_TIME_SHORT)
        try:
            select = Select(driver.find_element_by_id("DERIVED_REGFRM1_DESCR50$225$"))
            select.select_by_value(courseOut)
            classInput = driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR")
            classInput.send_keys(courseIn)
            driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$106$").click()
            return True
        except:
            print "Retrying..."
            attempts += 1
            if attempts == 10:
                return False

#Function that attempts to swap classes
def swapAttempt(driver):
    print "Attempting to swap"
    attempts = 0
    while True:
        sleep(SLEEP_TIME_SHORT)
        try:
            driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB").click()
            break
        except:
            print "Retrying..."
            attempts += 1
            if attempts == 10:
                return False
    attemps = 0
    while True:
        sleep(SLEEP_TIME_SHORT)
        try:
            print "click"
            driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_SUBMIT").click()
            return True
        except:
            print "Retrying..."
            attempts += 1
            if attempts == 10:
                return False

#Function that reads the feedback messages from a swap attempt
def swapFeedback(driver):
    print "Reading message"
    attempts = 0
    while True:
        sleep(SLEEP_TIME_XL)
        try:
            return driver.find_element_by_id("win1divDERIVED_REGFRM1_SS_MESSAGE_LONG$0").text
        except:
            print "Retrying..."
            attempts += 1
            if attempts == 10:
                return ""

#Function that notifies based on the swap feedback messages
def swapNotify(driver, enrollMsg, notifications):
    if enrollMsg[:5] in ['Error']:
        print "Error enrolling."
        if notifications:
            notify("Error enrolling in course...")
            notify(enrollMsg)
    else:
        print "Successfully enrolled!"
        if notifications:
            notify("Success in enrolling!")

#Function that checks the class capacity. Returns the class size information text
def checkCapacity(driver):
    print "Checking class capacity"
    attempts = 0
    while True:
        sleep(SLEEP_TIME_SHORT)
        try:
            capacity = driver.find_element_by_id("DERIVED_CLS_DTL_SSR_DESCRSHORT$0")
            break
        except:
            print "Retrying..."
            attempts += 1
            if attempts == 10:
                return False

    if capacity.text in ['Closed']:
        return False
    elif capacity.text in ['Open']:
        return True

#Function sleeps and prints out time until complete
def sleep(SLEEP_TIME):
    #print "Sleeping..."
    for i in range(SLEEP_TIME, 0, -1):
        #print i
        time.sleep(1)
    #print "Sleep end!"

#Function sends an sms with notification
def notify(msg):
    twilioClient = TwilioRestClient(accountSid, authToken)
    myMessage = twilioClient.messages.create(body = msg, from_ = myTwilioNumber, to = destCellPhone)

def notifyTimes(msg, count):
    twilioClient = TwilioRestClient(accountSid, authToken)
    for i in range(0, count):
        myMessage = twilioClient.messages.create(body = msg, from_ = myTwilioNumber, to = destCellPhone)
        sleep(SLEEP_TIME_SHORT)
