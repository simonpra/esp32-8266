#########################################
### NOT YET READY #######################
#########################################
from network import WLAN, STA_IF
from ntptime import settime
# import picoweb

def connect():
    ssid = "YOUR SSID"
    password =  "YOUR PASSWORD"

    station = WLAN( STA_IF )

    if station.isconnected() is True:
        print("Already connected")
        config = station.ifconfig()
        ip = config[0]
        print( "ip : "+str( ip ) )
        # print( "starting webserver --------" )
        # webserver( ip )
        ### SETTING time RTC
        print( "SETTING RTC --------" )
        settime()
        return

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() is False:
        pass

    print("Connection successful")

    config = station.ifconfig()
    ip = config[0]
    print( "ip : "+str( ip ) )
    ### SETTING time RTC
    print( "SETTING RTCr --------" )
    settime()
    # print( "starting webserver --------" )
    # webserver( ip )

# def webserver( ip ) :
#     app = picoweb.WebApp(__name__)

#     @app.route("/")
#     def index(req, resp):
#         yield from picoweb.start_response(resp)
#         yield from resp.awrite("Hello world from picoweb running on the ESP32")

#     app.run(debug=True, host = ip)
