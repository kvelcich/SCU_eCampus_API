from util import *

#Function continuously checks until a course is opens. Once it it is, attempts to swap.
def swapWhenOpen(courseIn, courseOut, headless, notifications):
    if (headless):
        headlessBrowsing()

    while True:
        open = isOpen(courseIn)
        if open:
            print "Course is open."
            if notifications:
                notifyTimes("Course " + courseIn + " is currently open...", 3)
                notify("Attempting to swap into " + courseIn + "...")
            swap(courseIn, courseOut)
            break
        else:
            print "Course is closed. Trying again in 5 minutes..."
            print "Current time: " + time.strftime('%X') + "\n"
            sleep(300)

#Checks if a passed in course is open
def isOpen(courseIn):
    driver = loadPage(url)
    login(driver)

    if not gotoEnroll(driver):
        print "Error in attempt. Restarting process...\n"
        driver.quit()
        return isOpen(courseIn)

    if not switchFrame(driver, ENROLL_FRAME):
        print "Error in attempt. Restarting process...\n"
        driver.quit()
        return isOpen(courseIn)

    if not selectSession(driver, SESSION_SPRING2017):
        print "Error in attempt. Restarting process...\n"
        driver.quit()
        return isOpen(courseIn)

    if not enrollSearch(driver, courseIn):
        print "Error in attempt. Restarting process...\n"
        driver.quit()
        return isOpen(courseIn)

    open = checkCapacity(driver)
    driver.quit()
    return open

#Function attempts to swap a course.
def swap(courseIn, courseOut, notifications):
    driver = loadPage(url)
    login(driver)

    if not gotoSwap(driver):
        print "Error in attempt. Restarting process...\n"
        driver.quit()
        return swap(courseIn, courseOut)

    if not switchFrame(driver, ENROLL_FRAME):
        print "Error in attempt. Restarting process...\n"
        driver.quit()
        return swap(courseIn, courseOut)

    if not selectSession(driver, SESSION_SPRING2017):
        print "Error in attempt. Restarting process...\n"
        driver.quit()
        return swap(courseIn, courseOut)

    if not swapSetup(driver, courseIn, courseOut):
        print "Error in attempt. Restarting process...\n"
        driver.quit()
        return swap(courseIn, courseOut)

    if not swapAttempt(driver):
        print "Error in attempt. Restarting process...\n"
        driver.quit()
        return swap(courseIn, courseOut)

    enrollMsg = swapFeedback(driver)
    swapNotify(driver, enrollMsg, notifications)

    print "Ending session..."
    driver.quit()
