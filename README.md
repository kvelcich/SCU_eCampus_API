# SCU eCampus API

Python functions to navigate and use SCU's eCampus.

Example uses include:
* Check if a class is open
* Swap into a class
* Enroll into a class

## Required Libraries
This program is dependent on the python library **selenium**.

In order to use headless browsing, the program uses the python library **pyvirtualdisplay**.

Lastly, for cellphone notifications, the program uses the **Twilio API** for python.

## How To Use
#### 1. Install Python
To install python, download and install a python version from [here.](https://www.python.org/downloads/)

#### 2. Install pip
Next, in order to download the required libraries, install pip following the directions at [pypa.io](https://pip.pypa.io/en/stable/installing/).

#### 3. Install Selenium
Once pip is installed correctly, in order to install the selenium library simply run the following command in the terminal:
```
pip install selenium
```

#### 4. [OPTIONAL] Install PyVirtualDisplay
In order to run headless browsing, i.e. where the graphical UI isn't shown. To install, run the following command in the terminal:
```
pip install pyvirtualdisplay
```

#### 5. [OPTIONAL] Set Up Twilio
* If you want to receive text notifications to your phone, then you will need to first create an account at [Twilio.com](https://www.twilio.com/try-twilio).
* Copy down your Account SID and Authentification Token from the [console page](https://www.twilio.com/console).
* Lastly, get a Twilio phone number, by going [here](https://www.twilio.com/console/phone-numbers/getting-started), and then clicking "Get your first Twilio phone number". Keep note of the number you selected.

#### 6. Download Files

#### 7. Edit config.py values
The file *config.py* contains specific user values for it to run.

1. Enter your eCampus account ID and password in actId and actPwd respectively.
2. If you want to receive phone notifications, enter your phone number into the destCellPhone variable and enter your Twilio phone number, account SID, and authentification token into myTwilioNumber, accountSid and authToken.

#### 8. Edit Main, and Run
Lastly, you need to add your code to the main python file. By default, the main file includes the following code:
```
#swapWhenOpen(55555, 55556, True, True)
```
You can uncomment this line, and this code will attempt to swap the class 55556 for 55555 using headless browsing and notifications.

To run, simply run the command:
```
python main.py
```
* For more information on the functions and API, please refer to the [wiki.](https://github.com/kvelcich/SCU_eCampus_API/wiki)
