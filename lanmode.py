import network
LAN = network.WLAN(network.STA_IF)
AP = network.WLAN(network.AP_IF)
#sta.active()

mode = input("Enter 1 for AP and 2 for Botdemy2 LAN: ")

if mode == '2':
    if not LAN.active():
        #activate station mode
        LAN.active(True)

        #Then connect to your WiFi network:
        LAN.connect('Botdemy2', 'chojins00xx')

    if LAN.isconnected():
        LAN.ifconfig()

        AP.active(False)


