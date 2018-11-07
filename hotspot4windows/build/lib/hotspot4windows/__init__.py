import os

name = "hotspot4windows"


class Hotspot:
    def allow(self):
        os.system("wlan set hostednetwork mode=allow")

    def disallow(self):
        os.system("netsh wlan set hostednetwork mode=disallow")

    def launch(self):   # 目前只能通过该Python包设置热点名称和密码，这是下一版本要解决的地方。
        ssid = input("Please enter SSID:")
        passwd = input("Please enter password:")
        os.system("netsh wlan set hostednetwork mode=allow ssid=%s key=%s" % (ssid, passwd))
        os.system("netsh wlan start hostednetwork")

    def wifiinfo(self):
        os.system("netsh wlan show hostednetwork")

    def starthotspot(self):
        os.system("netsh wlan start hostednetwork")

    def stophotspot(self):
        os.system("netsh wlan stop hostednetwork")


Hotspot = Hotspot()
