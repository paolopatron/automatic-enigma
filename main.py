import pyqrcode


def generateWiFiQRCode(SSID, password, protocol):
    QRCode = pyqrcode.create(F'WIFI:S:{SSID};T:{protocol};P:{password};;')
    QRCode.png(F'WiFi-{SSID}.png', scale=6)
    QRCode.show()


SSID = input("SSID: ")
password = input("Password: ")
protocol = input("Protocol (press enter key to use WPA/WPA2 by default): ")

if len(protocol) == 0:
    protocol = 'WPA/WPA2'

generateWiFiQRCode(SSID, password, protocol)