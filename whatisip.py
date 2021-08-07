import network
LAN = network.WLAN(network.STA_IF)
AP = network.WLAN(network.AP_IF)

if LAN.active():
    print('LAN IP:\n',LAN.ifconfig())



