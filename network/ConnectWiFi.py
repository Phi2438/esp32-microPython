'''
  module to connect to network -  esp32
  
'''
def connect():
    import network
 
    ssid = "SSID"
    password =  "PASSWORD"
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected():
        print("Already connected")
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while not station.isconnected():
        pass
 
    print("Connection successful")
    print(station.ifconfig())