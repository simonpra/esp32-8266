#########################################
### NOT YET READY #######################
#########################################
import usocket as socket
import ussl
from machine import Pin, I2C
from utime import time

signal = I2C( scl=Pin(5), sda=Pin(4) )

def readTemp() :
    ### DEFAULT address du sensor en I2C = 24
    ### l'adresse de registre où est stockée la température = 5
    ### On récupère 16bits = 2 bytes !
    ### [up] contien le UpperByte et [low] le LowerByte
    [up, low] = signal.readfrom_mem(24, 5, 2)

    ### la dataSheet pour le MCP9808 donne la correspondance des bits
    ### les 4 premiers bits de [up] définissent différents éléments de précision
    ### on récupère la valeur des 4 derniers bits du UpperByte (masque binaire)
    upVal = up & 0xF
    ### on prend directement la valeur du LowerByte
    lowVal = low

    ### calcul de la température en °C
    temp = upVal*16 + lowVal/16

    ### le 4ème bits (0x10) définit le SIGN demandant de soustraire la valeur à 256 (pour les températures négatives)
    if up & 0x10 :
        temp = 256 - temp

    return temp

def sendTemp( url ) :
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 443)[0][-1]

    ### variables GET
    get = str(
        '?t='+ str( 'readTemp()' )
    )

    path = path + get

    print( dir( socket ) )

    request = (
        ('GET /%s HTTP/1.0'  +"\r\n"+
        'Host: %s'          +"\r\n"+
        'User-Agent: esp32'    +"\r\n\r\n")
        % (path, host)
    )

    print( addr )
    ### SSL pour HTTPS
    s = socket.socket(  )
    s.connect( addr )
    s = ussl.wrap_socket( s )
    print( s )
    # ss.connect( addr )

    # s = socket.socket()
    # s.connect(addr)

    # try :
    #     s = wrap_socket(s)
    # except OSError as error :
    #     print(error)

    s.write( bytes(request, 'utf8') )
    while True:
        data = s.read(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
