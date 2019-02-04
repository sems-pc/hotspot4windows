import os
import getpass
import time

name = "hotspot4windows"


class Hotspot:
    def allow(self):
        os.system("wlan set hostednetwork mode=allow")

    def disallow(self):
        os.system("netsh wlan set hostednetwork mode=disallow")

    def launch(self):
        ssid = input("Please enter SSID:")
        passwd = getpass.getpass("Please enter password:")
        passwd2 = getpass.getpass("Pleast enter password again:")
        print("Checking password......")
        time.sleep(1)
        if passwd == passwd2:
            print("Password validation is OK!")
            time.sleep(1)
            print("Launching wireless hotspot......")
            os.system("netsh wlan set hostednetwork mode=allow ssid=%s key=%s" % (ssid, passwd))
            os.system("netsh wlan start hostednetwork")
            print("OK!")

    def wifiinfo(self):
        os.system("netsh wlan show hostednetwork")

    def starthotspot(self):
        os.system("netsh wlan start hostednetwork")

    def stophotspot(self):
        os.system("netsh wlan stop hostednetwork")


Hotspot = Hotspot()
