import os
import getpass
import time

name = "hotspot4windows"


def checkwirelesscard():
    os.system("netsh wlan show interfaces")


def launch():
    failtimes = 0
    for failtimes in range(3):
        ssid = input("Please enter SSID:")
        passwd = getpass.getpass("Please enter password:")
        passwd2 = getpass.getpass("Pleast enter password again:")
        print("Checking password......")
        time.sleep(1)
        if passwd == passwd2:
            print("Password validation is OK!")
            time.sleep(1)
            print("Preparing wireless hotspot......")
            time.sleep(1)
            print("Launching wireless hotspot")
            os.system("netsh wlan set hostednetwork mode=allow ssid=%s key=%s" % (ssid, passwd))
            os.system("netsh wlan start hostednetwork")
            print("OK!")
            time.sleep(2)
            break
        else:
            failtimes = failtimes + 1
            print("Password validation is Failed! You have failed for %s times" % failtimes)
            time.sleep(2)
    else:
        print("You have failed for 3 times, please try again later.")
        time.sleep(2)
        exit()


def starthotspot():
    os.system("netsh wlan start hostednetwork")


def stophotspot():
    os.system("netsh wlan stop hostednetwork")


def allow():
    os.system("wlan set hostednetwork mode=allow")


def disallow():
    os.system("netsh wlan set hostednetwork mode=disallow")


def hotspotinfo():
    os.system("netsh wlan show hostednetwork")


def faststart(ssid, password):
    os.system("netsh wlan set hostednetwork mode=allow ssid=%s key=%s" % (ssid, password))
    os.system("netsh wlan start hostednetwork")
    print("OK!")
    time.sleep(2)
